import random
from datetime import datetime, timedelta
import os # Para la creación de directorios y manejo de archivos.

# Definición de parámetros de la simulación
TOTAL_DIAS = 2
MIN_ARCHIVOS = 500
MAX_ARCHIVOS = 999

# 1. Script: generate_meteors.py
# Crea entre 500 y 999 archivos de meteoros.
# Cada archivo tiene un timestamp único dentro de 48 horas y algunos valores aleatorios.
# Pasos:
# 1) Definir la ventana de tiempo.
# 2) Generar timestamps únicos.
# 3) Crear los archivos meteor_XXX.txt con los datos.

def generar_datos_simulados(min_filas, max_filas, total_dias):
    """Crea los archivos de meteoros con datos aleatorios y tiempos dentro de una ventana de 48 horas."""

    # Carpeta donde se guardaran los archivos
    carpeta = "meteoros"
    os. makedirs(carpeta, exist_ok=True) # Crea carpeta si no existe

    # Elegir cuántos archivos generar
    num_archivos = random.randint(min_filas, max_filas)

    # Tiempo inicial de la simulacion
    inicio = datetime(2025, 12, 1, 2, 0, 0)
    segundos_totales = total_dias * 24 * 3600

    # crear momentos de tiempo únicos dentro de los 2 dias
    offsets = random.sample(range(segundos_totales), num_archivos)
    offsets.sort()

    for i, s in enumerate(offsets, start=1):
        timestamp = inicio + timedelta(seconds=s)

        fecha = timestamp.strftime("%Y-%m-%d")
        hora = timestamp.strftime("%H:%M:%S")

        duracion = round(random.uniform(0.1, 5.0), 2)
        altura = round(random.uniform(10.0, 90.0), 1)
        azimut = round(random.uniform(0.0, 359.0), 1)

        nombre = f"{carpeta}/meteoro_{i:03d}.txt"
        with open(nombre, "w") as f:
            f.write(f"{fecha}, {hora}, {duracion}, {altura}, {azimut}")

    print(f"Generación completada. Se crearon {num_archivos} archivos.")
    return num_archivos

# Ejecución de la función de generación
archivos_creados = generar_datos_simulados(MIN_ARCHIVOS, MAX_ARCHIVOS, TOTAL_DIAS)
