# ===========================================
# TEST VISUAL DEL ÁRBOL AVL EN TEMPERATURAS_DB
# ===========================================
from modules.temperaturas import Temperaturas_DB
import matplotlib.pyplot as plt
import networkx as nx
from datetime import datetime

# --- Función auxiliar para graficar el árbol AVL ---
def graficar_avl(nodo, G=None, parent=None, pos=None, nivel=0, x=0, dx=1.5):
    """
    Dibuja el árbol AVL recursivamente usando networkx.
    """
    if G is None:
        G = nx.DiGraph()
        pos = {}

    if nodo:
        # Etiqueta del nodo (fecha sin año)
        label = nodo.clave.strftime("%d/%m")
        G.add_node(label)
        pos[label] = (x, -nivel)

        if parent:
            G.add_edge(parent, label)

        # Recursión a hijos izquierdo y derecho
        graficar_avl(nodo.izq, G, label, pos, nivel + 1, x - dx, dx / 2)
        graficar_avl(nodo.der, G, label, pos, nivel + 1, x + dx, dx / 2)

    return G, pos


def test_avl_temperaturas():
    print("🌡️ TEST VISUAL DEL ÁRBOL AVL DE TEMPERATURAS 🌡️\n")

    # Crear la base de datos
    db = Temperaturas_DB()

    # Ruta del archivo de datos
    ruta_archivo = "data/muestras.txt"

    # Cargar los datos
    try:
        db.cargar_desde_archivo(ruta_archivo)
    except FileNotFoundError:
        print(f"❌ No se encontró el archivo '{ruta_archivo}'.")
        return
    except Exception as e:
        print(f"⚠️ Error al cargar el archivo: {e}")
        return

    total = db.cantidad_muestras()
    print(f"📁 Archivo '{ruta_archivo}' cargado correctamente con {total} muestras.\n")

    # Mostrar recorrido inorden
    print("📅 Recorrido inorden (fechas ordenadas cronológicamente):")
    for f, t in db.arbol.obtener_todos():
        print(f"   {f.strftime('%d/%m/%Y')} → {t} °C")

    # Graficar árbol AVL
    print("\n🌳 Generando gráfico del árbol AVL...")
    G, pos = graficar_avl(db.arbol.raiz)
    plt.figure(figsize=(12, 6))
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=2000,
        node_color="#90caf9",
        font_size=10,
        font_weight="bold",
    )
    plt.title(f"Estructura del Árbol AVL con {total} muestras")
    plt.show()

    print("\n✅ Test finalizado. Si el árbol se muestra balanceado visualmente y el recorrido está ordenado, el AVL funciona correctamente.")


if __name__ == "__main__":
    test_avl_temperaturas()
