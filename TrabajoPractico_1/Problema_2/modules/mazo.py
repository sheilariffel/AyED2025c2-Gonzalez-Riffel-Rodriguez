# mazo.py

from modules.LDE import ListaDobleEnlazada  # Importa la clase ListaDobleEnlazada

class DequeEmptyError(Exception):
    """Excepción personalizada para cuando el mazo está vacío"""
    pass


class Mazo:
    def __init__(self):
        self._cartas = ListaDobleEnlazada()  # mazo vacío

    def esta_vacio(self):
        return self._cartas.esta_vacia()

    def poner_carta_arriba(self, carta):
        """Agrega una carta arriba del mazo (al inicio)."""
        self._cartas.agregar_al_inicio(carta)

    def poner_carta_abajo(self, carta):
        """Agrega una carta abajo del mazo (al final)."""
        self._cartas.agregar_al_final(carta)

    def sacar_carta_arriba(self, mostrar=False):
        """Saca la carta de arriba del mazo (inicio)."""
        if self.esta_vacio():
            raise DequeEmptyError("El mazo está vacío")
        return self._cartas.extraer(0)

    def __len__(self):
        """Permite usar len(mazo)."""
        return len(self._cartas)

    def __iter__(self):
        """Permite iterar sobre las cartas del mazo."""
        return iter(self._cartas)

    def __str__(self):
        """Representación del mazo al imprimirlo."""
        return " ".join(str(carta) for carta in self._cartas)
