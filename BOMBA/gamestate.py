"""Modulo de los estados del juego."""

from tablero import Tablero


class GameState:
    """Esta clase representa todos los estados que puede tomar el juego."""

    def __init__(self, tablero: "Tablero") -> None:
        self._tablero = tablero
        self._drawcount = 0
        self._winnercombinations = []

    def checkwin(self):
        """Esta funcion decide si la partida la gana algun jugador o queda en empate"""
        
        if not self._winnercombinations:
            for i in range(self._tablero.dimension):
                rows = [i * self._tablero.dimension + j +
                        1 for j in range(self._tablero.dimension)]
                self._winnercombinations.append(rows)

            for j in range(self._tablero.dimension):
                columns = [i * self._tablero.dimension + j +
                        1 for i in range(self._tablero.dimension)]
                self._winnercombinations.append(columns)

            diagonalone = [i * self._tablero.dimension +
                        i + 1 for i in range(self._tablero.dimension)]
            self._winnercombinations.append(diagonalone)

            diagonaltwo = [(i + 1) * self._tablero.dimension -
                        i for i in range(self._tablero.dimension)]
            self._winnercombinations.append(diagonaltwo)

        for combination in self._winnercombinations:
            gridkeys = [self._tablero.grid.get(
                str(position))for position in combination]
            if gridkeys[0] != 0 and gridkeys.count(gridkeys[0]) == self._tablero.dimension:
                return "X" if gridkeys[0] == 1 else "O"

        self._drawcount += 1
        if self._drawcount == self._tablero.dimension**2:
            return "Empate"
        return None
