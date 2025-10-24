
# cola_prioridad.py mejorada con el segundo criterio
from modulos.monticulobinario import MonticuloBinario

class ColaDePrioridad:
    def __init__(self):
        self.monticulo = MonticuloBinario()
        self.contador_llegadas = 0  # contador para desempatar según orden de llegada

    def insertar(self, prioridad, dato):
        """
        Inserta un elemento con prioridad y orden de llegada.
        prioridad: cuanto más chico, más urgente
        dato: cualquier tipo de dato (por ejemplo, un paciente)
        """
        self.contador_llegadas += 1
        # La tupla incluye prioridad y orden para desempatar
        self.monticulo.insertar((prioridad, self.contador_llegadas, dato))

    def eliminar(self):
        """
        Elimina y devuelve el elemento con mayor prioridad (la tupla completa).
        """
        return self.monticulo.eliminarMin()

    def esta_vacia(self):
        return self.monticulo.tamanoActual == 0

    def ver_minimo(self):
        if self.monticulo.tamanoActual >= 1:
            return self.monticulo.listaMonticulo[1]
        else:
            return None





"""
#ni idea que es lo anterior pero ahora agrego esto 
# cola_prioridad.py
from modulos.monticulobinario import MonticuloBinario

class ColaDePrioridad:
    def __init__(self):
        # Internamente usa un montículo de mínima
        self.monticulo = MonticuloBinario()

    def insertar(self, prioridad, dato):
        
        #Inserta un elemento en la cola de prioridad.
        #prioridad: número (cuanto más chico, más urgente)
        #dato: cualquier tipo de dato (por ejemplo, un paciente)
        
        # En el montículo se almacenan tuplas (prioridad, dato)
        self.monticulo.insertar((prioridad, dato))

    def eliminar(self):
        
        #Elimina y devuelve el elemento con mayor prioridad (la tupla completa).
        
        return self.monticulo.eliminarMin()

    def esta_vacia(self):
        
        #Devuelve True si no hay elementos en la cola.
        
        return self.monticulo.tamanoActual == 0

    def ver_minimo(self):
        
        #Devuelve (sin eliminar) el elemento con mayor prioridad (el mínimo).
        
        if self.monticulo.tamanoActual >= 1:
            return self.monticulo.listaMonticulo[1]
        else:
            return None
#Agregado por mi, para poder realizar una cola de prioridad. Que permite insetar elmentos con prioridad asociada

import heapq

class PriorityQueue:
    def __init__(self):
        self._heap = []
        self._count = 0

    def push(self, prioridad, item):
        # prioridad menor = más urgente
        heapq.heappush(self._heap, (prioridad, self._count, item))
        self._count += 1

    def pop(self):
        if not self._heap:
            return None
        return heapq.heappop(self._heap)[2]

    def peek(self):
        if not self._heap:
            return None
        return self._heap[0][2]

    def __len__(self):
        return len(self._heap)

#...
# Supongamos que internamente hay una instancia global (o contexto) de la cola
_cola = PriorityQueue()

#Luego, funciones que probablemente los tests esperan:

def reiniciar():
    Reinicia la estructura (vaciar) para los tests.
    global _cola
    _cola = PriorityQueue()

def inserta_paciente(paciente, riesgo):
    
    Inserta un nuevo paciente con su nivel de riesgo.
    paciente: puede ser cualquier identificador (nombre, objeto, etc.)
    riesgo: entero 1, 2, 3 (1 = más urgencia)
    
    _cola.push(riesgo, paciente)

def atender_paciente():
    
    Extrae y devuelve el paciente de mayor prioridad (más urgente) restante.
    Si no hay pacientes, retorna None (o lo que el test espera).
    
    return _cola.pop()

def proximo_paciente():
    
    Devuelve el paciente que sería atendido a continuación sin extraerlo.
    
    return _cola.peek()

def pacientes_pendientes():
    
    Devuelve la cantidad de pacientes que restan por atender (para tests de longitud).
    
    return len(_cola)
#....

#Me pidieron definir una clase paciente _> hay una en el modulo

class Paciente:
    def __init__(self, nombre, riesgo):
        self.nombre = nombre
        self.riesgo = riesgo

    def __repr__(self):
        return f"{self.nombre} (riesgo {self.riesgo})"

#simulamos el flujo 
# Ejemplo de uso
cola = PriorityQueue()

#simulamos el flujo 
cola.push(3, Paciente("Juan", 3))   # bajo
cola.push(1, Paciente("Ana", 1))    # crítico
cola.push(2, Paciente("Luis", 2))   # moderado
cola.push(1, Paciente("Marta", 1))  # crítico, llegó después de Ana

print("Atención de pacientes:")
while len(cola) > 0:
    print("->", cola.pop())

"""
