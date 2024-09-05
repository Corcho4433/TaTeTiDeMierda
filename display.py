"""Modulo del Display del juego."""

from tablero import Tablero


class Display:
    """Clase que se encarga de mostrar los elementos en la terminal de forma visual."""

    def __init__(self, tablero: "Tablero") -> None:
        self._tablero = tablero

    def displaytablero(self):
        """Este metodo se encarga de mostrar correctamente el tablero. 
        Incluye fichas y espacios vacios."""
        for i in range(self._tablero.dimension):
            for j in range(self._tablero.dimension):
                indice = i * self._tablero.dimension + j + 1
                if self._tablero.grid[str(indice)] == 1:
                    print("[X] ", end="")
                elif self._tablero.grid[str(indice)] == 2:
                    print("[O] ", end="")
                else:
                    print("[ ] ", end="")
            print("\n")
