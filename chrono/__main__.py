"""
"TOP CHRONO"
Un chronomètre en ligne de commande
Auteur : Simon Salvaing
Date : 2024-11-11

Point d'entrée
"""
from chrono.models.chrono import Chrono
from chrono.controllers.cli_controller import CliController


def main():
    """Boucle principale du programme."""
    chrono = Chrono()
    controller = CliController(chrono)
    controller.run()


if __name__ == '__main__':
    main()
