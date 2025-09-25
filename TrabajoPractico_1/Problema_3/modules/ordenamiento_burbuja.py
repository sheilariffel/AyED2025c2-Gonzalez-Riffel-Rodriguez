"""
A continuación se muestran distintas implementaciones del algoritmo de ordenamiento burbuja.
Algunas están comentadas porque se usaron en pruebas previas, para comparar eficiencia 
y comprobar cuál versión era más rápida y adecuada para graficar.

2. Segunda versión: incluye una optimización con una bandera (intercambios) 
   para terminar antes si la lista ya está ordenada.
3. Versión final: tomada del libro, resultó ser la más eficiente en las pruebas 
   al momento de graficar tiempos. Esta es la que quedó implementada.
"""

from modules.lista_aleatoria import lista_aleatoria # Importa la función que genera listas aleatorias de 5 dígitos 

"""Ordena una lista de números usando el algoritmo de ordenamiento burbuja.

    Args:
        lista (list): La lista de números a ordenar.

    Returns:
        list: La lista ordenada.
"""
# --- Implementación con optimización usando bandera (también quedó comentada) ---
def ordenamiento_burbuja1(Lista):
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

# --- Versión final utilizada (más eficiente en las pruebas realizadas) ---
#unaLista = [54,26,93,17,77,31,44,55,20]
#ordenamientoBurbuja(unaLista)
#print(unaLista)

#del libro, fue el mas eficiente a la hora de graficar
def ordenamiento_burbuja(Lista):
    # Se recorren varias "pasadas" sobre la lista.
    # En cada pasada, el mayor de los elementos "sube" hasta su posición correcta.
    for numPasada in range(len(Lista)-1,0,-1): # Recorre desde el final hacia el principio
        for i in range(numPasada):
            # Compara cada par de elementos adyacentes
            if Lista[i]>Lista[i+1]:
                 # Si el actual es mayor, se intercambian
                temp = Lista[i]
                Lista[i] = Lista[i+1]
                Lista[i+1] = temp
    return Lista

# -*- coding: utf-8 -*-

def ordenamientoBurbuja2(unaLista):
    # Recorremos desde el final hacia el inicio
    for extremo in range(len(unaLista)-1, 0, -1):
        hubo_cambio = False  # asumimos que no se harán cambios
        
        # Recorremos hasta el extremo comparando vecinos
        for i in range(extremo):
            if unaLista[i] > unaLista[i+1]:
                # Intercambiamos si están en el orden equivocado
                unaLista[i], unaLista[i+1] = unaLista[i+1], unaLista[i]
                hubo_cambio = True  # se hizo un cambio
        
        # Si no hubo cambios en toda la pasada, ya está ordenada
        if not hubo_cambio:
            print("La lista ya estaba ordenada. Algoritmo detenido.")
            break


# Ejemplo: lista desordenada
unaLista = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print("Lista original:", unaLista)
ordenamientoBurbuja2(unaLista)
print("Lista ordenada:", unaLista)

# Ejemplo: lista ya ordenada
otraLista = [1, 2, 3, 4, 5]
print("\nLista original:", otraLista)
ordenamientoBurbuja2(otraLista)
print("Lista ordenada:", otraLista)




#ejemplo realizado para verificar que realmente se comparen los valores y sean iguales. Usando la funcion sorter
# --- Bloque principal para probar el algoritmo ---
if __name__== "__main__":
    lista1 = lista_aleatoria() #Genera una lista de números aleatorios de 5 dígitos
    lista_burbuja = ordenamientoBurbuja2(lista1.copy()) #metodo copy # Ordena usando nuestro método

    #print(lista_burbuja)

    lista_sort = sorted(lista1.copy())  #como tengo demasiados numeros, no puedo comparar 1 por uno si realmente estan ordenados
    #por lo tanto lo que hago es llamar a la funcion sortes que tambien ordena los elementos, y los comparo con mi metodo
    #si son iguales arroja un comentario de que son iguales y si no lo son, me informa que no so iguales

    #-------------------------------

    # Ordena usando la función built-in de Python
    # Como la lista contiene muchos elementos, no es práctico compararlos manualmente.
    # Por eso, comparamos los resultados de nuestro algoritmo con los de sorted().
    if lista_burbuja == lista_sort:
        print("son iguales") # Si coinciden, nuestro algoritmo funciona correctamente.
    else: 
        print("no son iguales") # Si no coinciden, hay un error en la implementación.



    # Ejemplo de uso
    print()
    numeros = [64, 34, 25, 12, 22, 11, 90]
    print(f"Lista original: {numeros}")

    lista_ordenada = ordenamientoBurbuja2(numeros)
    print(f"Lista ordenada: {lista_ordenada}")
    print()
    nume = [1,2,3,4,5,6]
    lista_ordenada1 = ordenamientoBurbuja2(nume)
    print(lista_ordenada1)

    