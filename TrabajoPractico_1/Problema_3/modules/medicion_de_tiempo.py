import time 
from modules.lista_aleatoria import lista_aleatoria


def medicion_de_tiempo (func_ordenamiento):
    lista_de_tiempos = [] #donde voy guardando el tiempo de ordenamiento
    for i in range (10, 1050, 50):
        lista = lista_aleatoria(i) 
        
        inicio = time.perf_counter() #me da valor de tiempo
        func_ordenamiento(lista)
        fin = time.perf_counter()
        total = fin - inicio
        lista_de_tiempos.append(total)

    return lista_de_tiempos

