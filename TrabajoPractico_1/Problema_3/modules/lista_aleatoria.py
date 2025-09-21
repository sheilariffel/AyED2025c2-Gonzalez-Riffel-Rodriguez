import random

def lista_aleatoria (n=500):
    lista = []

    for i in range (n): #genera el número aleatorio
        lista.append(random.randint(10000,99999)) #agrega los valores aletorios a la lista
    
    return lista