# ===========================
#  MAIN.PY – Prueba completa usando muestras.txt
# ===========================

from modules.temperaturas import Temperaturas_DB

def main():
    # Crear base de datos
    db = Temperaturas_DB()

    # 1️⃣ Cargar datos desde el archivo
    ruta_archivo = "data/muestras.txt"
    db.cargar_desde_archivo(ruta_archivo)
    print(f"Muestras cargadas desde {ruta_archivo}: {db.cantidad_muestras()}")

    # 2️⃣ Consultar una temperatura existente
    # Tomamos la primera fecha del archivo (primer registro en orden)
    todas_las_temp = db.devolver_temperaturas("01/01/2000", "31/12/2100")
    if todas_las_temp:
        fecha_consulta = todas_las_temp[0].split(":")[0]  # extraer fecha del string
        temp = db.devolver_temperatura(fecha_consulta)
        print(f"\nTemperatura registrada el {fecha_consulta}: {temp} ºC")
    else:
        print("\nNo hay registros en la base de datos.")

    # 3️⃣ Borrar una temperatura (ejemplo)
    if todas_las_temp:
        fecha_borrar = todas_las_temp[1].split(":")[0] if len(todas_las_temp) > 1 else fecha_consulta
        db.borrar_temperatura(fecha_borrar)
        print(f"\nSe borró la temperatura del {fecha_borrar}")
        print(f"Cantidad de muestras actual: {db.cantidad_muestras()}")

    # 4️⃣ Listar todas las temperaturas
    print("\nListado completo de temperaturas:")
    for entrada in db.devolver_temperaturas("01/01/2000", "31/12/2100"):
        print(entrada)

    # 5️⃣ Máxima y mínima temperatura en un rango
    fecha_inicio = "01/01/2023"
    fecha_fin = "31/12/2023"
    min_temp = db.min_temp_rango(fecha_inicio, fecha_fin)
    max_temp = db.max_temp_rango(fecha_inicio, fecha_fin)
    print(f"\nTemperatura mínima entre {fecha_inicio} y {fecha_fin}: {min_temp} ºC")
    print(f"Temperatura máxima entre {fecha_inicio} y {fecha_fin}: {max_temp} ºC")

    # 6️⃣ Mínimo y máximo combinados
    min_ext, max_ext = db.temp_extremos_rango(fecha_inicio, fecha_fin)
    print(f"\nExtremos del rango: mínimo = {min_ext} ºC, máximo = {max_ext} ºC")

if __name__ == "__main__":
    main()
