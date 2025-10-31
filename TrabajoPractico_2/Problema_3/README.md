# 🐍Palomas mensajeras

Breve descripción del proyecto:
El proyecto trata sobre  encontrar la forma más eficiente de llevar un mensaje desde una aldea a todas las demás, donde cada aldea reciba solamente una vez la noticia. Cada aldea, al recibir la noticia, puede replicarla y enviarla a tantas aldeas vecinas como quiera.
---
## 🏗Arquitectura General

El codigo primero lee el archivo con las aldeas y sus distancias, armando un mapa de todas las conexiones posibles.
Después usa un método para encontrar la forma más corta de unir todas las aldeas. Empieza desde "Peligros" y va agregando los caminos más cercanos, evitando dar vueltas innecesarias.
Luego organiza el resultado para saber claramente: cada aldea recibe mensajes de quién y a quiénes debe reenviarlos.
Finalmente muestra toda la información: el listado de aldeas, cómo se comunican entre sí y cuánta distancia se recorre en total.

El informe completo está disponible en la carpeta [docs](./docs) del proyecto.

---
## 🙎‍♀️🙎‍♂️Autores

- Gonzalez María Jimena
- Riffel Sheila Gabriela
- Rodriguez Maite

---

> **Consejo**: Mantén el README **actualizado** conforme evoluciona el proyecto, y elimina (o añade) secciones según necesites. Esta plantilla es sólo un punto de partida general.
