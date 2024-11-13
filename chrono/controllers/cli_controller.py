"""Contient la classe CliController"""
import sys
from typing import NoReturn

import keyboard

from chrono.constants import TOGGLE_CHRONO_KEY, RESET_CHRONO_KEY, EXIT_KEY
from chrono.models.chrono import Chrono
from chrono.models.exceptions import StartError, StopError, ResetWhileRunningError, ResetAlreadyAtZeroError
from chrono.views.cli_view import CliView


class CliController:
    """
    Crée un contrôleur basé sur un keyboard listener
    pour l'interface en ligne de commandes.
    """

    def __init__(self, chrono: Chrono) -> None:
        """Par défaut, le KeyboardListener est actif"""
        self.chrono = chrono
        self.view = CliView()
        self.is_running = True

    def press_toggle_key(self) -> None:
        """Le chronomètre bascule de start à stop, ou inversement."""
        try:
            self.chrono.toggle()
            if self.chrono.is_running:
                self.view.start_chrono_view()
            else:
                self.view.stop_chrono_view(self.chrono.value)
        except StartError as e:
            print(e)
        except StopError as e:
            print(e)

    def press_reset_key(self) -> None:
        """Le chronomètre est réinitialisé."""
        try:
            self.chrono.reset()
            self.view.reset_view()
        except ResetWhileRunningError as e:
            print(e)
        except ResetAlreadyAtZeroError as e:
            print(e)

    def on_key_event(self, event: keyboard.KeyboardEvent) -> None:
        """Exécute les actions en fonction des touches"""
        if event.event_type == "down":
            event.name = event.name.upper()
            if event.name == TOGGLE_CHRONO_KEY:
                self.press_toggle_key()
            elif event.name == RESET_CHRONO_KEY:
                self.press_reset_key()
            elif event.name == EXIT_KEY:
                self.is_running = False

    def run(self) -> NoReturn:
        """Exécute le contrôleur"""
        self.view.welcome_view()
        keyboard.hook(self.on_key_event, suppress=True)
        while self.is_running:
            pass
        self.view.exit_view()
        sys.exit()
