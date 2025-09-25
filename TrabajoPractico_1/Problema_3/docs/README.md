# 📝Documentación del proyecto

Implementar en python los siguientes algoritmos de ordenamiento:
Ordenamiento burbuja
Ordenamiento quicksort
Ordenamiento por residuos (radix sort)

Corroborar que funcionen correctamente con listas de números aleatorios de cinco dígitos generados aleatoriamente (mínimamente de 500 números en adelante).

Medir los tiempos de ejecución de tales métodos con listas de tamaño entre 1 y 1000. Graficar en una misma figura los tiempos obtenidos. ¿Cuál es el orden de complejidad O de cada algoritmo? ¿Cómo lo justifica con un análisis a priori?

Comparar ahora con la función built-in de python sorted. ¿Cómo funciona sorted? Investigar y explicar brevemente.

-----sorted() - una nueva función incorporada sorted() actúa como una lista sort() en el lugar pero se puede usar en expresiones, ya que devuelve una copia de la secuencia, ordenada.

La sorted()función devuelve una lista ordenada del objeto iterable especificado. Puede especificar el orden ascendente o descendente. Las cadenas se ordenan alfabéticamente y los números, numéricamente.


El proyecto también deberá contener un informe en pdf con una breve explicación -------de la solución y resultados de cada uno de los ejercicios (conclusiones o gráficas según lo solicite el enunciado)------. Puede agregarse algún pseudocódigo si se considera necesario para explicar las soluciones entregadas. En el caso del ejercicio 1 y 3, debe contener los análisis de complejidad que solicita el enunciado, con las gráficas correspondientes.


--------------------------------------------------------------------------------------------------------------------------
si quiero agregar graficas, debo poner en data 

Las graficas podemos ver que 
sorted es el mas rapido 
quicksort y radix estan ahi en una minima diferencia 
burbuja es el que mas demora 

segun sus ordenes de complejidad 
burbuja es O(n^2) por lo que el comportamiento es exponencial como vemos en el grafica 
quicksort y O(n log n) por lo su comportamiento es 
-----------------------------------------------------------------------------------------------------------------------
Paso 2: Complejidades (análisis a priori)

Burbuja:
---- Comparaciones y swaps ≈ 𝑂(𝑛^2)
---- Justificación: doble bucle anidado que recorre la lista.

Quicksort:
---- Mejor caso: 𝑂(𝑛 log 𝑛)(divide y conquista con particiones balanceadas).
---- Peor caso: 𝑂(𝑛^2) (siempre se elige mal el pivote, listas desbalanceadas).
---- Caso promedio: 𝑂(𝑛log𝑛)

Radix Sort:
---- Depende de la cantidad de dígitos 𝑑
d.

Complejidad: 
𝑂
(
𝑑
⋅
(
𝑛
+
𝑘
)
)
O(d⋅(n+k)) donde 
𝑘
=
10
k=10 (número de posibles dígitos).

Para números de 5 dígitos, 
𝑑
=
5
d=5, entonces 
𝑂
(
5
𝑛
)
=
𝑂
(
𝑛
)
O(5n)=O(n).

sorted() de Python:

Usa Timsort, un híbrido entre mergesort e insertion sort.

Complejidad: 
𝑂
(
𝑛
log
⁡
𝑛
)
O(nlogn).

Optimizado para casos reales, detecta runs (subsecuencias ya ordenadas).

🔹 Paso 3: Informe en PDF (estructura sugerida)

Se puede armar con reportlab o con pypandoc. Te paso un esquema del informe:

Informe: Algoritmos de Ordenamiento

Introducción
Breve descripción del problema y objetivo.

Implementación

Burbuja (con pseudocódigo y complejidad).

Quicksort (con pseudocódigo y complejidad).

Radix Sort (con explicación de dígitos y conteo).

Función sorted() (explicación de Timsort).

Resultados experimentales

Gráficas de tiempos.

Discusión: Burbuja muy lento, Quicksort eficiente, Radix lineal, Sorted muy optimizado.

Conclusiones

Confirmación de las complejidades a priori.

Diferencia entre algoritmos teóricos y la implementación optimizada de Python.