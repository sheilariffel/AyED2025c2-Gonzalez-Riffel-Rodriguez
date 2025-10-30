import sys
import heapq

# Definición de un vértice (aldea)
class Vertice:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vecinos = {}  # vecino: distancia
        self.distancia = sys.maxsize
        self.predecesor = None

    def agregar_vecino(self, vecino, distancia):
        self.vecinos[vecino] = distancia

# Grafo como colección de vértices
class Grafo:
    def __init__(self):
        self.vertices = {}

    def agregar_vertice(self, nombre):
        v = Vertice(nombre)
        self.vertices[nombre] = v
        return v

    def agregar_arista(self, origen, destino, distancia):
        if origen not in self.vertices:
            self.agregar_vertice(origen)
        if destino not in self.vertices:
            self.agregar_vertice(destino)
        self.vertices[origen].agregar_vecino(self.vertices[destino], distancia)
        self.vertices[destino].agregar_vecino(self.vertices[origen], distancia)

# Prim usando Cola de prioridad (heapq)
def prim(grafo, inicio_nombre):
    inicio = grafo.vertices[inicio_nombre]
    inicio.distancia = 0
    heap = [(0, inicio.nombre, inicio)]  # (distancia, nombre, vertice)
    visitados = set()
    resultado = []

    while heap:
        dist_actual, _, v_actual = heapq.heappop(heap)
        if v_actual.nombre in visitados:
            continue
        visitados.add(v_actual.nombre)
        if v_actual.predecesor:
            resultado.append((v_actual.predecesor.nombre, v_actual.nombre, dist_actual))
        for vecino, d in v_actual.vecinos.items():
            if vecino.nombre not in visitados and d < vecino.distancia:
                vecino.distancia = d
                vecino.predecesor = v_actual
                heapq.heappush(heap, (d, vecino.nombre, vecino))
    return resultado

# Construir red de recepción/envío y distancia por palomar
def construir_red(resultado):
    recibir = {}
    enviar = {}
    dist_recorrida = {}
    for origen, destino, dist in resultado:
        recibir[destino] = origen
        enviar.setdefault(origen, []).append(destino)
        enviar.setdefault(destino, [])
        dist_recorrida[origen] = dist_recorrida.get(origen, 0) + dist
        dist_recorrida.setdefault(destino, 0)
    return recibir, enviar, dist_recorrida

# Leer archivo y construir grafo
def leer_aldeas(archivo):
    grafo = Grafo()
    with open(archivo, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if not linea or linea.count(",") < 2:
                continue
            origen, destino, dist = [x.strip() for x in linea.split(",")]
            grafo.agregar_arista(origen, destino, int(dist))
    return grafo

# Main
def main():
    grafo = leer_aldeas(r"C:\Users\PC\Desktop\Facultad 2025\Algoritmos\Repo\AyED2025c2-Gonzalez-Riffel-Rodriguez\TrabajoPractico_2\Problema_3\data\aldeas.txt")
    resultado = prim(grafo, "Peligros")
    aldeas = sorted(grafo.vertices.keys())
    recibir, enviar, dist_recorrida = construir_red(resultado)

    print(" Lista de aldeas (orden alfabético) ")
    for aldea in aldeas:
        print(aldea)

    print("\n Comunicación más eficiente ")
    for aldea in aldeas:
        if aldea == "Peligros":
            if enviar[aldea]:
                print(f"{aldea}: no recibe, envía a {', '.join(enviar[aldea])}")
            else:
                print(f"{aldea}: no recibe, envía a nadie")
        else:
            if enviar[aldea]:
                print(f"{aldea}: recibe de {recibir[aldea]}, envía a {', '.join(enviar[aldea])}")
            else:
                print(f"{aldea}: recibe de {recibir[aldea]}, envía a nadie")

    print("\n Distancia recorrida por cada palomar")
    for aldea in aldeas:
        print(f"{aldea}: {dist_recorrida[aldea]} leguas")

    total = sum(dist_recorrida.values())
    print(f"\nDistancia total recorrida: {total} leguas")

if __name__ == "__main__":
    main()

