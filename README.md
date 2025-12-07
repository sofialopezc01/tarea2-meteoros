# Tarea 2 Recuperativa – Simulación y Análisis de Lluvias de Meteoros
**Curso:** FIS-1220–01 Programación  
**Estudiante:** Sofía Valentina López Catalán  
**Fecha:** 7 de diciembre de 2025

## Descripción
Este repositorio contiene la solución a la Tarea 2 Recuperativa.  
El proyecto genera cientos de archivos de meteoros y luego calcula el intervalo promedio entre los eventos registrados.

## Contenido del repositorio
- `generate_meteors.py` -> Genera entre 500 y 999 archivos con datos de meteoros.  
- `analyze_meteors.py` -> Procesa los archivos generados y calcula el intervalo promedio.  
- `meteoros/` -> Carpeta con los archivos de meteoros comprimidos en un archivo zip. `meteoro_XXX.txt`.  
- `stats-2.txt` -> Archivo con el resultado numérico del análisis.  
- `README.md` -> Este documento.

## Instrucciones de uso
1. Ejecutar el script de generación:
   ```bash
   python generate_meteors.py
