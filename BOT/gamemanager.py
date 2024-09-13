"""Modulo que maneja el desarrollo del juego."""

from tablero import Tablero
from player import Player
from display import Display
from gamestate import GameState
import random

class GameManager:
    """Clase que maneja el loop del juego."""

    def __init__(self, tablero: "Tablero") -> None:
        self._jugador = Player()
        self._tablero = tablero
        self._display = Display(tablero)
        self._state = GameState(tablero)

    #MODIFICADO
    def gameloop(self):
        """Se encarga de definir el loop del juego y de tomar las decisiones pertinentes."""
        self._tablero.spawngrid()
        winner = False
        while not winner:
            ficha = 0
            while ficha > self._tablero.dimension**2 or ficha < 1:
                try:
                    self._display.displaytablero()
                    if self._jugador.tipo == 1:
                        ficha = self._jugador.inputficha()
                    else:
                        ficha_valida = []
                        for i in self._tablero.grid:
                            if self._tablero.grid.get(i) not in [1,2]:
                                ficha_valida.append(i)
                        ficha = int(random.choice(ficha_valida))
                    if str(ficha) not in self._tablero.grid:
                        raise KeyError
                except KeyError:
                    print("Posicion fuera de rango")
                    ficha = 0
                except ValueError:
                    print("Ficha invalida")
                    ficha = 0

                if ficha == 0:
                    continue

            if self._tablero.grid[str(ficha)] == 0:
                self._tablero.grid[str(ficha)] = self._jugador.tipo
            else:
                print("No podes colocar tu ficha aca!")
                continue

            winner = self._state.checkwin()
            if winner in ["X", "O"]:
                self._display.displaytablero()
                print(f"Gana el jugador {winner}!")
                break
            if winner == "Empate":
                print(f"{winner}!")
                break

            self._jugador.changetipo()
