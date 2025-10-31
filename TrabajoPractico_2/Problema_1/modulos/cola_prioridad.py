
# cola_prioridad.py mejorada con el segundo criterio
from modulos.monticulobinario import MonticuloBinario

class ColaDePrioridad:
    def __init__(self):
        self.monticulo = MonticuloBinario()  # El montículo es la estructura que mantiene todo ordenado automáticamente
        
        # Contador para manejar el orden de llegada
        # Útil cuando dos elementos tienen la misma prioridad
        self.contador_llegadas = 0  # Este el contador se usa para considerar el segundo criterio de criticidad. De esa manera si hay dos con el mismo riesgo, se atiende el que llegó primero (contador simula el orden de llegada)
    
    def insertar(self, prioridad, dato):
        """
        Inserta un elemento en la cola junto con su prioridad.
        
        Cuanto más chica sea la prioridad, más importante es el elemento.
        Si dos elementos tienen la misma prioridad, se utiliza el orden de llegada
        para decidir cuál se debe obtener primero.
        """
        # En el contexto de nuestro problema, cada vez que llega un paciente, aumentamos el contador.
        # Esto permite saber quién llegó antes.
 
        self.contador_llegadas += 1     #Es el número de inserción de este paciente, que simula su orden de llegada.
        
        # La tupla incluye prioridad y orden para desempatar quien se atiende primero
        """
        El montículo se fija de que si hay dos prioridades iguales, analiza la segunda variable del contador
        Por lo tanto se realiza el siguiente procedimeinto 
        - Guardamos en el montículo una tupla: (prioridad, orden_de_llegada, paciente)
        - El montículo compara primero por prioridad.
        - Si dos prioridades son iguales, compara por elf.contador_llegadas
        - Resultado: si dos pacientes tienen mismo riesgo, se atiende primero al que llegó antes.
        """
        self.monticulo.insertar( (prioridad, self.contador_llegadas, dato) )

    def eliminar(self):
        
        #Elimina el elemento con menor prioridad y lo saca de la cola. Es el paciente que será atendido
               
        return self.monticulo.eliminarMin()

    def esta_vacia(self):
        return self.monticulo.tamanoActual == 0 # Devuelve True si no quedan pacientes.

    def ver_minimo(self):
        if self.monticulo.tamanoActual >= 1: # Devuelve el paciente más urgente sin sacarlo.
            return self.monticulo.listaMonticulo[1]
        else:
            return None

