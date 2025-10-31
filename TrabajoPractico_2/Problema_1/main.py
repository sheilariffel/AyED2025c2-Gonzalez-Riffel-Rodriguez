# -*- coding: utf-8 -*-
"""
Sala de emergencias
"""

import time
import datetime
import random

from modulos.paciente import Paciente
from modulos.cola_prioridad import ColaDePrioridad

n = 20  # cantidad de ciclos de simulación

# cola_de_espera = list()
"""
Modificamos la cola de espera para que pase de ser una lista, a una cola de prioridad que me permita
atender los pacientes según su riesgo de salud 
"""

# Se crea la cola de prioridad (la "sala de espera")
cola_de_espera = ColaDePrioridad()

# Ciclo principal de la simulación
for i in range(n):
    # Mostrar fecha y hora del ciclo
    ahora = datetime.datetime.now()
    fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S')
    print('-*-' * 15)
    print('\n', fecha_y_hora, '\n')


    # paciente = pac.Paciente()
    # cola_de_espera.append(paciente)  -> Esto solo agrega el paciente al final de la lista, sin importar su riesgo.
    """Modificamos para que tome la cola de prioridad"""

    # Crear un paciente nuevo con datos aleatorios
    paciente = Paciente()
    print(f"Llega {paciente}")

    """Esto no solo inserta al paciente. Lo inserta en el lugar correcto según su prioridad (nivel de riesgo)."""
    # Insertar al paciente en la cola según su riesgo (prioridad)
    cola_de_espera.insertar(paciente.get_riesgo(), paciente)

    # Con 50% de probabilidad, se atiende un paciente
    if random.random() < 0.5 and not cola_de_espera.esta_vacia():

        """Modificamos porque sino atendia siempre el primero que llegaba aunque sea leve y haya llegado alguien más grave"""
        #paciente_atendido = cola_de_espera.pop(0)

        # Se saca el paciente con mayor prioridad (menor número de riesgo)
        prioridad, orden, paciente_atendido = cola_de_espera.eliminar()
        print('*' * 40)
        print(f"Se atiende a: {paciente_atendido}")
        print('*' * 40)
    else:
        print("No se atiende paciente en este turno.")

    print()
    print("Pacientes que faltan atenderse:", cola_de_espera.monticulo.tamanoActual)
    Ordenar = cola_de_espera.monticulo.tamanoActual

    # Mostrar la cola de espera (los pacientes aún sin atender)
    for prioridad, orden, paciente in cola_de_espera.monticulo.listaMonticulo[1:]:
        print(f"\t{paciente} (orden {orden})")

    print('-*-' * 15)
    # Pausa de 1 segundo entre ciclos
    time.sleep(1)


