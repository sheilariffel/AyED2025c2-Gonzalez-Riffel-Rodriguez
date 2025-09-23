# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código

#b) Ordenamiento quicksort: Se selecciona un pivote que puede ser el primer número o el último o uno 
# aleatorio. 
# La lista que queda se reorganizan 1 a 1 hasta encontrar la ubicación exacta de ese pivote y se 
# realiza continuamente.
import sys    
import random
sys.setrecursionlimit(2000)

def particion(lista, bajo, alto):# Ejemplo de una función de partición con pivote aleatorio
    # Elegir un pivote aleatorio
    pivote_idx = random.randint(bajo, alto)
    lista[pivote_idx], lista[alto] = lista[alto], lista[pivote_idx]
    
    pivote = lista[alto]
    i = bajo - 1
    
    for j in range(bajo, alto):
        if lista[j] <= pivote:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
            
    lista[i + 1], lista[alto] = lista[alto], lista[i + 1]
    return i + 1

def quicksort(lista,bajo=0, alto=0):
    """
    Función principal de quicksort que ordena la lista de forma recursiva.
    """
    if alto==0: 
        alto=len(lista)-1

    if bajo < alto:

        # p_index es el índice de partición, lista[p_index] ya está en su lugar.Ese esta bien ordenado, falta ordenar loq ue está antes y lo que está después
        p_index = particion(lista, bajo, alto)

        # Ordena los elementos antes de la partición
        quicksort(lista, bajo, p_index - 1)

        # Ordena los elementos después de la partición
        quicksort(lista, p_index + 1, alto)
    

if __name__=="__main__":
    # Ejemplo de uso
    numeros = [10, 7, 8, 9, 1, 5]
    print(numeros)
    n = len(numeros)
    quicksort(numeros, 0, n - 1) 

    print("Lista ordenada usando quicksort:")
    print(numeros)
"""
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
"""