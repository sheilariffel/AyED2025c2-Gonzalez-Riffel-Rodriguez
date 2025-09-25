
from modules.ordenamiento_burbuja import ordenamiento_burbuja
from modules.ordenamiento_quicksort import quicksort
from modules.ordenamiento_radixsort import radix_sort
from modules.medicion_de_tiempo import medicion_de_tiempo
import matplotlib.pyplot as plt
import numpy as np

"""
lista_1 = lista_aleatoria()
ordenamiento_burbuja(lista_1)
print(lista_1)
print()

lista_2 = lista_aleatoria()
quicksort(lista_2)
print(lista_2)
print()

lista_3 = lista_aleatoria()
radix_sort(lista_3)
print(lista_3)

print()
lista_11 = medicion_de_tiempo(ordenamiento_burbuja)
print(lista_11)
"""
tamanios = np.arange(10, 1050, 50) 
lista_burbuja = medicion_de_tiempo(ordenamiento_burbuja)
lista_quicksort = medicion_de_tiempo(quicksort)
lista_radix = medicion_de_tiempo(radix_sort)
lista_sorted = medicion_de_tiempo(sorted)

 # Gráfica
plt.plot(tamanios,lista_burbuja, label="burbuja")
plt.plot(tamanios,lista_quicksort, label="quicksort")
plt.plot(tamanios,lista_radix, label="residuos")
plt.plot(tamanios,lista_sorted, label="sorted")
plt.xlabel("Tamaño de la lista (n)")
plt.ylabel("Tiempo (segundos)")
plt.title("Tiempo real de ejecución de operaciones")
plt.legend()
plt.grid(True)
plt.show()