# *********************************************************************
# HACER UNA COPIA DE ESTE ARCHIVO A LA CARPETA
# CODIGO_ESTUDIANTES
# NO SOBRESCRIBIR ESTE ARCHIVO PARA EVITAR CONFLICTOS DE SINCRONIZACION
# *********************************************************************


# ---------------------------------------------------------------------
#  Ejercicio 1 - Convertir temperaturas
# ---------------------------------------------------------------------
"""
Dada la lista de temperaturas en °C, obtené una nueva lista
con las temperaturas en °F, redondeadas a 1 decimal.

Clue: fórmula → F = C * 9/5 + 32 y usá round(valor, 1).
"""
tempCelsius = [10, 14, 25, 32, 28, 4]

tempFar = list(map(lambda temperatura: round(temperatura * 9/5 + 32), tempCelsius))
print(tempFar)
# ---------------------------------------------------------------------
#  Ejercicio 2 - Promedio ponderado de notas
# ---------------------------------------------------------------------
"""
Dados dos listados paralelos con notas de parcial y final, 
calculá el promedio ponderado 0.4*parcial + 0.6*final para cada alumno. 
Redondeá a 1 decimal.
"""
parciales = [7, 6, 4, 9, 8, 5, 10]
finales = [8, 9, 5, 10, 7, 6, 9]

promedio = list(map(lambda parcial, final: round(0.4*parcial + 0.6*final, 1), parciales, finales))
print(promedio)

# ---------------------------------------------------------------------
#  Ejercicio 3 - Normalizar los nombres y apellidos de los estudiantes
# ---------------------------------------------------------------------
"""
Se solicita normalizar los nombre y apellidos de los estudiantes, de manera
que todos sus caracteres sean en minúscula, salvo la primer letra.
"""

