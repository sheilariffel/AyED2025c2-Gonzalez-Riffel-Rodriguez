"""
------------------------------------------ORDENAMIENTO RADIX SORT-------------------------------------------------------
Es un algoritmo de ordenamiento no comparativo, o sea, no compara directamente los números como hace burbuja o 
quicksort. Lo que hace es ordenar los números dígito por dígito, desde el menos significativo (unidades) hasta el 
más significativo (decenas, centenas, etc.). 
1 - Radix Sort funciona mirando los números dígito por dígito.
2 - Arranca por las unidades, y reparte los números en cajitas según ese dígito.
3 - Junta las cajitas en orden y reconstruye la lista.
4 - Después hace lo mismo con las decenas, luego centenas, etc.
5 - Repite hasta que ya no haya dígitos que mirar (se pasa del número más grande).
6 - Así, de a poquito, la lista va quedando más y más ordenada, hasta que queda totalmente ordenada.

"""

def obtener_digito(numero, posicion_digito, base = 10):
    """
    Obtiene el dígito en la posición especificada (de derecha a izquierda) de un número.
    Devuelve cero si la posición es mayor que el número de dígitos del número.
   
    Devuelve el dígito en la posición especificada (de derecha a izquierda).
    Ejemplo: numero=12345, posicion_digito=0 → 5 (unidades)
                           posicion_digito=2 → 3 (centenas)
    """
    return (numero // (base ** posicion_digito)) % base

def ordenamiento_radix(lista):
 
    # Encuentra el número máximo para determinar el número de dígitos
    max_num = max(lista)  # Número más grande para saber hasta dónde iterar
    exp = 1  # Exponente para la posición del dígito 
    lista_aux = [[] for _ in range(10)]  
    pos = 0  # Inicializa la posición del dígito 
    while max_num // exp > 0:  # Mientras haya dígitos por procesar
        # Coloca los números en la lista auxiliar según el dígito actual
        for num in lista:
            digit = obtener_digito(num, pos)  # Obtiene el dígito en la posición actual
            lista_aux[digit].append(num)

        # Reconstruye la lista original a partir de la lista auxiliar
        sig_pos = 0  # Inicializa la posición en la lista original
        for sublist in lista_aux:
            for num in sublist:
                lista[sig_pos] = num  # Añade el número a la lista original 
                sig_pos += 1    


        # Limpia la lista auxiliar para la siguiente posición de dígito
        lista_aux = [[] for _ in range(10)]

        # Aumenta el exponente para pasar al siguiente dígito
        exp *= 10
        pos += 1

    return lista

from modules.lista_aleatoria import lista_aleatoria

"""
-------------------------Verificación------------------------------------------------------------- 
Si el algoritmo de ordenamiento radix sort devuelve la lista ordenada. Usamos dos métodos de prueba:
1 - Generar una lista grande con lista_aleatoria(), ordenarla con nuestro algoritmo
    (ordenamiento_radix()) y también con la función sorted() de Python.
    Luego comparamos ambas listas: 
       - Si son iguales → nuestro algoritmo funciona bien.
       - Si no lo son → hay un error en nuestra implementación.
2 - Generar una lista pequeña y aplicar nuestro método para ver el resultado.
"""
# --- Ejemplo para probar el algoritmo ---
if __name__=="__main__": 
    
    #Primer método de prueba, a las listas ordenadas las comparamos y vemos si son iguales
    Lista1 = lista_aleatoria() 
    lista_radix = ordenamiento_radix(Lista1.copy())
    lista_sort = sorted(Lista1.copy())  
        
    if lista_radix == lista_sort:       
        print("Las listas son iguales") 
    else: 
        print("Las listas no son iguales") 
    # -------------------------------

    #Segundo método de prueba, informa la lista original y la ordenada
    numeros = [54,26,93,17,77,31,44,55,20]
    print()
    print(f"Lista original: {numeros}")
    lista_ordenada = ordenamiento_radix(numeros) 
    print(f"Lista ordenada: {lista_ordenada}") 


"""
-------------------------Versión descartada------------------------------------------------------------- 
def counting_sort(lista, exp): #ordenamiento por cuentas
    
    Algoritmo principal Radix Sort.
    Aplica counting_sort para cada dígito desde unidades hasta el máximo número.

    Args:
        lista (list): Lista de números enteros a ordenar.

    Returns:
        None: La lista se ordena en su lugar.
    
    Subrutina de Radix Sort que ordena la lista según el dígito
    indicado por 'exp' (1 = unidades, 10 = decenas, 100 = centenas, etc.).
    
   
    n = len(lista)
    salida = [0] * n   #es del tamaño de la lista   # Lista auxiliar donde se guarda el resultado parcial
    conteo = [0] * 10  #cuanto digitos del 0 al 9  # Contador de frecuencia para cada dígito (0-9)

    # Contar la ocurrencia de cada dígito # 1) Contar la frecuencia de cada dígito en la posición actual
    for i in range(n): #cuento cuantas veces aparece ese digito en la lista original, y segun el exp me fijo en la unidad decena o centene
        indice = (lista[i] // exp) % 10
        conteo[indice] += 1

    # Cambiar conteo[i] para que contenga la posición real del dígito en la salida  # 2) Transformar conteo en acumulado -> indica posición final en salida[]
    for i in range(1, 10):  #una vez que se llena el contador, se hace como una suma acumulada en el vector, pasando a representar posiciones en la lista ordenada
        conteo[i] += conteo[i - 1]

    # Construir el array(arreglo) de salida  # 3) Construir la salida en orden estable (de derecha a izquierda)
    i = n - 1
    while i >= 0: #recorre en sentido inverso
        indice = (lista[i] // exp) % 10
        salida[conteo[indice] - 1] = lista[i]
        conteo[indice] -= 1
        i -= 1
        
    # Copiar el array de salida a la lista original  # 4) Copiar la lista ordenada parcial a la lista original
    for i in range(n):
        lista[i] = salida[i]

def radix_sort(lista):
    
    #Función principal de ordenamiento por residuos que utiliza
    #counting_sort para ordenar por cada dígito.
    
    
    #Implementación de Radix Sort utilizando Counting Sort como subrutina.
    
    # Encontrar el número máximo  para determinar el número de dígitos
    maximo = max(lista) # Para saber cuántos dígitos tiene el número más grande

    # Ordenar por cada dígito, empezando por las unidades (exp = 1)
    exp = 1
    while maximo // exp > 0: # Repite para unidades, decenas, centenas...
        counting_sort(lista, exp)
        exp *= 10
    return lista

"""
