# 🐍MediCuidado
Modificar el proyecto de Sala de Emergencias para que los pacientes se atiendan según su nivel de riesgo (prioridad médica) y no por orden de llegada. 

---
## 🏗Arquitectura General

Explica brevemente cómo está organizado el código (funciones y/o clases)
* La sección de módulos contiene 4 archivos 
   - Archivo abb -> utilizado para realizar test 
   - Archivo cola_prioridad -> utilizado para ordenar a los pacientes según el riesgo y el orden de llegada
   - Archivo monticulobinario -> utilizado por la cola de prioridad para realizar funciones especificas, como insertar, eliminar, mover un elemento arriba o abajo. 
   - Archivo paciente -> contiene información aleatoria de los pacientes que irán ingresando. Utiliza la clase paciente que contiene funciones que van guardando, nombre, apellido, número de riesgo y descripcion del riesgo. 
* La sección doc contiene el informe del problema en formato PDF
* La sección data contendría graficas, pero en este problema no se utilizaron 
* La sección aplicaciones -> no se que iría acá
* La sección de test que es para realizar pruebas del problema
* Un main principal donde se encuentra la estructura de la sala de emergencia

## 🙎‍♀️🙎‍♂️Autores

- Gonzalez Maria Jimena
- Riffel Sheila Gabriela
- Rodriguez Maite

---
# Consideraciones que estoy teniendo del trabajo

1 - Descargar simulación de la sala de emergencia y probarla
2 - Implementar un montículo de mínima
3 - Implementar cola de prioridad que ocupa el montículo de mínima
4 - Integrar la cola de prioridad en la sala de emergencia propuesta por la cátedra
5 - Ajustar cola de prioridad para cumplir la consigna de igual orden de criticidad



