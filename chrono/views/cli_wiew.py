"""Vue pour l'utilisation en ligne de commandes."""

from typer import style
from typer.colors import YELLOW, BLUE, GREEN, RED

from chrono.constants import ROUNDING_PRECISION, LINE_LENGTH, TOGGLE_CHRONO_KEY, RESET_CHRONO_KEY, EXIT_KEY
from chrono.views.base_view import BaseView


class CliView(BaseView):
    """Pour créer la vue en ligne de commandes."""

    class Messages:
        EXIT = "À bientôt !"
        KEYS = (f"'{style(TOGGLE_CHRONO_KEY, fg=RED)}' pour démarrer ou arrêter le chrono, "
                f"'{style(RESET_CHRONO_KEY, fg=RED)}' pour le remettre à zéro.\n"
                f"Pour quitter le programme, appuyez sur '{style(EXIT_KEY, fg=RED)}'.")
        LAUNCH = f"{style(' TOP CHRONO '.center(LINE_LENGTH, "*"), fg=RED)}"
        RESET = f"{style('On recommence !', fg=GREEN)}"
        START = f"{style('GO !', fg=YELLOW)} ('{style(TOGGLE_CHRONO_KEY, fg=RED)}' pour arrêter le chrono.)"
        STOP = f"{style('STOP !', fg=BLUE)}"
        TIMELAPSE = "Le chrono affiche: {chrono_value}"

    def exit_view(self) -> None:
        """Vue quand le chronomètre est stoppé."""
        print(self.Messages.EXIT)

    def welcome_view(self) -> None:
        """Vue de lancement du programme."""
        print(self.Messages.LAUNCH)
        print(self.Messages.KEYS)
        print()

    def reset_view(self) -> None:
        """Vue à la réinitialisation du chronomètre."""
        print(self.Messages.RESET)
        print(self.Messages.TIMELAPSE.format(chrono_value=f"{0:.{ROUNDING_PRECISION}f}"))

    def run_view(self) -> None:
        """Vue au lancement du programme."""
        print(self.Messages.LAUNCH)
        print(self.Messages.KEYS)
        print()

    def start_chrono_view(self) -> None:
        """Vue quand le chronomètre est lancé."""
        print(self.Messages.START)

    def stop_chrono_view(self) -> None:
        """Vue quand le chronomètre est stoppé."""
        print(self.Messages.STOP)
        print(self.Messages.TIMELAPSE.format(chrono_value=f"{self.chrono.value:.{ROUNDING_PRECISION}f}"))
