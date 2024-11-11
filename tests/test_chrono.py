"""Tests du chronomètre"""
from time import sleep

import pytest

from chrono.models.chrono import Chrono
from chrono.constants import ROUNDING_PRECISION
from chrono.models.exceptions import StartError, StopError, ResetWhileRunningError, ResetAlreadyAtZeroError

TOLERANCE = float(f"1e-{ROUNDING_PRECISION if ROUNDING_PRECISION > 0 else 0}")
PAUSE = 0.05


@pytest.fixture
def new_chrono():
    return Chrono()


@pytest.fixture
def started_chrono(new_chrono):
    new_chrono.start()
    return new_chrono


@pytest.fixture
def started_and_stopped_chrono(started_chrono):
    sleep(PAUSE)
    started_chrono.stop()
    return started_chrono


def test_chrono_created():
    chrono = Chrono()
    assert chrono is not None
    assert not chrono.start_time
    assert not chrono.stop_time
    assert chrono.value == 0
    assert chrono.__str__() == f"{0:.{ROUNDING_PRECISION}f}"
    assert not chrono.is_running


def test_start_chrono(new_chrono):
    new_chrono.start()
    assert new_chrono.start_time
    assert new_chrono.is_running


def test_start_chrono_already_started(started_chrono):
    with pytest.raises(StartError):
        started_chrono.start()


def test_stop_chrono(started_chrono):
    sleep(PAUSE)
    started_chrono.stop()
    assert started_chrono.stop_time > started_chrono.start_time
    assert started_chrono.value == pytest.approx(PAUSE, abs=TOLERANCE)
    assert not started_chrono.is_running


def test_stop_chrono_already_stopped(started_and_stopped_chrono):
    with pytest.raises(StopError):
        started_and_stopped_chrono.stop()


def test_reset_chrono_stopped(started_and_stopped_chrono):
    started_and_stopped_chrono.reset()
    assert started_and_stopped_chrono.value == .0


def test_reset_chrono_started(started_chrono):
    with pytest.raises(ResetWhileRunningError):
        started_chrono.reset()


def test_reset_chrono_already_at_0(new_chrono):
    with pytest.raises(ResetAlreadyAtZeroError):
        new_chrono.reset()


def test_toggle_new_chrono(new_chrono):
    new_chrono.toggle()
    assert new_chrono.start_time
    assert new_chrono.is_running


def test_toggle_started_chrono(started_chrono):
    sleep(PAUSE)
    started_chrono.toggle()
    assert started_chrono.stop_time > started_chrono.start_time
    assert not started_chrono.is_running


def test_toggle_started_and_stopped_chrono(started_and_stopped_chrono):
    sleep(PAUSE)
    started_and_stopped_chrono.toggle()
    assert started_and_stopped_chrono.start_time > started_and_stopped_chrono.stop_time
    assert started_and_stopped_chrono.is_running
