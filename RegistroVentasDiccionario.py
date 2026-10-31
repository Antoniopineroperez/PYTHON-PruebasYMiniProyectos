#Tienes una tienda y deseas realizar un seguimiento de las 
#ventas diarias de tus productos. Cada producto tiene un nombre
#y una cantidad vendida. Implementa un programa que utilice 
#un diccionario para almacenar la información de las ventas. 
#El programa debe permitir registrar las ventas de productos,
#actualizar la cantidad vendida de un producto existente 
#y calcular el total de ventas diarias.

caja = {}

#Definimos las variables del diccionario de los productos
#mediante los datos que aporte el usuario.
namep1 = input("Introduce el nombre del producto 1:\n")
ventas1 = int(input("Introduce las ventas del producto 1:\n"))

namep2 = input("Introduce el nombre del producto 2:\n")
ventas2 = int(input("Introduce las ventas del producto 2:\n"))

namep3 = input("Introduce el nombre del producto 3:\n")
ventas3 = int(input("Introduce las ventas del producto 3:\n"))

caja = {
    "Producto1": {"nombre": namep1, "ventas": ventas1},
    "Producto2": {"nombre": namep2, "ventas": ventas2},
    "Producto3": {"nombre": namep3, "ventas": ventas3}
}

print("")

#Mostramos el resultado del inventario
print("Tus productos son:")
for clave, valor in caja.items():
    nombre = valor["nombre"]
    ventas = valor["ventas"]
    print(nombre, ",", ventas, "ventas.")

print("")

#Preguntamos al usuario si desea corregir las 
#ventas de algun producto al final del dia.
#Actualizamos su inventario y lo mostramos.

v1 = int(input("¿Cuantos helados más se han vendido hasta el final del dia?\n"))
ventas1 = ventas1 + v1
v2 = int(input("¿Cuantos gofres más se han vendido hasta el final del dia?\n"))
ventas2 = ventas2 + v2
v3 = int(input("¿Cuantas crepes más se han vendido hasta el final del dia?\n"))
ventas3 = ventas3 + v3

print("")

caja = {
    "Producto1": {"nombre": namep1, "ventas": ventas1},
    "Producto2": {"nombre": namep2, "ventas": ventas2},
    "Producto3": {"nombre": namep3, "ventas": ventas3}
}

print("Caja final de hoy:")
for clave, valor in caja.items():
    nombre = valor["nombre"]
    ventas = valor["ventas"]
    print(nombre, ",", ventas, "ventas.")

print("")

#Calculamos el total de las ventas del dia

total_ventas = ventas1 + ventas2 + ventas3

print("El número total de ventas de hoy es:", total_ventas)