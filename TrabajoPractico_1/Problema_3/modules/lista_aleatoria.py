"""
Para corroborar que los distintos ordenamientos funcionen, se genera una función que me genere una lista de 750 números 
aleatorios de cinco dígitos, y luego en el main, realizar la llamada de los ordenamientos. 
"""
import random # Importa el módulo random, que permite generar números aleatorios.

def lista_aleatoria (n=750): # Define una función que genera una lista de 600 números aleatorios. 
    lista = [] # Se crea una lista vacía donde se guardarán los números generados.

    for i in range (n): # Repite el bucle n veces (en este caso, 750 por defecto).
        #Genera un número entero aleatorio de 5 dígitos entre 10000 y 99999 
        lista.append(random.randint(10000,99999)) # Agrega el número al final de la lista con append()
    return lista # Devuelve la lista completa de números aleatorios generados.
