# 📝Documentación del proyecto
---
Resolución: 
1 - Descargar simulación de la sala de emergencia 
2 - Implementar un montículo de mínima
3 - Implementar cola de prioridad que ocupa el montículo de mínima
4 - Integrar la cola de prioridad en la sala de emergencia propuesta por la cátedra
5 - Ajustar cola de prioridad para cumplir la consigna de igual orden de criticidad

#Objetivo del trabajo
Modificar el proyecto de Sala de Emergencias para que los pacientes se atiendan según su nivel de riesgo (prioridad médica) y no por orden de llegada. 

Tenés tres niveles de riesgo:
1 → crítico
2 → moderado
3 → bajo


Quiero que siempre se atienda primero el paciente con menor número de riesgo, o sea, el más grave. Para esto aplicamos una cola de prioridad, también conocida como heap o montículo. Es una estructura que permite insertar elementos con una “prioridad” asociada, y siempre permite extraer (eliminar) el elemento con la mayor prioridad (o menor, según se defina). En este caso, la prioridad será el nivel de riesgo del paciente. El montículo no “sabe” nada de pacientes ni de prioridades semánticas (solo maneja un conjunto de elementos y mantiene siempre el menor arriba), el que va a establecer el orden en que serán atendidos lo establece la cola de prioridad.

Inserción
Se agrega un paciente al montículo manteniendo la propiedad del orden (menor riesgo = más prioridad). Complejidad: O(log n)
Eliminación (atender paciente)
Se extrae el paciente con mayor prioridad (riesgo más bajo numéricamente). Complejidad: O(log n)


Acceso al siguiente paciente
Consultar el elemento con mayor prioridad (sin eliminarlo). Complejidad: O(1)

El criterio secundario para desempatar entre pacientes con el mismo nivel de riesgo es el orden de llegada, asegurando un tratamiento justo y reproducible.

sala_emergencias/
│
├── main.py                            	# Programa principal
│
├── monticulo.py             		# Clase MonticuloBinario 
│
├── cola_prioridad.py         	# Clase ColaDePrioridad 
│
└── test/                              	# Carpeta opcional para pruebas
    ├── test_monticulo.py
    └── test_cola_prioridad.py






