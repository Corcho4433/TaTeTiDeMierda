import unittest
import unittest.test
from unittest.mock import patch

from gamestate import GameState
from player import Player
from tablero import Tablero

class TestTablero(unittest.TestCase):
    def test_01_tablero_spawnea_correctamente_indexando_desde_1_a_dimension(self):
        tablero = Tablero(3)
        tablero.spawngrid()
        self.assertEqual({"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0}, tablero.grid)

    @patch('builtins.input', return_value='1')
    def test_02_tablero_guarda_valores_segun_jugador_X(self, mock_input):
        jugador = Player()
        tablero = Tablero(3)
        tablero.spawngrid()
        ficha = jugador.inputficha()
        tablero.grid[str(ficha)] = jugador.tipo
        self.assertEqual({"1": 1, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0}, tablero.grid)

    @patch('builtins.input', return_value='1')
    def test_03_tablero_guarda_valores_segun_jugador_O(self, mock_input):
        jugador = Player()
        jugador.changetipo()
        tablero = Tablero(3)
        tablero.spawngrid()
        ficha = jugador.inputficha()
        tablero.grid[str(ficha)] = jugador.tipo
        self.assertEqual({"1": 2, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0}, tablero.grid)

class TestPlayer(unittest.TestCase):
    def test_01_el_primer_jugador_es_siempre_X(self):
        jugador = Player()
        self.assertEqual("X", str(jugador))

    def test_02_cambiar_tipo_de_jugador_cambia_la_ficha_O(self):
        jugador = Player()
        jugador.changetipo()
        self.assertEqual("O", str(jugador))

    @patch('builtins.input', return_value='1')
    def test_03_input_jugador_devuelve_posicion_para_ingresar_ficha(self, mock_input):
        jugador = Player()
        ficha = jugador.inputficha()
        self.assertEqual(1, ficha)
    

class TestGameState(unittest.TestCase):
    def test_01_winnercombinations_devuelve_todas_las_posiciones_ganadoras(self):
        tablero = Tablero(3)
        state = GameState(tablero)
        state.checkwin()
        self.assertEqual([[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]], state._winnercombinations)

    def test_02_winnercombinations_devuelve_todas_las_posiciones_ganadoras_con_dimension_modificada(self):
        tablero = Tablero(4)
        state = GameState(tablero)
        state.checkwin()
        self.assertEqual([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16], [1, 6, 11, 16], [4, 7, 10, 
13]], state._winnercombinations)
        
if __name__ == "__main__":
    unittest.main()