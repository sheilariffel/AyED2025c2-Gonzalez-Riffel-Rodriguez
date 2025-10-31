# ===========================
#  MÓDULO: temperaturas.py
# ===========================
from datetime import datetime
from modules.avl import ArbolAVL

class Temperaturas_DB:
    def __init__(self):
        self.arbol = ArbolAVL()

    # Convertir string a datetime
    def _parse_fecha(self, fecha_str):
        return datetime.strptime(fecha_str, "%d/%m/%Y")

    # Insertar medición
    def guardar_temperatura(self, temperatura, fecha):
        self.arbol.insertar(self._parse_fecha(fecha), temperatura)

    # Devolver temperatura exacta
    def devolver_temperatura(self, fecha):
        return self.arbol.buscar(self._parse_fecha(fecha))

    # Borrar por fecha
    def borrar_temperatura(self, fecha):
        self.arbol.eliminar(self._parse_fecha(fecha))

    # Cantidad de muestras
    def cantidad_muestras(self):
        return len(self.arbol.obtener_todos())
    
    #Auxiliar
    def _filtrar_rango(self, fecha1, fecha2):
        f1 = self._parse_fecha(fecha1)
        f2 = self._parse_fecha(fecha2)
        return [(f, t) for f, t in self.arbol.obtener_todos() if f1 <= f <= f2]

    # Listar temperaturas entre fechas
    def devolver_temperaturas(self, fecha1, fecha2):
        filtradas = self._filtrar_rango(fecha1, fecha2)
        return [f"{f.strftime('%d/%m/%Y')}: {t} ºC" for f, t in filtradas]

    # Máxima temperatura en rango
    def max_temp_rango(self, fecha1, fecha2):
        valores = [t for _, t in self._filtrar_rango(fecha1, fecha2)]
        return max(valores) if valores else None

    # Mínima temperatura en rango
    def min_temp_rango(self, fecha1, fecha2):
        valores = [t for _, t in self._filtrar_rango(fecha1, fecha2)]
        return min(valores) if valores else None

    # Mín y Máx en rango
    def temp_extremos_rango(self, fecha1, fecha2):
        valores = [t for _, t in self._filtrar_rango(fecha1, fecha2)]
        return (min(valores), max(valores)) if valores else (None, None)

    # Leer archivo de muestras .txt
    def cargar_desde_archivo(self, ruta_archivo):
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                if ";" in linea:
                    fecha, temp = linea.strip().split(";")
                    self.guardar_temperatura(float(temp), fecha)
    


    

    
