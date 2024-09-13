"""Modulo de ejecucion del juego."""

from gamemanager import GameManager
from tablero import Tablero

if __name__ == "__main__":
    DIMENSION = None
    while not isinstance(DIMENSION, int) or DIMENSION <= 0:
        try:
            DIMENSION = int(
                input("De que Dimension quieres tu tablero? (3x3, 4x4, etc): "))
            if DIMENSION <= 0:
                print("La Dimension debe ser positiva")
        except ValueError:
            print("Dimension invalida")

    GAME = GameManager(Tablero(DIMENSION))
    GAME.gameloop()
