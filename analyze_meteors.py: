# 2. Script: analyze_meteors.py
# Lee los archivos, obtiene los timestamps, los ordena
# y calcula los intervalos entre eventos. Luego escribe
# el promedio de esos intervalos en stats.txt.

def calcular_intervalo_promedio(num_archivos, carpeta="meteoros"):
    """Lee los archivos, calcula los intervalos entre meteoros y guarda el promedio."""

    eventos = []

    # Leer cada archivo y obtener sus timestamps
    for i in range(1, num_archivos + 1):
        nombre = f"{carpeta}/meteoro_{i:03d}.txt"
        try:
            with open(nombre, 'r') as f:
                linea = f.readline().strip()
                partes = linea.split(',')      # Dividir la linea por coma

                # Extraer fecha y hora
                fecha_str = partes[0].strip()
                hora_str = partes[1].strip()

                # Reconstruir el string 'YYYY-MM-DD HH:MM:SS'
                fecha_hora_str = f"{fecha_str} {hora_str}"

                # Convertir el string a un objeto datetime
                timestmap = datetime.strptime(fecha_hora_str, "%Y-%m-%d %H:%M:%S")
                eventos.append(timestmap)       # Guarda el timestramp para ordenarlo y restarlo

        except FileNotFoundError:
         continue      # si falta un archivo se ignora

    # Ordenar los eventos cronológicamente
    eventos.sort()

    # Calcular diferencias entre eventos consecutivos
    intervalos = []
    for i in range(1, len(eventos)):
        diferencia = (eventos[i] - eventos[i - 1])
        segundos = diferencia.total_seconds()  # Corrected from total_segundos() to total_seconds()
        intervalos.append(segundos)

    # Promedio de intervalos
    if intervalos:
      promedio_segundos = sum(intervalos) / len(intervalos)

    else:
        promedio_segundos = 0.0

    # Cálculo del promedio final y guardado en stats.txt
    with open("stats.txt", "w") as f:
        f.write(f"Numero total de eventos: {len(eventos)}\n")
        f.write(f"Tiempo promedio entre meteoros: {promedio_segundos:.2f} segundos\n")

    return promedio_segundos

promedio_final = calcular_intervalo_promedio(archivos_creados)
