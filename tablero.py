"""Modulo del tablero del juego."""


class Tablero:
    """Esta clase representa el tablero del TicTacToe."""

    def __init__(self, dimension: int) -> None:
        self._dimension = dimension
        self._grid: dict = {}

    def spawngrid(self):
        """Genera la grid vacia con sus posiciones desde el 1 hasta la dimension."""
        for i in range(self._dimension ** 2):
            self._grid.update({str(i + 1): 0})

    @property
    def grid(self):
        """Devuelve el diccionario del tablero."""
        return self._grid

    @property
    def dimension(self):
        """Devuelve la dimension del tablero."""
        return self._dimension
