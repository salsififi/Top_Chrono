"""Contient la classe Chrono"""
from time import time

from chrono.constants import ROUNDING_PRECISION
from chrono.models.exceptions import StartError, StopError, ResetWhileRunningError, ResetAlreadyAtZeroError


class Chrono:
    """Classe pour créer des chronomètres."""

    def __init__(self) -> None:
        self.start_time: float | None = None
        self.stop_time: float | None = None
        self.value: float = .0  # Durée affichée sur le chronomètre
        self.is_running: bool = False

    def __str__(self) -> str:
        return f"{self.value:.{ROUNDING_PRECISION}f}"

    @property
    def duration(self) -> float:
        """Temps écoulé entre un start le stop suivant"""
        return self.stop_time - self.start_time

    def start(self) -> None:
        """
        Démarre le chronomètre.
        Si le chronomètre tournait déjà, lève une exception AlreadyStartedError.
        """
        if self.is_running:
            raise StartError()
        self.start_time = time()
        self.is_running = True

    def stop(self) -> None:
        """
        Arrête le chronomètre.
        Si le chronomètre était déjà à l'arrêt, lève une exception AlreadyStoppedError.
        """
        if not self.is_running:
            raise StopError()
        self.stop_time = time()
        self.is_running = False
        self.value = round(self.value + self.duration, ROUNDING_PRECISION)

    def reset(self) -> None:
        """Remet le chronomètre à zéro."""
        if self.is_running:
            raise ResetWhileRunningError()
        if self.value == 0:
            raise ResetAlreadyAtZeroError()
        self.value = .0

    def toggle(self) -> None:
        """Bascule de start à stop et inversement."""
        if self.is_running:
            self.stop()
        else:
            self.start()
