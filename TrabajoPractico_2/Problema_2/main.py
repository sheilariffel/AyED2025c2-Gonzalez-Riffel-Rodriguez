#PROGRAMA PRINCIPAL

from modules.temperaturas import Temperaturas_DB 


db = Temperaturas_DB()

# Ruta del archivo de muestras
archivo_muestras = "data/muestras.txt"

db.cargar_desde_archivo(archivo_muestras)

# Mostrar cantidad de muestras
print("Cantidad de muestras:", db.cantidad_muestras())

# Devolver temperatura de una fecha específica
fecha_consulta = "09/04/2025"
print(f"Temperatura en {fecha_consulta}:", db.devolver_temperatura(fecha_consulta))

# Temperatura máxima y mínima en un rango
fecha1 = "01/01/2025"
fecha2 = "30/04/2025"
print(f"Temperatura máxima entre {fecha1} y {fecha2}:", db.max_temp_rango(fecha1, fecha2))
print(f"Temperatura mínima entre {fecha1} y {fecha2}:", db.min_temp_rango(fecha1, fecha2))
print(f"Temperaturas extremas entre {fecha1} y {fecha2}:", db.temp_extremos_rango(fecha1, fecha2))

#Devolver todas las temperaturas en un rango
print(f"Listado de temperaturas entre {fecha1} y {fecha2}:")
for registro in db.devolver_temperaturas(fecha1, fecha2):
    print(registro)

fecha_borrar = "04/03/2025"

print(f"Borrando temperatura de {fecha_borrar}...")
db.borrar_temperatura(fecha_borrar)
print("Cantidad de muestras después de borrar:", db.cantidad_muestras())
