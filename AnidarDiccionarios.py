#Crea un diccionario llamado "productos" que contenga dos entradas. 
#Cada entrada representa un producto y tiene a su vez las claves 
#"nombre" y "precio" con sus respectivos valores. 
#Recorre el diccionario e imprime el nombre y precio de cada producto.

productos = {
    "producto1": {"nombre": "Helado", "precio": 3},
    "producto2": {"nombre": "Gofre", "precio": 4}
}

for clave, valor in productos.items():
    nombre = valor["nombre"]
    precio = valor["precio"]
    print("Producto:", nombre, ",", "Precio:", precio)

print("----------------------------------------------")

#Agrega un nuevo producto al diccionario "productos" utilizando
#una nueva clave y valor. Imprime el diccionario actualizado.

productos["producto3"] = {"nombre": "Crepe", "precio": 4.5}
print(productos)

print("----------------------------------------------")

#Crea un diccionario llamado "equipos" que contenga tres entradas.
#Cada entrada representa un equipo deportivo y tiene las claves 
#"nombre" y "jugadores" con sus respectivos valores. Los valores de 
#"jugadores" deben ser listas con los nombres de los jugadores. 
#Recorre el diccionario e imprime el nombre del equipo y
#la lista de jugadores.

equipos = {
    "Equipo1": {"nombre": "SKT1", "jugadores": ["Antonio", "Miguel", "Emu"]},
    "Equipo2": {"nombre": "FNC", "jugadores": ["Paula", "Jesus", "Laura"]},
    "Equipo3": {"nombre": "KOI", "jugadores": ["Judit", "Alberto", "Claudia"]}
}

for clave, valor in equipos.items():
    nombre = valor["nombre"]
    jugadores = valor["jugadores"]
    print("Nombre de equipo:", nombre, ",", "Nombre de los jugadores:", jugadores)

print("----------------------------------------------")

#Agrega un nuevo equipo al diccionario "equipos" utilizando una 
#nueva clave y valor. La lista de jugadores debe contener al menos 
#tres nombres. Imprime el diccionario actualizado.

equipos["Equipo4"] = {"nombre": "GIANTS", "jugadores": ["Didac", "Andrea", "Daniel"]}

for clave, valor in equipos.items():
    nombre = valor["nombre"]
    jugadores = valor["jugadores"]
    print("Nombre de equipo:", nombre, ",", "Nombre de los jugadores:", jugadores)

print("----------------------------------------------")

#Actualiza la lista de jugadores de uno de los equipos existentes en
#el diccionario "equipos". Agrega un nuevo jugador a la lista. 
#Imprime el diccionario actualizado.

equipos["Equipo1"]["jugadores"].append("Gersio")
print(equipos["Equipo1"])