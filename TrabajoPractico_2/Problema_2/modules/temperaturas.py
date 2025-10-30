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
        fecha_dt = self._parse_fecha(fecha)
        self.arbol.insertar(fecha_dt, temperatura)

    # Devolver temperatura exacta
    def devolver_temperatura(self, fecha):
        fecha_dt = self._parse_fecha(fecha)
        return self.arbol.buscar(fecha_dt)

    # Borrar por fecha
    def borrar_temperatura(self, fecha):
        fecha_dt = self._parse_fecha(fecha)
        self.arbol.eliminar(fecha_dt)

    # Cantidad de muestras
    def cantidad_muestras(self):
        return len(self.arbol.obtener_todos())

    # Listar temperaturas entre fechas
    def devolver_temperaturas(self, fecha1, fecha2):
        f1 = self._parse_fecha(fecha1)
        f2 = self._parse_fecha(fecha2)
        datos = self.arbol.obtener_todos()
        filtradas = [(f, t) for f, t in datos if f1 <= f <= f2]
        return [f"{f.strftime('%d/%m/%Y')}: {t} ºC" for f, t in filtradas]

    # Máxima temperatura en rango
    def max_temp_rango(self, fecha1, fecha2):
        f1 = self._parse_fecha(fecha1)
        f2 = self._parse_fecha(fecha2)
        datos = self.arbol.obtener_todos()
        valores = [t for f, t in datos if f1 <= f <= f2]
        return max(valores) if valores else None

    # Mínima temperatura en rango
    def min_temp_rango(self, fecha1, fecha2):
        f1 = self._parse_fecha(fecha1)
        f2 = self._parse_fecha(fecha2)
        datos = self.arbol.obtener_todos()
        valores = [t for f, t in datos if f1 <= f <= f2]
        return min(valores) if valores else None

    # Mín y Máx en rango
    def temp_extremos_rango(self, fecha1, fecha2):
        f1 = self._parse_fecha(fecha1)
        f2 = self._parse_fecha(fecha2)
        datos = self.arbol.obtener_todos()
        valores = [t for f, t in datos if f1 <= f <= f2]
        if not valores:
            return None, None
        return min(valores), max(valores)

    # Leer archivo de muestras .txt
    def cargar_desde_archivo(self, ruta_archivo):
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                if ";" in linea:
                    fecha, temp = linea.strip().split(";")
                    self.guardar_temperatura(float(temp), fecha)
