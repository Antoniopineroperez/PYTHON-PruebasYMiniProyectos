#Crea una clase "Producto" con atributos como nombre, precio y cantidad en
#stock. Luego, crea una clase "Tienda" que contenga una lista de productos
#disponibles y métodos para agregar productos, mostrar el inventario y
#realizar una compra.

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

class Tienda:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def inventario(self):
        for producto in self.productos:
            print(f"{producto.nombre} -- Precio: {producto.precio}€ -- Stock: {producto.stock}")

    def comprar(self, nombre, cantidad):
        for producto in self.productos:
            if producto.nombre == nombre:
                if producto.stock >= cantidad:
                    producto.stock = producto.stock - cantidad
                    print(f"¡Compra realizada!  Total: {producto.precio * cantidad}€")
                else:
                    print("No hay suficiente stock :(")

                return
        print("Producto no encontrado.")


tienda = Tienda()
producto1 = Producto("Tarjeta RAM 8GB", 100, 20)
producto2 = Producto("Tarjeta Grafica Nvidia", 350, 32)

tienda.agregar_producto(producto1)
tienda.agregar_producto(producto2)
print("Inventario de la tienda:")
tienda.inventario()
print("")

tienda.comprar("Tarjeta Grafica Nvidia", 1)
tienda.comprar("Tarjeta RAM 8GB", 2)
tienda.comprar("Procesador", 1)
print("")

print("Inventario de la tienda:")
tienda.inventario()