#c) Ordenamiento por residuos (radix sort): Tienes una lista desde el 0 al 9 en donde se 
# utilizaran para sumar cantidades, 
# empezar a verificar primero las unidades de todos los números y cada número que este lo 
# vas sumando en las cantidades que van del 0 al 9,    

def counting_sort(lista, exp): #ordenamiento por cuentas
    """
    Función de ordenamiento por conteo para ordenar una lista según
    el dígito representado por 'exp' (ej. 1, 10, 100, ...).
    """
    n = len(lista)
    salida = [0] * n   #es del tamaño de la lista
    conteo = [0] * 10  #cuanto digitos del 0 al 9

    # Contar la ocurrencia de cada dígito
    for i in range(n): #cuento cuantas veces aparece ese digito en la lista original, y segun el exp me fijo en la unidad decena o centene
        indice = (lista[i] // exp) % 10
        conteo[indice] += 1

    # Cambiar conteo[i] para que contenga la posición real del dígito en la salida
    for i in range(1, 10):  #una vez que se llena el contador, se hace como una suma acumulada en el vector, pasando a representar posiciones en la lista ordenada
        conteo[i] += conteo[i - 1]

    # Construir el array(arreglo) de salida
    i = n - 1
    while i >= 0: #recorre en sentido inverso
        indice = (lista[i] // exp) % 10
        salida[conteo[indice] - 1] = lista[i]
        conteo[indice] -= 1
        i -= 1
        
    # Copiar el array de salida a la lista original
    for i in range(n):
        lista[i] = salida[i]

def radix_sort(lista):
    """
    Función principal de ordenamiento por residuos que utiliza
    counting_sort para ordenar por cada dígito.
    """
    # Encontrar el número máximo para determinar el número de dígitos
    maximo = max(lista)

    # Ordenar por cada dígito, empezando por las unidades (exp = 1)
    exp = 1
    while maximo // exp > 0:
        counting_sort(lista, exp)
        exp *= 10


if __name__=="__main__":
# Ejemplo de uso
    numeros = [170, 45, 75, 90, 802, 24, 2, 66]
    print(f"Lista original: {numeros}")

    radix_sort(numeros)
    print(f"Lista ordenada: {numeros}")

