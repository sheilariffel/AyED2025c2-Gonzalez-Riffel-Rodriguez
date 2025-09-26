"""
------------------------------------------ORDENAMIENTO QUICKSORT-------------------------------------------------------
1 - Se selecciona un pivote que puede ser el primer número o el último o uno aleatorio. (En este caso es el primero)
2 - Se reorganiza la lista en dos sublistas:
    - valores menores al pivote 
    - valores mayores al pivote
3 - Luego se aplica el mismo procedimiento recursivamente a cada sublista.
"""

from modules.lista_aleatoria import lista_aleatoria

def quicksort(Lista):
   """
    Ordena una lista de números usando el algoritmo quicksort.
    Args:
        Lista (list): La lista de números a ordenar.
    Returns:
        list: La lista ordenada.
    """
   ordenamientoRapidoAuxiliar(Lista,0,len(Lista)-1)    # Llamo a la función auxiliar que usa punteros de inicio y fin
   return Lista # Devuelvo la lista ya ordenada

def ordenamientoRapidoAuxiliar(Lista,primero,ultimo):
   """
    Función auxiliar recursiva para aplicar quicksort en un subrango.
    """
   if primero<ultimo: # Condición base: si la sublista tiene al menos 2 elementos


       puntoDivision = particion(Lista,primero,ultimo) # Se obtiene la posición final del pivote después de reordenar

       ordenamientoRapidoAuxiliar(Lista,primero,puntoDivision-1)  # Ordenar la parte izquierda del pivote
       ordenamientoRapidoAuxiliar(Lista,puntoDivision+1,ultimo)  # Ordenar la parte derecha del pivote

#En el proceso de partición, encontrará el punto de división y al mismo tiempo moverá otros elementos al lado apropiado de la lista, según sean menores o mayores que el valor pivote.
def particion(Lista,primero,ultimo):
   """
    Función de partición: reordena la lista respecto a un pivote.
    Se elige el primer elemento como pivote.
    Args:
        Lista (list): lista de números.
        primero (int): índice inicial.
        ultimo (int): índice final.
    Returns:
        int: índice final del pivote.
    """
   valorPivote = Lista[primero]   # Se toma el primer elemento como pivote

   #El particionamiento comienza localizando dos marcadores de posición al principio y al final de los ítems restantes de la lista
   marcaIzq = primero+1    # Puntero que avanza desde la izquierda 
   marcaDer = ultimo   # Puntero que retrocede desde la derecha
   hecho = False

   while not hecho: # Repetimos hasta que los punteros se crucen
       
       while marcaIzq <= marcaDer and Lista[marcaIzq] <= valorPivote: # Avanza el puntero izquierdo hasta encontrar un valor mayor al pivote
           marcaIzq = marcaIzq + 1
           
       while Lista[marcaDer] >= valorPivote and marcaDer >= marcaIzq:  # Retrocede el puntero derecho hasta encontrar un valor menor al pivote
           marcaDer = marcaDer -1
      
       if marcaDer < marcaIzq: # Nos detendremos en el punto donde marcaDer se vuelva menor que marcaIzq
           hecho = True
    
      
       else:  # Intercambio de los valores encontrados en los punteros
           temp = Lista[marcaIzq]
           Lista[marcaIzq] = Lista[marcaDer]
           Lista[marcaDer] = temp

   # Finalmente colocamos el pivote en su lugar correcto
   temp = Lista[primero]
   Lista[primero] = Lista[marcaDer]
   Lista[marcaDer] = temp
   return marcaDer  # Retorna a la posición final del pivote
 

"""
-------------------------Verificación------------------------------------------------------------- 
Si el algoritmo de ordenamiento burbuja devuelve la lista ordenada. Usamos dos métodos de prueba:
1 - Generar una lista grande con lista_aleatoria(), ordenarla con nuestro algoritmo
    (quicksort()) y también con la función sorted() de Python.
    Luego comparamos ambas listas: 
       - Si son iguales → nuestro algoritmo funciona bien.
       - Si no lo son → hay un error en nuestra implementación.
2 - Generar una lista pequeña y aplicar nuestro método para ver el resultado.
"""
# --- Ejemplo para probar el algoritmo ---
if __name__=="__main__": #Me va a permitir que el ejemplo solo se ejecute en este módulo y no en el main
    
    #Primer método de prueba    
    #Como la lista contiene muchos elementos, no es práctico compararlos manualmente.

    Lista1 = lista_aleatoria() #Genera una lista de números aleatorios de 5 dígitos
    lista_quicksort = quicksort(Lista1.copy())#Usamos quicksort() (hacemos copia para no alterar la lista original)
    lista_sort = sorted(Lista1.copy())  #Usamos sorted() (función de Python que siempre ordena correctamente)
    
    # Comparamos los resultados de ambas listas
    if lista_quicksort == lista_sort:
        print("Las listas son iguales") # Si coinciden, nuestro algoritmo funciona correctamente.
    else: 
        print("Las listas no son iguales") # Si no coinciden, hay un error en la implementación.
    # -------------------------------

    #Segundo método de prueba
    #Ejemplo con una lista más corta (más fácil de ver en pantalla)   
    numeros = [54,26,93,17,77,31,44,55,20]

    #Muestro las listas previas a ser ordenadas
    print()
    print(f"Lista original: {numeros}")
    lista_ordenada = quicksort(numeros) #Aplico ordenamiento quicksort()
    print(f"Lista ordenada: {lista_ordenada}") #Muestro las listas ordenadas

"""
--------------------------- Versión descartada --------------------------------------
No era práctica a la hora de realizar medición de tiempo y graficación.
Para este ordenamiento la función solicitaba 3 parámetros, la lista y los punteros. Y cuando haciamos una llamada
a la función siempre quedaba descolgados esos 2 parámetros y se dificultó realizar la graficación 
-------------------------------------------------------------------------------------


def particion(lista, bajo, alto):
    
    Función auxiliar para particionar la lista.
    Elige el último elemento como pivote, coloca todos los elementos menores
    que el pivote a la izquierda, y los mayores a la derecha.
    
    pivote = lista[alto]
    i = (bajo - 1)  # Índice del elemento más pequeño   i es el puntero de la izquierda

    for j in range(bajo, alto): #j es el puntero de la derecha
        # Si el elemento actual es menor o igual que el pivote
        if lista[j] <= pivote:
            i = i + 1
            # Intercambia lista[i] y lista[j]
            lista[i], lista[j] = lista[j], lista[i]

    # Intercambia lista[i+1] y el pivote (lista[alto])
    lista[i + 1], lista[alto] = lista[alto], lista[i + 1]
    return (i + 1) #devuelve la posición del pivote, y a partir de aca ordeno los que estan antes y después

def quicksort(lista,bajo=0, alto=0):

    Función principal de quicksort que ordena la lista de forma recursiva.

    if alto==0: 
        alto=len(lista)-1

    if bajo < alto:

        # p_index es el índice de partición, lista[p_index] ya está en su lugar.Ese esta bien ordenado, falta ordenar loq ue está antes y lo que está después
        p_index = particion(lista, bajo, alto)

        # Ordena los elementos antes de la partición
        quicksort(lista, bajo, p_index - 1)

        # Ordena los elementos después de la partición
        quicksort(lista, p_index + 1, alto)
"""