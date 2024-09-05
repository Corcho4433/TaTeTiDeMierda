"""Modulo de los jugadores del juego."""


class Player:
    """Esta clase representa a los jugadores del juego."""

    def __init__(self) -> None:
        self._tipo = 1

    def changetipo(self):
        """Cambia el jugador."""
        if self._tipo == 1:
            self._tipo = 2
        else:
            self._tipo = 1

    def inputficha(self):
        """Se encarga de pedir que ficha se quiere ingresar."""
        inputusr = int(
            input(f"Coloque la posicion en la que quiere colocar su ficha ({str(self)}): "))
        return inputusr

    @property
    def tipo(self):
        """Se encarga de devolver el tipo de jugador."""
        return self._tipo

    def __str__(self):
        if self._tipo == 1:
            return "X"
        return "O"
