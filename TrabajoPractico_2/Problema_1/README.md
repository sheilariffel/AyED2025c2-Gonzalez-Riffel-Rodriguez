# 🐍MediCuidado
Modificar el proyecto de Sala de Emergencias para que los pacientes se atiendan según su nivel de riesgo (prioridad médica) y adquirir un segundo criterio si llegan dos pacientes con el mismo riesgo de salud, para ese caso se considera el orden de llegada del paciente.

---
## 🏗Arquitectura General

* La sección de módulos contiene 4 archivos 
   - Archivo cola_prioridad
   <Utilizado para ordenar a los pacientes según el riesgo y el orden de llegada>
   - Archivo monticulobinario
   <Utilizado por la cola de prioridad para realizar funciones especificas, como insertar, eliminar, mover un elemento arriba o abajo.>
   - Archivo paciente
   <Contiene información aleatoria de los pacientes que irán ingresando. Utiliza la clase paciente que contiene funciones que van guardando, nombre, apellido, número de riesgo y descripcion del riesgo.>
* La sección doc contiene el informe del problema en formato PDF
* La sección data contendría graficas, pero en este problema no se utilizaron 
* La sección de test que es para realizar pruebas del problema
* Un main principal donde se encuentra la estructura de la sala de emergencia 
   <Simula la sala de emergencias de un hospital. Cada ciclo (20 veces) llega un paciente nuevo.Cada paciente tiene un nivel de riesgo (prioridad). Se usa una cola de prioridad para decidir quién se atiende primero. Pacientes con mayor riesgo → se atienden antes. Si dos tienen la misma prioridad, se atiende primero el que llegó antes. En el 50% de los turnos se atiende un paciente (se lo saca de la cola). Se muestran los pacientes que quedan en espera.>

## 🙎‍♀️🙎‍♂️Autores

- Gonzalez Maria Jimena
- Riffel Sheila Gabriela
- Rodriguez Maite

---
## Pasos para la realización
1 - Descargar simulación de la sala de emergencia y probarla
2 - Implementar un montículo de mínima
3 - Implementar cola de prioridad que ocupa el montículo de mínima
4 - Integrar la cola de prioridad en la sala de emergencia propuesta por la cátedra
5 - Ajustar cola de prioridad para cumplir la consigna de igual orden de criticidad

Primer criterio -> atender al que tenga menor valor de prioridad, es decir mayor riesgo de salud (En paciente se asigna aleatoriamente el riesgo) 
Segundo critero  -> si vienen dos con el mismo riesgo, considerar un segundo parámetro que es el orden de llegada.

## Orden de complejidad: para inserciones y eliminaciones del montículo

   def insertar(self, k):
        self.listaMonticulo.append(k) -> O (1)
        self.tamanoActual = self.tamanoActual + 1 -> O (1)
        self.infiltArriba(self.tamanoActual) -> O (log n) 

   def eliminarMin(self):
        valorSacado = self.listaMonticulo[1] -> O(1)
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual] -> O(1)
        self.tamanoActual = self.tamanoActual - 1 -> O(1)
        self.listaMonticulo.pop() -> O(1)
        self.infiltAbajo(1) -> O (log n)
        return valorSacado


