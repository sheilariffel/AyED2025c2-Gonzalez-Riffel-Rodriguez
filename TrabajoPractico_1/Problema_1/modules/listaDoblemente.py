# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código
# -*- coding: utf-8 -*-
# modulos.py

class Nodo:
    __inicio__ = ("dato", "siguiente", "anterior")

    def __init__(self, dato, siguiente=None, anterior=None):
        self.dato = dato
        self.siguiente = siguiente
        self.anterior = anterior


class ListaDobleEnlazada:
    __inicio__ = ("cabeza", "cola", "tamanio")

    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamanio = 0

    # ---------------- Métodos principales ----------------

    def esta_vacia(self):
        return self.tamanio == 0

    def _nodo_en_posicion(self, posicion: int):
        """Devuelve el nodo en 'posicion'. Lanza excepción si no existe."""
        if posicion < 0 or posicion >= self.tamanio:
            raise Exception("Posición inválida")
        if posicion <= self.tamanio // 2:
            actual = self.cabeza
            for _ in range(posicion):
                actual = actual.siguiente
            return actual
        else:
            actual = self.cola
            for _ in range(self.tamanio - 1 - posicion):
                actual = actual.anterior
            return actual

    def agregar_al_inicio(self, item):
        nuevo = Nodo(item, siguiente=self.cabeza, anterior=None)
        if self.cabeza is not None:
            self.cabeza.anterior = nuevo
        self.cabeza = nuevo
        if self.cola is None:  # lista vacía
            self.cola = nuevo
        self.tamanio += 1

    def agregar_al_final(self, item):
        nuevo = Nodo(item, siguiente=None, anterior=self.cola)
        if self.cola is not None:
            self.cola.siguiente = nuevo
        self.cola = nuevo
        if self.cabeza is None:  # lista vacía
            self.cabeza = nuevo
        self.tamanio += 1

    def insertar(self, item, posicion=None):
        if posicion is None:
            self.agregar_al_final(item)
            return

        if self.tamanio == 0 and posicion != 0:
            raise Exception("Posición inválida")

        if posicion < 0 or posicion >= self.tamanio:
            if not (self.tamanio == 0 and posicion == 0):
                raise Exception("Posición inválida")

        if posicion == 0:
            self.agregar_al_inicio(item)
            return

        actual = self._nodo_en_posicion(posicion)
        nuevo = Nodo(item, siguiente=actual, anterior=actual.anterior)
        actual.anterior.siguiente = nuevo
        actual.anterior = nuevo
        self.tamanio += 1

    def extraer(self, posicion=None):
        if self.esta_vacia():
            raise Exception("Lista vacía")

        if posicion is None or posicion == -1:
            nodo = self.cola
            dato = nodo.dato
            self.cola = nodo.anterior
            if self.cola is not None:
                self.cola.siguiente = None
            else:
                self.cabeza = None
            self.tamanio -= 1
            return dato

        if posicion < 0 or posicion >= self.tamanio:
            raise Exception("Posición inválida")

        if posicion == 0:
            nodo = self.cabeza
            dato = nodo.dato
            self.cabeza = nodo.siguiente
            if self.cabeza is not None:
                self.cabeza.anterior = None
            else:
                self.cola = None
            self.tamanio -= 1
            return dato

        actual = self._nodo_en_posicion(posicion)
        dato = actual.dato
        ant = actual.anterior
        sig = actual.siguiente
        ant.siguiente = sig
        if sig is not None:
            sig.anterior = ant
        else:
            self.cola = ant
        self.tamanio -= 1
        return dato

    def copiar(self):
        copia = ListaDobleEnlazada()
        actual = self.cabeza
        while actual is not None:
            copia.agregar_al_final(actual.dato)
            actual = actual.siguiente
        return copia

    def invertir(self):
        actual = self.cabeza
        while actual is not None:
            actual.siguiente, actual.anterior = actual.anterior, actual.siguiente
            actual = actual.anterior
        self.cabeza, self.cola = self.cola, self.cabeza

    def concatenar(self, otra_lista):
        actual = otra_lista.cabeza
        while actual is not None:
            self.agregar_al_final(actual.dato)
            actual = actual.siguiente
        return self

    def __len__(self):
        return self.tamanio

    def __add__(self, otra_lista):
        nueva = self.copiar()
        nueva.concatenar(otra_lista)
        return nueva

    def __iter__(self):
        actual = self.cabeza
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente
