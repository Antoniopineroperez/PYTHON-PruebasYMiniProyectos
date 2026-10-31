#Imagina que trabajas en una empresa de logística y tu tarea es desarrollar un
#sistema de gestión de inventario. El inventario está representado como una lista
#de productos ordenados por sus códigos. Cada producto se describe como un
#diccionario con las claves 'codigo' y 'cantidad'.
#Tu objetivo es implementar una función recursiva que realice una búsqueda
#binaria en este inventario y devuelva la cantidad disponible para un producto
#específico, dado su código.

inventario = [
    {"nombre": "Memoria RAM", "cantidad": 180, "codigo": "BXFZ12"},
    {"nombre": "Procesador I7", "cantidad": 10, "codigo": "AHJY13"},
    {"nombre": "Tarjeta grafica", "cantidad": 73, "codigo": "APJL11"}
]

repetir = "Si"
while repetir == "Si":
    buscar = input("Introduce el código del producto a buscar:\n")
    for item in inventario:
        for items in inventario:
            if item["codigo"] == buscar:
                print(f"El artículo con código {buscar} es: {item["nombre"]}, quedan {item['cantidad']} unidades disponibles.")
                break

    repetir = input("¿Deseas buscar otro artículo? Si | No\n")
    repetir = repetir.title()