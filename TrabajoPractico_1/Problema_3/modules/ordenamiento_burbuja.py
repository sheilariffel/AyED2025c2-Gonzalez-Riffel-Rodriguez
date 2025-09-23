# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código
from modules.lista_aleatoria import lista_aleatoria
"""
def ordenamiento_burbuja(lista):
   
    n = len(lista)

    # Recorremos todos los elementos de la lista
    for i in range(n):
        # La última 'i' elementos ya están en su lugar correcto,
        # por lo que no necesitamos compararlos de nuevo.
        for j in range(0, n - i - 1):
            # Comparamos los elementos adyacentes
            if lista[j] > lista[j + 1]:
                # Si el elemento actual es mayor que el siguiente, los intercambiamos
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista



def ordenamiento_burbuja(Lista):
    intercambios = True
    numPasada = len(Lista)-1
    while numPasada > 0 and intercambios:
       intercambios = False
       for i in range(numPasada):
           if Lista[i]>Lista[i+1]:
               intercambios = True
               temp = Lista[i]
               Lista[i] = Lista[i+1]
               Lista[i+1] = temp
       numPasada = numPasada-1
    return Lista
"""

#unaLista = [54,26,93,17,77,31,44,55,20]
#ordenamientoBurbuja(unaLista)
#print(unaLista)

#del libro, fue el mas eficiente a la hora de graficar
def ordenamiento_burbuja(Lista):
    for numPasada in range(len(Lista)-1,0,-1):
        for i in range(numPasada):
            if Lista[i]>Lista[i+1]:
                temp = Lista[i]
                Lista[i] = Lista[i+1]
                Lista[i+1] = temp
    return Lista



#ejemplo realizado para verificar que realmente se comparen los valores y sean iguales. Usando la funcion sorter
if __name__== "__main__":
    lista1 = lista_aleatoria()
    lista_burbuja = ordenamiento_burbuja(lista1.copy()) #metodo copy
    #print(lista_burbuja)

    lista_sort = sorted(lista1.copy())  #como tengo demasiados numeros, no puedo comparar 1 por uno si realmente estan ordenados
    #por lo tanto lo que hago es llamar a la funcion sortes que tambien ordena los elementos, y los comparo con mi metodo
    #si son iguales arroja un comentario de que son iguales y si no lo son, me informa que no son iguales
    if lista_burbuja == lista_sort:
        print("son iguales")
    else: 
        print("no son iguales")


    # Ejemplo de uso
    #print()
    #numeros = [64, 34, 25, 12, 22, 11, 90]
    #print(f"Lista original: {numeros}")

    #lista_ordenada = ordenamiento_burbuja(numeros)
    #print(f"Lista ordenada: {lista_ordenada}")

    """
    Ordena una lista de números usando el algoritmo de ordenamiento burbuja.

    Args:
        lista (list): La lista de números a ordenar.

    Returns:
        list: La lista ordenada.
    """