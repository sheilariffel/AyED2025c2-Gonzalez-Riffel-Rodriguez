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
    Ordenar = cola_de_espera.monticulo.tamanoActual

    # Mostrar los pacientes que están esperando
    for prioridad, orden, paciente in cola_de_espera.monticulo.listaMonticulo[1:]:
        print(f"\t{paciente} (orden {orden})")

    print('-*-' * 15)
    time.sleep(1)


