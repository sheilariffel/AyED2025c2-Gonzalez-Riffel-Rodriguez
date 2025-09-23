
from modules.ordenamiento_burbuja import ordenamiento_burbuja
from modules.ordenamiento_quicksort import quicksort
from modules.ordenamiento_radixsort import radix_sort
from modules.lista_aleatoria import lista_aleatoria
from modules.medicion_de_tiempo import medicion_de_tiempo
import matplotlib.pyplot as plt
import numpy as np

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

tamanios = np.arange(10, 1050, 50) #no puedo usar mayor a 500 porque se rompe el ordenamiento
lista_111 = medicion_de_tiempo(ordenamiento_burbuja)
lista_222 = medicion_de_tiempo(quicksort)
lista_333 = medicion_de_tiempo(radix_sort)
lista_444 = medicion_de_tiempo(sorted)

 # Gráfica
plt.plot(tamanios,lista_111, label="burbuja")
plt.plot(tamanios,lista_222, label="quicksort")
plt.plot(tamanios,lista_333, label="residuos")
plt.plot(tamanios,lista_444, label="sorted")
plt.xlabel("Tamaño de la lista (n)")
plt.ylabel("Tiempo (segundos)")
plt.title("Tiempo real de ejecución de operaciones")
plt.legend()
plt.grid(True)
plt.show()