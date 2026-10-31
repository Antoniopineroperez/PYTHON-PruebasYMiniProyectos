#Imagina que eres el gerente de recursos humanos de una empresa y necesitas gestionar 
#la información de los empleados. Cada empleado tiene un nombre, salario y departamento 
#al que pertenece. Implementa un programa en Python que permita agregar nuevos empleados,
#actualizar el salario de un empleado existente, mostrar la lista completa de empleados 
#y calcular el promedio salarial por departamento.
empleados = {
    "Antonio": {"departamento": "desarrolladores", "salario": 1650},
    "Paula": {"departamento": "marketing", "salario": 1600},
    "Jorge": {"departamento": "administracion", "salario": 1400},
}

print("Datos de empleados:")
print(empleados)

#Preguntamos si desea añadir más empleados
continuar = True
while continuar == True:
    print("")
    respuesta = input("¿Desea añadir otro empleado? Si | No\n")
    if respuesta == "Si":
        print("")
        nombre = input("Introduce el nombre del nuevo empleado:\n")
        new_dept = input("Introduce su departamento:\n")
        new_payroll = int(input("Introduce su salario:\n"))
        empleados[nombre] = {"departamento": new_dept, "salario": new_payroll}
        print("")
        print("Datos actualizados de empleados:\n", empleados)
    else:
        continuar = False
        break

#Preguntamos si desea modificar el salario de algun empleado
seguir = True
while seguir == True:

    print("")
    change = input("¿Deseas modificar el salario de algun empleado?: Si | No\n")
    if change == "Si":
        print("")
        print("Elige el empleado: (Introduce el nombre)")

        for clave, valor in enumerate(empleados, start = 1):
            print(clave, valor)

        eleccion = (input(""))
        if eleccion in (empleados):
            nuevo_salario = int(input("Introduce el nuevo salario:\n"))
            empleados[eleccion]["salario"] = nuevo_salario
            print("Datos de los salarios modificados de los empleados", empleados)
    else:
        seguir = False
        break

#Hacemos una media del salario de los empleados
suma_total = 0
for dinero in empleados.values():
    suma_total = suma_total + dinero["salario"]

num_empleados = len(empleados.keys())

media = suma_total / num_empleados
print("")
print("La media salarial de la empresa es de", media)