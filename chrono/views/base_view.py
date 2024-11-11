"""Contient la classe abstraite BaseView."""

from abc import ABC, abstractmethod

from chrono.models.chrono import Chrono


class BaseView(ABC):
    """Vue de base abstraite"""

    def __init__(self, chrono: Chrono) -> None:
        self.chrono = chrono

    @abstractmethod
    def exit_view(self) -> None:
        """Vue de sortie du programme."""

    @abstractmethod
    def welcome_view(self) -> None:
        """Vue de lancement du programme."""

    @abstractmethod
    def reset_view(self) -> None:
        """Vue à la réinitialisation du chronomètre."""

    @abstractmethod
    def run_view(self) -> None:
        """Vue au lancement du programme."""

    @abstractmethod
    def start_chrono_view(self) -> None:
        """Vue quand le chronomètre est lancé."""

    @abstractmethod
    def stop_chrono_view(self) -> None:
        """Vue quand le chronomètre est stoppé."""
