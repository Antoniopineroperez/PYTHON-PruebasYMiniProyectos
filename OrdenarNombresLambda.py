"""Imagina que te encuentras desarrollando una herramienta de procesamiento de
nombres para una aplicación de gestión de contactos. Tienes una lista de
nombres en el formato "Apellido, Nombre", realiza las siguientes tareas:
1. Utiliza la función lambda para transformar una lista de nombres completos al nuevo formato.
2. Filtra la lista para incluir solo los nombres que contienen al menos dos
vocales y tienen una longitud mayor a 10 caracteres."""

nombres = ["Piñero, Antonio", "Martin, Paula", "Vaquero, Jesus", "Moncin, Laura", "Garrido, Miguel", "Ruiz, Ana", "Diaz, Luis"]

#Funcion lambda para cambiar la posicion de apellido y nombre
voltear_nombre = lambda x: f"{x.split(',')[1].strip()} {x.split(',')[0].strip()}"
nombres_invertidos = list(map(voltear_nombre, nombres))

#Filtramos los nombres completos que contengan 2 vocales al menos y 10 caracteres como minimo
vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"

nombres_finales = [nombre for nombre in nombres_invertidos if sum(1 for letra in nombre if letra in vocales) >= 2 and len(nombre) >= 10]

#Mostramos el resultado

print(nombres_finales)