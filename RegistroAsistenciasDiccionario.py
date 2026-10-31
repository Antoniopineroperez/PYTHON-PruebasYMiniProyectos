#Eres un profesor y deseas realizar un seguimiento de la asistencia de tus
#estudiantes a lo largo del semestre. Cada estudiante tiene un nombre y
#una lista de fechas en las que asistió a clases. Implementa un programa
#en Python que utilice un diccionario para almacenar la información de las
#asistencias. El programa debe permitir registrar la asistencia de los
#estudiantes, agregar nuevas fechas de asistencia y mostrar la lista de
#estudiantes y las fechas en las que asistieron.
estudiantes = {}

#Pedimos el nombre de los alumnos y sus asistencias y 
#lo implementamos en el diccionario(maximo 3)
es1 = input("Nombre del primer alumno:\n")
date1_1 = input("Fecha de asistencia del primer estudiante (1 de 3)(dd-mm-aa):\n")
date2_1 = input("Fecha de asistencia del primer estudiante (2 de 3)(dd-mm-aa):\n")
date3_1 = input("Fecha de asistencia del primer estudiante (3 de 3)(dd-mm-aa):\n")

es2 = input("Nombre del segundo alumno:\n")
date1_2 = input("Fecha de asistencia del segundo estudiante (1 de 3)(dd-mm-aa):\n")
date2_2 = input("Fecha de asistencia del segundo estudiante (2 de 3)(dd-mm-aa):\n")
date3_2 = input("Fecha de asistencia del segundo estudiante (3 de 3)(dd-mm-aa):\n")

es3 = input("Nombre del tercer alumno:\n")
date1_3 = input("Fecha de asistencia del tercer estudiante (1 de 3)(dd-mm-aa):\n")
date2_3 = input("Fecha de asistencia del tercer estudiante (2 de 3)(dd-mm-aa):\n")
date3_3 = input("Fecha de asistencia del tercer estudiante (3 de 3)(dd-mm-aa):\n")

estudiantes[es1] = [date1_1, date2_1, date3_1]
estudiantes[es2] = [date1_2, date2_2, date3_2]
estudiantes[es3] = [date1_3, date2_3, date3_3]

#Mostramos los datos
print("Datos de las asistencias:")
print("")
for clave, valor in estudiantes.items():
    print("Nombre del estudiante:", clave, "  ", "\nFechas de asistencias:", valor)

#Preguntamos al usuario si quiere añadir alguna fecha y 
#le mostramos los datos finales
print("")
repetir = True
while repetir == True:
    respuesta = input("¿Deseas añadir alguna fecha de asistencia más? Si | No\n")
    if respuesta == "Si":
        print("")
        print("¿A qué estudiante se le asignará la fecha?")
        print(es1, ": (1)  ", es2, ": (2)  ", es3, ": (3)  ")
        eleccion = int(input(""))
        if eleccion == 1:
            print("")
            date4_1 = input("Introduce la nueva fecha de asistencia (dd-mm-aa):\n")
            estudiantes[es1] = [date1_1, date2_1, date3_1, date4_1]
        if eleccion == 2:
            print("")
            date4_2 = input("Introduce la nueva fecha de asistencia (dd-mm-aa):\n")
            estudiantes[es2] = [date1_2, date2_2, date3_2, date4_2]
        if eleccion == 3:
            print("")
            date4_3 = input("Introduce la nueva fecha de asistencia (dd-mm-aa):\n")
            estudiantes[es3] = [date1_3, date2_3, date3_3, date4_3]
    else:
        repetir = False
        print("")
        print("Registro de asistencia final:")
        for clave, valor in estudiantes.items():
            print("Nombre del estudiante:", clave, "  ", "\nFechas de asistencias:", valor)