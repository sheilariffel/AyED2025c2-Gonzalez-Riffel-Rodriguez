
class MonticuloBinario:
    def __init__(self):
        # Se crea una lista que representará el montículo.
        # El índice 0 NO se usa (se deja un 0 "falso" al inicio)
        # Esto facilita los cálculos de padres e hijos: 
        #   - hijo izquierdo = i*2
        #   - hijo derecho = i*2 + 1
        self.listaMonticulo = [0]        
        # Lleva la cuenta del número actual de elementos válidos en el montículo.
        self.tamanoActual = 0

# Una vez que se añade un nuevo ítem al árbol (al final de su lista), infiltArriba se hace cargo y posiciona el nuevo ítem apropiadamente.
# Este método “filtra hacia arriba” un nuevo elemento hasta que quede en la posición correcta dentro del montículo.
    def infiltArriba(self, i):
        # Mientras el nodo tenga un padre (i // 2 > 0)
        while i // 2 > 0:
            # Si el valor actual es menor que su padre,
            # significa que está "fuera de lugar" (no cumple con la propiedade del montículo de mínima)
            
            """ Contexto de nuestro problema: acá es donde mi montículo primero recibe la prioridad del paciente. Una vez que campara ese valor
        pasa al orden de llegada y luego a los datos del paciente. Es por eso que pasa primero el de riesgo menor que seria el 1. Siempre me devuelve la raiz
        """
            if self.listaMonticulo[i] < self.listaMonticulo[i // 2]: #compara la tupla (prioridad, contador_llegada, paciente)
                # Intercambia los valores (sube el valor más chico)
                tmp = self.listaMonticulo[i // 2]
                self.listaMonticulo[i // 2] = self.listaMonticulo[i]
                self.listaMonticulo[i] = tmp
            # Actualiza el índice: sube al padre y sigue comparando hacia arriba
            i = i // 2

#Inserta un elemento al final y luego lo “sube” hasta que se cumpla la propiedad del montículo (padres ≤ hijos).
    def insertar(self, k):
        # Agrega el nuevo elemento al final de la lista (al final del montículo)
        self.listaMonticulo.append(k)
        
        # Aumenta el contador de elementos
        self.tamanoActual = self.tamanoActual + 1
        
        # Llama a infiltArriba para reposicionar el nuevo elemento
        # si es necesario (asegura que el mínimo quede en la raíz)
        self.infiltArriba(self.tamanoActual)

#Este método “filtra hacia abajo” el elemento en posición i hasta que quede en el lugar correcto (propiedad del montículo restablecida).
    def infiltAbajo(self, i):
        # Mientras el nodo tenga al menos un hijo izquierdo
        while (i * 2) <= self.tamanoActual:
            # Obtiene el índice del hijo con el valor más chico
            hm = self.hijoMin(i)
            # Si el valor actual es mayor que su hijo menor, hay que intercambiar
            if self.listaMonticulo[i] > self.listaMonticulo[hm]:
                tmp = self.listaMonticulo[i]
                self.listaMonticulo[i] = self.listaMonticulo[hm]
                self.listaMonticulo[hm] = tmp
            # Actualiza el índice: baja al hijo con el que se intercambió
            i = hm

#Devuelve el índice del hijo con menor valor, para saber con cuál intercambiar al bajar un nodo.
    def hijoMin(self, i):
        # Si solo tiene un hijo izquierdo (no hay derecho)
        if i * 2 + 1 > self.tamanoActual:
            return i * 2
        else:
            # Compara los dos hijos y devuelve el índice del más chico
            if self.listaMonticulo[i * 2] < self.listaMonticulo[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

#Elimina y devuelve el mínimo (raíz).
#Para no dejar un hueco, mueve el último elemento a la raíz y lo baja hasta que todo quede en orden otra vez.           
    def eliminarMin(self):
        # Guarda el valor mínimo (siempre está en la raíz, posición 1)
        valorSacado = self.listaMonticulo[1]

        # Mueve el último elemento del montículo a la raíz (posición 1)
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]

        # Reduce el tamaño del montículo (uno menos)
        self.tamanoActual = self.tamanoActual - 1

        # Elimina el último elemento de la lista (ya está movido a la raíz)
        self.listaMonticulo.pop()

        # Restaura la propiedad del montículo bajando la raíz si es necesario
        self.infiltAbajo(1)

        # Devuelve el valor que se sacó (el mínimo original)
        return valorSacado

#Construye un montículo a partir de una lista desordenada.
#Empieza desde el último nodo padre y va bajando hasta la raíz, ajustando cada subárbol.
#Este algoritmo es O(n) (más rápido que insertar uno por uno).
    def construirMonticulo(self, unaLista):
        # Empieza desde el medio de la lista, que es el último nodo padre.
        i = len(unaLista) // 2

        # Define el tamaño actual del montículo
        self.tamanoActual = len(unaLista)

        # Crea una copia de la lista, agregando un 0 inicial (posición 0 vacía)
        self.listaMonticulo = [0] + unaLista[:]

        # Desde el último nodo padre hacia la raíz, aplica infiltAbajo
        # Esto asegura que toda la estructura cumpla la propiedad del montículo.
        while (i > 0):
            self.infiltAbajo(i)
            i = i - 1
