
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
        """
        self.contador_llegadas += 1     #self.contador_llegadas es el número de inserción de este paciente, que simula su orden de llegada.
        
        # La tupla incluye prioridad y orden para desempatar
        """
        Acá es donde sucede la magia de que llama al montículo y se fija de que si hay dos prioridades
        iguales, analiza la segunda variable del contador
        """
        self.monticulo.insertar( (prioridad, self.contador_llegadas, dato) )

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

