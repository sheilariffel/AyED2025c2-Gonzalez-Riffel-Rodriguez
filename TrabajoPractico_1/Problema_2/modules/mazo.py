# mazo.py

from modules.LDE import ListaDobleEnlazada  # Importa la clase ListaDobleEnlazada

class DequeEmptyError(Exception):
    pass  # Define una excepción personalizada para cuando el mazo está vacío

class Mazo:
    def __init__(self):
        self._cartas = ListaDobleEnlazada() #mazo vacío

    def esta_vacio(self):
        return self._cartas.esta_vacia() #devuelve True si el mazo está vacío

    def agregar_carta(self, carta):
        self._cartas.agregar_al_final(carta) #agrega una carta al final del mazo

    def sacar_carta(self):
        if self.esta_vacio():
            raise DequeEmptyError("El mazo está vacío")
        return self._cartas.extraer(0) #saca y devuelve la primera carta del mazo

    def __len__(self):
        return len(self._cartas) #devuelve la cantidad de cartas en el mazo

    def __iter__(self):
        return iter(self._cartas) #permite iterar sobre las cartas del mazo