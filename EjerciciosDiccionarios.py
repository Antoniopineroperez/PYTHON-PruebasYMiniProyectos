#Crea un diccionario vacío llamado “mi_diccionario”
print("EJERCICIO 1")

dict_prueba = {}
print(dict_prueba)

print("-----------------------------------------------------")

#Agrega un par clave-valor a "mi_diccionario" donde la clave sea 
#"nombre" y el valor sea tu nombre.
print("EJERCICIO 2")

dict_prueba["nombre"] = "Antonio"
print(dict_prueba)

print("-----------------------------------------------------")

#Accede e imprime el valor asociado con la clave "nombre" 
#en “mi_diccionario".
print("EJERCICIO 3")

print(dict_prueba["nombre"])

print("-----------------------------------------------------")

#Verifica si la clave "edad" existe en "mi_diccionario". 
# Imprime "True" si existe y "False" en caso contrario.
print("EJERCICIO 4")

print("edad" in dict_prueba)

print("-----------------------------------------------------")

#Crea un diccionario llamado "estudiante" con los siguientes 
#pares clave-valor: "nombre" con el nombre del alumno, 
# "edad" con su edad y "materia" con su materia favorita. 
print("EJERCICIO 5")

estudiante = {"nombre" : "Antonio",
              "edad" : "26",
              "materia" : "astrofisica"
              }

print(estudiante)

print("-----------------------------------------------------")

#Actualiza el valor de la clave "edad" en el diccionario "estudiante" 
#para reflejar la edad actual de tu amigo. 
print("EJERCICIO 6")

estudiante["edad"] = 27

print(estudiante)

print("-----------------------------------------------------")

#Elimina el par clave-valor con la clave "materia" 
#del diccionario “estudiante". 
print("EJERCICIO 7")

del estudiante["materia"]
print(estudiante)

print("-----------------------------------------------------")

#Imprime todas las claves en el diccionario “estudiante". 
print("EJERCICIO 8")

print(estudiante.keys())

print("-----------------------------------------------------")

#Crea un diccionario llamado "agenda" con tres entradas: "Juan" 
#con el valor "1234567890", "Joana" con el valor "9876543210" 
#y "Jimena" con el valor “5555555555”. 
print("EJERCICIO 9")

agenda = {"Juan" : "1234567890",
          "Joana" : "9876543210",
          "Jimena" : "5555555555"
          }

print(agenda)

print("-----------------------------------------------------")

#Agrega una nueva entrada al diccionario "agenda" con la clave 
#"Julio" y el valor “9998887777". 
print("EJERCICIO 10")

agenda["Julio"] = "9998887777"

print(agenda)

print("-----------------------------------------------------")

#Imprime el número de entradas (pares clave-valor) en el diccionario “agenda". 
print("EJERCICIO 11")

print(len(agenda))

print("-----------------------------------------------------")

#Crea una lista llamada "claves" que contenga todas las claves 
#del diccionario “agenda". 
print("EJERCICIO 12")

claves = list(agenda.keys())
print(claves)

print("-----------------------------------------------------")

#Verifica si la clave "Juan" existe en el diccionario "agenda". 
#Imprime "True" si existe y "False" en caso contrario.
print("EJERCICIO 13")

if "Juan" in agenda:
    comprobar = True
    print(comprobar)
    print("La clave `Juan´ en el diccionario `agenda´ es de valor:", agenda["Juan"])
else:
    comprobar = False
    print("No existe la clave `Juan´ en este diccionario.")

print("-----------------------------------------------------")

#Elimina la entrada con la clave “Jimena”. 
print("EJERCICIO 14")

del agenda["Jimena"]
print(agenda)

print("-----------------------------------------------------")

#Utiliza un bucle for para iterar sobre todas las claves en el
#diccionario "agenda" e imprime cada par clave-valor en 
#el formato "Nombre: Número”. 
print("EJERCICIO 15")

for name, num in agenda.items():
    print(name, ":", num)

print("-----------------------------------------------------")

#Utiliza el método "get()" para obtener el valor asociado con la
#clave "Juan" en el diccionario "agenda". Si la clave no existe,
#imprime "Clave no encontrada”.
print("EJERCICIO 16")

if "Juan" in agenda:
    print(agenda.get("Juan"))
else:
    print("Clave no encontrada.")

print("-----------------------------------------------------")

#Borra todas las entradas del diccionario “agenda”.
print("EJERCICIO 17")

agenda.clear()
print(agenda)