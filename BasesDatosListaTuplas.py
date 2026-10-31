#Una compañía tiene dos bases de datos de clientes. 
#La primera base de datos contiene el nombre del cliente, 
#la dirección de correo electrónico y el número de teléfono. 
#La segunda base de datos contiene el nombre del cliente, 
#la dirección y el historial de pedidos. 
#Escribe un programa que tome las dos bases de datos como listas de tuplas 
#y devuelva una nueva lista de tuplas que contenga solo los clientes 
#que aparecen en ambas bases de datos. 
#Los clientes se consideran iguales si tienen el mismo nombre.
base_datos1 = [("Antonio", "antonio@example.com", "666-999-666"),
               ("Paula", "paula@example.com", "123-456-789"),
               ("Jesus", "jesus@example.com", "987-654-321")]
base_datos2 =[("Antonio", "Calle 6", ("Juego1", "Juego2")),
              ("Paula", "Calle 13", ("Libro1", "Libro2")),
              ("Jorge", "Calle 10", ("Libro3", "Libro4"))]
lista_final = []

print("Nuestras bases de datos son\n", base_datos1, "\n", base_datos2)

#Extraemos los clientes comunes que aparecen en ambas bases de datos
nombres_b1 = set([base_datos1[0][0], base_datos1[1][0], base_datos1[2][0]])
nombres_b2 = set([base_datos2[0][0], base_datos2[1][0], base_datos2[2][0]])
nombres_comunes = nombres_b1.intersection(nombres_b2)

#Creamos la lista de tuplas de los datos de los usuarios 
#en común de ambas bases de datos
for nombre1 in base_datos1:
    if nombre1[0] in nombres_comunes:
        for nombre2 in base_datos2:
            if nombre2[0] == nombre1[0]:
                lista_final.append((nombre1[0], nombre1[1], nombre1[2], nombre2[1], nombre2[2]))
                break

print("")
print("Los datos de los clientes en común de ambas bases de datos son:\n", lista_final)