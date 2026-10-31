#NUMERO FAVORITO 
#Escribe un programa que solicite al usuario su número favorito. Utiliza
#json.dump() para almacenar este número en un archivo. Escribe un
#programa separado que lea este valor e imprima el mensaje: 
#"Sé cuál es tu número favorito… Es ____.” Combina ambos programas en un 
#solo archivo (puedes crear tantas funciones como necesites). Si el 
#número ya está almacenado, muestra el número favorito al usuario.
#Si no lo está, solicita al usuario su número favorito y guárdalo en 
#un archivo. Ejecuta el programa al menos dos veces para asegurarte 
#de que funciona correctamente.

#--------------------------------------------------------------------
#Guardamos el numero favorito en un archivo .json
import time as time
import json as json

num_fav = int(input("Introduce tu número favorito para guardarlo:\n"))

with open("NumeroFavorito.json", "w") as archivo:
    json.dump(num_fav, archivo)

#--------------------------------------------------------------------
#Mostramos al usuario su numero favorito que almacenó antes en un archivo .json
repetir = True
while repetir == True:
    try:
        with open("NumeroFavorito.json", "r") as archivo:
            contenido = archivo.read()
            print(f"Tu número favorito es el {contenido}")
            repetir = False
    except FileNotFoundError:
        print("ERROR: El archivo no existe")
        num_fav = int(input("Por favor, introduce de nuevo tu número favorito:\n"))

        print("Creando archivo con tu número favorito...")
        with open("NumeroFavorito.json", "w") as archivo:
            json.dump(num_fav, archivo)

        time.sleep(2)