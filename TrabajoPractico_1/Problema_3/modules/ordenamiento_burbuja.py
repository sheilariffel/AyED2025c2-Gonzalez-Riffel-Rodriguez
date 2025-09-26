"""
------------------------------------------ORDENAMIENTO BURBUJA-------------------------------------------------------
Funciona como si fueran burbujas en el agua: Vas comparando dos elementos vecinos de la lista. Si el de 
la izquierda es más grande que el de la derecha, los intercambiás. Después seguís comparando los 
siguientes pares. Al final de una pasada, el número más grande termina en el último lugar 
(como una burbuja que sube). Entonces, en la siguiente pasada ya no hace falta mirar ese último.

# --- Versión sin considerar los casos cuando la lista ya esta ordenada desde el principio d---
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

    
Función: ordenamiento_burbuja
Ordena una lista de números usando el algoritmo de ordenamiento burbuja.

Args:
    lista (list): La lista de números a ordenar.
Returns:
    list: La lista ordenada en orden ascendente.
   
"""
# Importa la función que genera lista aletoria para corroborar el funcionamiento de este ordenamiento
from modules.lista_aleatoria import lista_aleatoria 

# --- Implementación con optimización ---
def ordenamiento_burbuja(Lista):
    intercambios = True              # Al inicio supone que habrá intercambios
    numPasada = len(Lista)-1         # Última posición a revisar (cada pasada reduce este valor)

    # El bucle sigue mientras queden posiciones y se hayan hecho intercambios
    while numPasada > 0 and intercambios:
       intercambios = False          # Al inicio de cada pasada, asume que no habrá intercambios

       # Recorre los elementos desde 0 hasta numPasada-1
       for i in range(numPasada):
           # Si el elemento actual es mayor que el siguiente, hay intercambio
           if Lista[i] > Lista[i+1]: # Compara cada par de elementos adyacentes
               intercambios = True   # Marca que sí hubo un intercambio (la lista no estaba ordenada)
               
               # Intercambio usando una variable auxiliar
               temp = Lista[i]
               Lista[i] = Lista[i+1] # Si el actual es mayor, se intercambian
               Lista[i+1] = temp
       
       numPasada = numPasada - 1     # Reduce el rango, ya que el último elemento quedó ordenado

    return Lista                      # Devuelve la lista ordenada




"""
-------------------------Verificación------------------------------------------------------------- 
Si el algoritmo de ordenamiento burbuja devuelve la lista ordenada. Usamos dos métodos de prueba:
1 - Generar una lista grande con lista_aleatoria(), ordenarla con nuestro algoritmo
    (ordenamiento_burbuja) y también con la función sorted() de Python.
    Luego comparamos ambas listas: 
       - Si son iguales → nuestro algoritmo funciona bien.
       - Si no lo son → hay un error en nuestra implementación.
2 - Generar una lista pequeña y aplicar nuestro método para ver el resultado.
"""
# --- Ejemplo para probar el algoritmo ---
if __name__== "__main__": #Me va a permitir que el ejemplo solo se ejecute en este módulo y no en el main
    
    #Primer método de prueba    
    #Como la lista contiene muchos elementos, no es práctico compararlos manualmente.
    
    lista1 = lista_aleatoria() #Genera una lista de números aleatorios de 5 dígitos
    lista_burbuja = ordenamiento_burbuja(lista1.copy()) #Usamos ordenamiento_burbuja (hacemos copia para no alterar la lista original)
    lista_sort = sorted(lista1.copy())  #Usamos sorted() (función de Python que siempre ordena correctamente)
    
    # Comparamos los resultados de ambas listas
    if lista_burbuja == lista_sort:
        print("Las listas son iguales") # Si coinciden, nuestro algoritmo funciona correctamente.
    else: 
        print("Las listas no son iguales") # Si no coinciden, hay un error en la implementación.
    # -------------------------------

    #Segundo método de prueba
    #Ejemplo con una lista más corta (más fácil de ver en pantalla)
    numeros = [64, 34, 25, 12, 22, 11, 90]
    nume = [1,2,3,4,5,6]

    #Muestro las listas previas a ser ordenadas
    print()
    print(f"Lista 1 original: {numeros}")
    print("Lista 2 ordenada desde el inicio: ", nume)

    #Aplico ordenamiento_burbuja()
    lista_ordenada = ordenamiento_burbuja(numeros) 
    lista_ordenada1 = ordenamiento_burbuja(nume)

    #Muestro las listas ordenadas
    print(f"Lista 1 ordenada: {lista_ordenada}")
    print("Lista 2 ordenada: ",lista_ordenada1)
 
    
    

    