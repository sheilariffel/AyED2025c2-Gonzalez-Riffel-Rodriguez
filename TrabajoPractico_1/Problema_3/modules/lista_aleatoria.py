"""
Como debo corroborar que funcionen correctamente los ordenamientos con listas de números aleatorios 
de cinco dígitos generados aleatoriamente (mínimamente de 500 números en adelante), genero una función que me lo haga
"""
import random

def lista_aleatoria (n=600):
    lista = []

    for i in range (n): #genera el número aleatorio
        lista.append(random.randint(10000,99999)) #agrega los valores aletorios a la lista
    
    return lista