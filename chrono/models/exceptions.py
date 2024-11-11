"""Exceptions liées à l'utilisation des instances de la classe Chrono."""


class StartError(Exception):
    """Chronomètre déjà en train de tourner."""
    def __init__(self):
        super().__init__("Le chronomètre est déjà démarré.")


class StopError(Exception):
    """Chronomètre déjà à l'arrêt."""
    def __init__(self):
        super().__init__("Le chronomètre est déjà à l'arrêt.")


class ResetWhileRunningError(Exception):
    """Chronomètre en train de tourner."""
    def __init__(self):
        super().__init__("Le chronomètre doit d'abord être arrêté avant d'être remis à zéro...")


class ResetAlreadyAtZeroError(Exception):
    """Chronomètre déjà à zéro."""
    def __init__(self):
        super().__init__("Le chronomètre est déjà à zéro !")



