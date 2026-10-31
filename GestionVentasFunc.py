#Crea un programa que permita gestionar las ventas de una tienda. Utiliza una estructura 
#de datos adecuada para almacenar la información de las ventas (por ejemplo, una lista 
#de diccionarios). Implementa dos funciones, una para agregar el producto vendido con su 
#precio y otro para mostrar las ventas de productos con sus respectivos precios.
#(La base de datos puede tener la forma [{“Producto”: producto1, “Precio”: precio1}, 
#{“Producto”: producto2, “Precio”: precio2}…])
ventas = []

def importar_productos_y_precios(producto, precio):
  #Agregamos datos a la lista de diccionarios anterior
  venta = {
    "producto": producto,
    "precio": precio
    }

  ventas.append(venta)

def mostrar_ventas():
  #Bucle para mostrar cada entrada del diccionario
  for venta in ventas:
    print("Producto: ", venta["producto"])
    print("Precio: ", venta["precio"])
    print("-----------------------")


importar_productos_y_precios("Helado", 3.50)
importar_productos_y_precios("Gofre", 4)
importar_productos_y_precios("Gofre con helado", 5.20)
mostrar_ventas()