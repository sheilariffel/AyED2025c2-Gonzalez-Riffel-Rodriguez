# 🐍 Juego de cartas: "Guerra" 

Juego de azar para 2 jugadores basado en un mazo estándar de 52 cartas. Cada turno, ambos jugadores revelan su carta superior; el ganador se queda con ambas cartas al final de su mazo. En caso de empate, se inicia una guerra colocando cartas adicionales para desempatar. El juego termina cuando un jugador obtiene todas las cartas o se alcanza un límite de turnos.

## 🏗Arquitectura General 

El proyecto tiene 4 módulos principales:
- carta.py: define la clase Carta con valor, palo y visibilidad, y métodos de comparación.
- listaDoblemente.py: implementa la lista doblemente enlazada usada para almacenar cartas.
- mazo.py: clase Mazo, maneja cartas usando la lista doble y lanza DequeEmptyError si está vacío.
- juego_de_guerra.py: controla la dinámica del juego, turnos, guerras y muestra de la partida.

## 🙎‍♀️🙎‍♀️🙎‍♀️ Autoras 
- Gonzalez Maria Jimena
- Riffel Sheila 
- Rodriguez Maite

