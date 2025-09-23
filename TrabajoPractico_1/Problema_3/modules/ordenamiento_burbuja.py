# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código
from modules.lista_aleatoria import lista_aleatoria
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

#ejemplo realizado para verificar que realmente se comparen los valores y sean iguales. Usando la funcion sorter
if __name__== "__main__":
    lista1 = lista_aleatoria()
    lista_burbuja = ordenamiento_burbuja(lista1.copy()) #metodo copy
    #print(lista_burbuja)

    lista_sort = sorted(lista1.copy())
    if lista_burbuja == lista_sort:
        print("son iguales")
    else: 
        print("no son iguales")


    # Ejemplo de uso
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