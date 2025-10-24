# -*- coding: utf-8 -*-

#ESTO Y EL MODULO PACIENTE ES DE TP2
"""
Sala de emergencias
"""

import time
import datetime
import random

from modulos.paciente import Paciente
from modulos.cola_prioridad import ColaDePrioridad

n = 10  # cantidad de ciclos de simulación

cola_de_espera = ColaDePrioridad()

for i in range(n):
    ahora = datetime.datetime.now()
    fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S')
    print('-*-' * 15)
    print('\n', fecha_y_hora, '\n')

    paciente = Paciente()
    print(f"Llega {paciente}")

    # Insertar paciente con riesgo (prioridad)
    cola_de_espera.insertar(paciente.get_riesgo(), paciente)

    # 50% de probabilidad de atender un paciente
    if random.random() < 0.5 and not cola_de_espera.esta_vacia():
        prioridad, orden, paciente_atendido = cola_de_espera.eliminar()
        print('*' * 40)
        print(f"Se atiende a: {paciente_atendido}")
        print('*' * 40)
    else:
        print("No se atiende paciente en este turno.")

    print()
    print("Pacientes que faltan atenderse:", cola_de_espera.monticulo.tamanoActual)

    # Mostrar los pacientes que están esperando
    for prioridad, orden, paciente in cola_de_espera.monticulo.listaMonticulo[1:]:
        print(f"\t{paciente} (orden {orden})")

    print('-*-' * 15)
    time.sleep(1)



"""


import time
import datetime
import modulos.paciente as pac
import random
import modulos.cola_prioridad as pac

n = 20  # cantidad de ciclos de simulación



cola_de_espera = list()


# Ciclo que gestiona la simulación
for i in range(n):
    # Fecha y hora de entrada de un paciente
    ahora = datetime.datetime.now()
    fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S')
    print('-*-'*15)
    print('\n', fecha_y_hora, '\n')

    # Se crea un paciente un paciente por segundo
    # La criticidad del paciente es aleatoria
    paciente = pac.Paciente()
    cola_de_espera.append(paciente)

    # Atención de paciente en este ciclo: en el 50% de los casos
    if random.random() < 0.5:
        # se atiende paciente que se encuentra al frente de la cola
        paciente_atendido = cola_de_espera.pop(0)
        print('*'*40)
        print('Se atiende el paciente:', paciente_atendido)
        print('*'*40)
    else:
        # se continúa atendiendo paciente de ciclo anterior
        pass
    
    print()

    # Se muestran los pacientes restantes en la cola de espera
    print('Pacientes que faltan atenderse:', len(cola_de_espera))
    for paciente in cola_de_espera:
        print('\t', paciente)
    
    print()
    print('-*-'*15)
    
    time.sleep(1)



# main.py
from modulos.cola_prioridad import ColaDePrioridad

def main():
    cola = ColaDePrioridad()

    # Insertamos pacientes: (prioridad, nombre)
    cola.insertar(3, "Paciente A - Riesgo bajo")
    cola.insertar(1, "Paciente B - Crítico")
    cola.insertar(2, "Paciente C - Moderado")

    print("Atendiendo pacientes según prioridad:\n")
    while not cola.esta_vacia():
        prioridad, paciente = cola.eliminar()
        print(f"Atendiendo {paciente} (riesgo {prioridad})")

if __name__ == "__main__":
    main()

# sala_emergencias.py

import time
import datetime
import random

from modulos.paciente import Paciente
from modulos.cola_prioridad import ColaDePrioridad

n = 20  # cantidad de ciclos de simulación

# Creamos la cola de prioridad
cola_de_espera = ColaDePrioridad()

for i in range(n):
    ahora = datetime.datetime.now()
    fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S')
    print('-*-' * 15)
    print('\n', fecha_y_hora, '\n')

    # Crear paciente nuevo
    paciente = Paciente()
    print(f"Llega {paciente}")

    # Insertar paciente en la cola de prioridad según su riesgo
    cola_de_espera.insertar(paciente.get_riesgo(), paciente)

    # 50% de probabilidad de atender un paciente en este ciclo
    if random.random() < 0.5 and not cola_de_espera.esta_vacia():
        prioridad, paciente_atendido = cola_de_espera.eliminar()
        print('*' * 40)
        print(f"Se atiende a: {paciente_atendido}")
        print('*' * 40)
    else:
        print("No se atiende paciente en este turno.")

    print()
    print("Pacientes que faltan atenderse:", cola_de_espera.monticulo.tamanoActual)
    
    # Mostrar pacientes en espera
    for prioridad, paciente in cola_de_espera.monticulo.listaMonticulo[1:]:
        print(f"\t{paciente}")

    print('-*-' * 15)
    time.sleep(1)
"""