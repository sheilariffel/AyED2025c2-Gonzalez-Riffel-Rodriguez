# Importamos los algoritmos de ordenamiento implementados en módulos separados
from modules.ordenamiento_burbuja import ordenamiento_burbuja
from modules.ordenamiento_quicksort import quicksort
from modules.ordenamiento_radixsort import ordenamiento_radix

# Importamos la función que mide tiempos de ejecución
from modules.medicion_de_tiempo import medicion_de_tiempo

# Librerías para graficar
import matplotlib.pyplot as plt
import numpy as np

# Tamaños de listas que se evaluarán: desde 10 hasta 1000 en saltos de 50
tamanios = np.arange(10, 1050, 50) 

# Medición de tiempos para cada algoritmo de ordenamiento
lista_burbuja = medicion_de_tiempo(ordenamiento_burbuja)
lista_quicksort = medicion_de_tiempo(quicksort)
lista_radix = medicion_de_tiempo(ordenamiento_radix)
lista_sorted = medicion_de_tiempo(sorted)  # función built-in de Python


# -------------------------------------------------------------------
# Gráfica de los tiempos obtenidos
# -------------------------------------------------------------------
plt.plot(tamanios,lista_burbuja, label="burbuja")
plt.plot(tamanios,lista_quicksort, label="quicksort")
plt.plot(tamanios,lista_radix, label="radix")
plt.plot(tamanios,lista_sorted, label="sorted")

# Etiquetas y título
plt.xlabel("Tamaño de la lista (n)")
plt.ylabel("Tiempo (segundos)")
plt.title("Tiempo real de ejecución de operaciones")
plt.legend() 
plt.grid(True)

# Mostrar gráfico
plt.show()