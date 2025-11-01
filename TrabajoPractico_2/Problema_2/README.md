# 🐍Temperatuas_DB 

Este proyecto implementa un sistema para almacenar y consultar mediciones de temperatura asociadas a fechas específicas.
Las temperaturas se gestionan mediante una clase Temperaturas_DB que utiliza estructuras de datos, como árbol AVL, para permitir operaciones rápidas de búsqueda, inserción y eliminación.

---
## 🏗Arquitectura General

El proyecto tiene dos módulos y un programa principal:

- avl.py: define NodoAVL y ArbolAVL para manejar un árbol AVL balanceado.
  - NodoAVL representa un nodo del árbol con clave (fecha), valor (temperatura), referencias a hijos y altura.
  - ArbolAVL maneja los nodos, permitiendo insertar, buscar, eliminar y recorrer el árbol, manteniéndolo balanceado automáticamente.
- temperaturas.py: Contiene la clase Temperaturas_DB, que usa internamente ArbolAVL. Permite guardar, consultar, borrar y listar temperaturas. Incluye métodos para calcular máximos y mínimos en un rango de fechas. Implementa la carga de datos desde archivo (muestras.txt).
- Programa principal (main.py): crea la base de datos, carga las mediciones y muestra resultados por consola.

Las archivo muestras.txt está disponible en la carpeta [data](./data) del proyecto.

El informe completo está disponible en la carpeta [docs](./docs) del proyecto.

---
## 🙎‍♀️🙎‍♀️🙎‍♀️Autoras

- Gonzalez María Jimena
- Riffel Sheila Gabriela
- Rodriguez Maite

---
