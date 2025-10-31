# ===========================
#  MÓDULO: avl.py
# ===========================
from datetime import datetime

class NodoAVL:
    def __init__(self, clave, valor):
        self.clave = clave
        self.valor = valor
        self.altura = 1
        self.izq = None
        self.der = None


class ArbolAVL:
    def __init__(self):
        self.raiz = None

    # Obtener altura
    def _altura(self, nodo):
        return nodo.altura if nodo else 0
    
    def _actualizar_altura(self, nodo):
        nodo.altura = 1 + max(self._altura(nodo.izq), self._altura(nodo.der))

    # Obtener balance
    def _balance(self, nodo):
        return self._altura(nodo.izq) - self._altura(nodo.der) if nodo else 0

    # Rotación derecha
    def _rotar_derecha(self, y):
        x, T2 = y.izq, y.izq.der
        x.der, y.izq = y, T2
        self._actualizar_altura(y)
        self._actualizar_altura(x)
        return x

    # Rotación izquierda
    def _rotar_izquierda(self, x):
        y, T2 = x.der, x.der.izq
        y.izq, x.der = x, T2
        self._actualizar_altura(x)
        self._actualizar_altura(y)
        return y

    # Insertar nodo
    def _insertar(self, nodo, clave, valor):
        if not nodo:
            return NodoAVL(clave, valor)
        if clave < nodo.clave:
            nodo.izq = self._insertar(nodo.izq, clave, valor)
        elif clave > nodo.clave:
            nodo.der = self._insertar(nodo.der, clave, valor)
        else:
            nodo.valor = valor
            return nodo

        nodo.altura = 1 + max(self._altura(nodo.izq), self._altura(nodo.der))
        balance = self._balance(nodo)

        # Balancear
        if balance > 1 and clave < nodo.izq.clave:
            return self._rotar_derecha(nodo)
        if balance < -1 and clave > nodo.der.clave:
            return self._rotar_izquierda(nodo)
        if balance > 1 and clave > nodo.izq.clave:
            nodo.izq = self._rotar_izquierda(nodo.izq)
            return self._rotar_derecha(nodo)
        if balance < -1 and clave < nodo.der.clave:
            nodo.der = self._rotar_derecha(nodo.der)
            return self._rotar_izquierda(nodo)

        return nodo

    def insertar(self, clave, valor):
        self.raiz = self._insertar(self.raiz, clave, valor)

    # Buscar por clave
    def _buscar(self, nodo, clave):
        if not nodo:
            return None
        if clave == nodo.clave:
            return nodo.valor
        elif clave < nodo.clave:
            return self._buscar(nodo.izq, clave)
        else:
            return self._buscar(nodo.der, clave)

    def buscar(self, clave):
        return self._buscar(self.raiz, clave)

    # Eliminar nodo
    def _min_nodo(self, nodo):
        while nodo.izq:
            nodo = nodo.izq
        return nodo

    def _eliminar(self, nodo, clave):
        if not nodo:
            return nodo
        if clave < nodo.clave:
            nodo.izq = self._eliminar(nodo.izq, clave)
        elif clave > nodo.clave:
            nodo.der = self._eliminar(nodo.der, clave)
        else:
            if not nodo.izq:
                return nodo.der
            elif not nodo.der:
                return nodo.izq
            temp = self._min_nodo(nodo.der)
            nodo.clave, nodo.valor = temp.clave, temp.valor
            nodo.der = self._eliminar(nodo.der, temp.clave)

        nodo.altura = 1 + max(self._altura(nodo.izq), self._altura(nodo.der))
        balance = self._balance(nodo)

        # Rebalancear
        if balance > 1 and self._balance(nodo.izq) >= 0:
            return self._rotar_derecha(nodo)
        if balance > 1 and self._balance(nodo.izq) < 0:
            nodo.izq = self._rotar_izquierda(nodo.izq)
            return self._rotar_derecha(nodo)
        if balance < -1 and self._balance(nodo.der) <= 0:
            return self._rotar_izquierda(nodo)
        if balance < -1 and self._balance(nodo.der) > 0:
            nodo.der = self._rotar_derecha(nodo.der)
            return self._rotar_izquierda(nodo)

        return nodo

    def eliminar(self, clave):
        self.raiz = self._eliminar(self.raiz, clave)

    # Recorrido en orden (clave, valor)
    def _inorden(self, nodo, lista):
        if nodo:
            self._inorden(nodo.izq, lista)
            lista.append((nodo.clave, nodo.valor))
            self._inorden(nodo.der, lista)

    def obtener_todos(self):
        lista = []
        self._inorden(self.raiz, lista)
        return lista
