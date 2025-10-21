# 📝Documentación del proyecto
---
# Objetivo del trabajo

Modificar el proyecto de Sala de Emergencias para que los pacientes se atiendan según su nivel de riesgo (prioridad médica) y no por orden de llegada. 
<ADOPTAR un nuevo criterio si varios pacientes poseen el mismo nivel de riesgo.>
<Estructura de datos debe almacenar cualquier tipo de dato, y no ser específica para alojar pacientes (separar implementación de aplicación).>

Fundamentar en el informe, en no más de una página, la estructura seleccionada indicando el orden de complejidad O de inserciones y de eliminaciones en la estructura seleccionada.


# Idea central: tres niveles de riesgo: queremos que siempre se atienda primero el mas grave, con menor numero de riesgo

1 → crítico

2 → moderado

3 → bajo

⚙️Para poder cumplir con esta consigna, se necesita implementar una cola de prioridad (priority queue), también conocida como heap o montículo.

Una cola de prioridad es una estructura que permite insertar elementos con una “prioridad” asociada, y siempre permite extraer (eliminar) el elemento con la mayor prioridad (o menor, según se defina). En este caso, la prioridad será el nivel de riesgo del paciente.

🔸 Inserción: Se agrega un paciente al heap manteniendo la propiedad del orden (menor riesgo = más prioridad) Complejidad: O(log n)

🔸 Eliminación (atender paciente): Se extrae el paciente con mayor prioridad (riesgo más bajo numéricamente).
Complejidad: O(log n)

🔸 Acceso al siguiente paciente: Consultar el elemento con mayor prioridad (sin eliminarlo).
Complejidad: O(1)

# Estructura seleccionada: Cola de Prioridad (Heap)

Para la gestión de pacientes en una sala de emergencias, se seleccionó una cola de prioridad (heap) como estructura de datos. Esta estructura permite almacenar elementos junto con una prioridad asociada, garantizando que la extracción siempre devuelva el elemento de mayor prioridad.

En este caso, la prioridad se asocia al nivel de riesgo clínico del paciente, siendo el valor numérico más bajo el de mayor urgencia (1 = crítico). De esta manera, la cola permite atender primero a los pacientes más graves, independientemente del orden de llegada.

El criterio secundario para desempatar entre pacientes con el mismo nivel de riesgo es el orden de llegada, asegurando un tratamiento justo y reproducible.

Complejidades:

Inserción (push): O(log n)

Eliminación (pop): O(log n)

Acceso al siguiente paciente (peek): O(1)

Estas características hacen que la cola de prioridad sea la opción más eficiente y adecuada para un sistema donde las atenciones deben priorizarse según un criterio de urgencia.


