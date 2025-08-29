# *********************************************************************
# HACER UNA COPIA DE ESTE ARCHIVO A LA CARPETA
# CODIGO_ESTUDIANTES
# NO SOBRESCRIBIR ESTE ARCHIVO PARA EVITAR CONFLICTOS DE SINCRONIZACION
# *********************************************************************

# ---------------------------------------------------------------------
#  Ejercicio 1 - Ordenar una lista de listas
# ---------------------------------------------------------------------
"""
Declarar una lista de listas con una matriz de tu proyecto.
Luego generar una función que retorne la lista ordenada por alguna variable numérica.

Clue: usar función sorted combinada con lambda para ordenar ese arreglo
"""
matriz = [
    [1001, "Juan", "Pérez", "Analista", "Migración SAP", "Si"],
    [1002, "María", "Gómez", "Desarrollador", "App Móvil", "No"],
    [1003, "Carlos", "López", "Tester", "Automatización QA", "Si"],
    [1004, "Sofía", "Martínez", "Líder Proyecto", "E-commerce", "Si"]
]

def ordenMatriz(valorColumna,ordenColumna):
    if ordenColumna == 1:
        matrizOrdenada = sorted(matriz, key=lambda x: x[valorColumna - 1])
    else:
        matrizOrdenada = sorted(matriz, key=lambda x: x[valorColumna - 1], reverse=True)
    
    print(matrizOrdenada)
# ---------------------------------------------------------------------
#  Ejercicio 2 - Invertir el orden
# ---------------------------------------------------------------------
"""
Generar una función complementaria, que además de ordenar, 
lo haga de forma ascendente o descendente, según indique el usuario 
"""
def main():
    valorColumna = int(input("Indique que columna desea ordenar. 1-Legajo, 2-Nombre, 3-Apellido, 4-Posicion, 5-Proyecto, 6-Tareas asignadas: "))
    ordenColumna = int(input("¿Desea ordenar en forma ascendente o descendente? 1-Asc- o 2-Desc.: "))
    
    ordenMatriz(valorColumna,ordenColumna)
main()

