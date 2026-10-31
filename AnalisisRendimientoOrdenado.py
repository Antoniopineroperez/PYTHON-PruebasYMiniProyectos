"""Imagina que trabajas en una empresa internacional con equipos distribuidos en
diferentes países. Cada equipo tiene una lista de empleados, representados
como diccionarios, con información sobre el nombre, la edad y el rendimiento
en proyectos recientes.
Tu tarea es organizar una lista consolidada de todos los empleados de la
empresa. La organización debe seguir ciertas reglas:
1. Los empleados se deben ordenar por el rendimiento en proyectos recientes
de forma descendente.
2. Para aquellos con el mismo rendimiento, se deben ordenar por edad de
forma ascendente. Además, deseas agrupar a los empleados por país para
un análisis más efectivo. Utiliza funciones lambda."""

empleados = [
    {"nombre": "Antonio", "edad": 27, "rendimiento": 71, "pais": "España"},
    {"nombre": "Bjorn", "edad": 35, "rendimiento": 62, "pais": "Noruega"},
    {"nombre": "Paula", "edad": 31, "rendimiento": 95, "pais": "España"},
    {"nombre": "David", "edad": 42, "rendimiento": 88, "pais": "USA"},
    {"nombre": "Aurora", "edad": 33, "rendimiento": 90, "pais": "Noruega"},
    {"nombre": "Iker", "edad": 31, "rendimiento": 74, "pais": "España"},
    {"nombre": "Jaden", "edad": 25, "rendimiento": 91, "pais": "USA"},
    {"nombre": "Thomas", "edad": 40, "rendimiento": 90, "pais": "USA"},
    {"nombre": "Saavik", "edad": 30, "rendimiento": 80, "pais": "Noruega"},
]

def ordenar_empleados(empleados):
    empleados_ordenados = sorted(empleados, key=lambda empleado: empleado["edad"])
    empleados_ordenados = sorted(empleados_ordenados, key=lambda empleado: empleado["rendimiento"], reverse=True)

    for i in empleados_ordenados:
        print(i)

    return empleados_ordenados

def agrupar_por_pais(empleados_ordenados):
    rendimiento_españa = []
    rendimiento_usa = []
    rendimiento_noruega = []

    clave_esp = "pais"
    valor_esp = "España"
    rendimiento_españa = [p for p in empleados_ordenados if p.get(clave_esp) == valor_esp]
    for esp in rendimiento_españa:
        print(esp)

    print("")
    clave_nor = "pais"
    valor_nor = "Noruega"
    rendimiento_noruega = [p for p in empleados_ordenados if p.get(clave_nor) == valor_nor]
    for nor in rendimiento_noruega:
        print(nor)

    print("")
    clave_usa = "pais"
    valor_usa = "USA"
    rendimiento_usa = [p for p in empleados_ordenados if p.get(clave_usa) == valor_usa]
    for usa in rendimiento_usa:
        print(usa)

    return rendimiento_usa, rendimiento_noruega, rendimiento_españa


print("RENDIMIENTO GENERAL DE PLANTILLA:")
empleados_ordenados = ordenar_empleados(empleados)
print("")
print("RENDIMIENTO POR PAIS")
agrupar_por_pais(empleados_ordenados)
print("")