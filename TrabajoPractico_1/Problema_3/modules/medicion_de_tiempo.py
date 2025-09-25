"""
Como debo medir los tiempos de ejecución de todos los ordenamientos con listas de tamaño entre 1 y 1000. 
Genero una función que mida el tiempo
"""
import time # Importa el módulo time, que permite medir tiempos 
from modules.lista_aleatoria import lista_aleatoria # Importa la función que genera listas aleatorias de 5 dígitos 

def medicion_de_tiempo (func_ordenamiento):  
    # La función recibe como parámetro otra función (el algoritmo de ordenamiento a medir).
    lista_de_tiempos = [] # Genero lista vacía para guardar los tiempos de ejecuación obtenidos
                     
    # Genera listas de distintos tamaños: desde 10 hasta 1000, avanzando de 50 en 50.
    for i in range (10, 1050, 50):  
        lista = lista_aleatoria(i) # Crea una lista de tamaño i con números aleatorios de 5 dígitos
        inicio = time.perf_counter() # Me da el valor inicial de tiempo
        func_ordenamiento(lista) # Ejecuta el algoritmo de ordenamiento sobre la lista
        fin = time.perf_counter() # Registra el tiempo final tras terminar el ordenamiento
        total = fin - inicio # Calcula el tiempo total transcurrido en segundos
        lista_de_tiempos.append(total) # Agrega ese tiempo a la lista de resultados

    return lista_de_tiempos  # Devuelve la lista completa con los tiempos medidos.

