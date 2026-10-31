#Tienes a tu disposición un conjunto de discos numerados del 1 al 3 y tres torres
#etiquetadas como A, B y C. La torre A contiene inicialmente todos los discos
#apilados en orden descendente, desde el disco 3 en la parte inferior hasta el
#disco 1 en la parte superior.
#Tu tarea es implementar una solución recursiva para mover todos los discos
#desde la torre A hasta la torre C, siguiendo las reglas clásicas de las Torres de Hanoi:
#1. Puedes mover un disco a una torre adyacente.
#2. Un disco grande nunca puede ir encima de un disco más pequeño.
#3. Solo se puede mover el disco que está en la parte superior de cada torre
#Debes definir una función llamada torres_de_hanoi(discos, origen, destino, medio)
#que, dado el número total de discos y las torres de origen, destino y medio,
#imprima los pasos necesarios para lograr el movimiento de todos los discos
#desde la torre A hasta la torre C.

import time as time

print("|===|===|===| TORRES DE HANOI |===|===|===|")
print("")
print("Reglas:")
print("1. Puedes mover un disco a una torre adyacente.")
print("2. Un disco grande nunca puede ir encima de un disco más pequeño.")
print("3. Solo se puede mover el disco que está en la parte superior de cada torre")
print("")
print("* = disco1, ** = disco2, *** = disco3, - = vacio")
print("")
print("")

def torres_hanoi(disco1, disco2, disco3, origen, medio, destino):
    origen = [disco1, disco2, disco3]
    medio = []
    destino = []
    imprimir_torres(disco1, disco2, disco3, origen, medio, destino)

    print("1: El disco1 debe moverse de la torre A a la torre B")
    origen.remove(disco1)
    medio.append(disco1)
    imprimir_torres(disco1, disco2, disco3, origen, medio, destino)
    print("2: El disco1 debe moverse de la torre B a la torre C")
    medio.remove(disco1)
    destino.append(disco1)
    imprimir_torres(disco1, disco2, disco3, origen, medio, destino)
    print("3: El disco2 debe moverse de la torre A a la torre B")
    origen.remove(disco2)
    medio.append(disco2)
    imprimir_torres(disco1, disco2, disco3, origen, medio, destino)
    print("4: El disco1 debe moverse de la torre C a la torre B")
    destino.remove(disco1)
    medio.append(disco1)
    imprimir_torres(disco1, disco2, disco3, origen, medio, destino)
    print("5: El disco1 debe moverse de la torre B a la torre A")
    medio.remove(disco1)
    origen.append(disco1)
    imprimir_torres(disco1, disco2, disco3, origen, medio, destino)
    print("6: El disco2 debe moverse de la torre B a la torre C")
    medio.remove(disco2)
    destino.append(disco2)
    imprimir_torres(disco1, disco2, disco3, origen, medio, destino)
    print("7: El disco1 debe moverse de la torre A a la torre B")
    origen.remove(disco1)
    medio.append(disco1)
    imprimir_torres(disco1, disco2, disco3, origen, medio, destino)
    print("8: El disco1 debe moverse de la torre B a la torre C")
    medio.remove(disco1)
    destino.append(disco1)
    imprimir_torres(disco1, disco2, disco3, origen, medio, destino)
    print("9: El disco3 debe moverse de la torre A a la torre B")
    origen.remove(disco3)
    medio.append(disco3)
    imprimir_torres(disco1, disco2, disco3, origen, medio, destino)
    print("10: El disco1 debe moverse de la torre C a la torre B")
    destino.remove(disco1)
    medio.append(disco1)
    imprimir_torres(disco1, disco2, disco3, origen, medio, destino)
    print("11: El disco1 debe moverse de la torre B a la torre A")
    medio.remove(disco1)
    origen.append(disco1)
    imprimir_torres(disco1, disco2, disco3, origen, medio, destino)
    print("12: El disco2 debe moverse de la torre C a la torre B")
    destino.remove(disco2)
    medio.append(disco2)
    imprimir_torres(disco1, disco2, disco3, origen, medio, destino)
    print("13: El disco1 debe moverse de la torre A a la torre B")
    origen.remove(disco1)
    medio.append(disco1)
    imprimir_torres(disco1, disco2, disco3, origen, medio, destino)
    print("14: El disco1 debe moverse de la torre B a la torre C")
    medio.remove(disco1)
    destino.append(disco1)
    imprimir_torres(disco1, disco2, disco3, origen, medio, destino)
    print("15: El disco2 debe moverse de la torre B a la torre A")
    medio.remove(disco2)
    origen.append(disco2)
    imprimir_torres(disco1, disco2, disco3, origen, medio, destino)
    print("16: El disco1 debe moverse de la torre C a la torre B")
    destino.remove(disco1)
    medio.append(disco1)
    imprimir_torres(disco1, disco2, disco3, origen, medio, destino)
    print("17: El disco1 debe moverse de la torre B a la torre A")
    medio.remove(disco1)
    origen.append(disco1)
    imprimir_torres(disco1, disco2, disco3, origen, medio, destino)
    print("18: El disco3 debe moverse de la torre B a la torre C")
    medio.remove(disco3)
    destino.append(disco3)
    imprimir_torres(disco1, disco2, disco3, origen, medio, destino)
    print("19: El disco1 debe moverse de la torre A a la torre B")
    origen.remove(disco1)
    medio.append(disco1)
    imprimir_torres(disco1, disco2, disco3, origen, medio, destino)
    print("20: El disco1 debe moverse de la torre B a la torre C")
    medio.remove(disco1)
    destino.append(disco1)
    imprimir_torres(disco1, disco2, disco3, origen, medio, destino)
    print("21: El disco2 debe moverse de la torre A a la torre B")
    origen.remove(disco2)
    medio.append(disco2)
    imprimir_torres(disco1, disco2, disco3, origen, medio, destino)
    print("22: El disco1 debe moverse de la torre C a la torre B")
    destino.remove(disco1)
    medio.append(disco1)
    imprimir_torres(disco1, disco2, disco3, origen, medio, destino)
    print("23: El disco1 debe moverse de la torre B a la torre A")
    medio.remove(disco1)
    origen.append(disco1)
    imprimir_torres(disco1, disco2, disco3, origen, medio, destino)
    print("24: El disco2 debe moverse de la torre B a la torre C")
    medio.remove(disco2)
    destino.append(disco2)
    imprimir_torres(disco1, disco2, disco3, origen, medio, destino)
    print("25: El disco1 debe moverse de la torre A a la torre B")
    origen.remove(disco1)
    medio.append(disco1)
    imprimir_torres(disco1, disco2, disco3, origen, medio, destino)
    print("26: El disco1 debe moverse de la torre B a la torre C")
    medio.remove(disco1)
    destino.append(disco1)
    imprimir_torres(disco1, disco2, disco3, origen, medio, destino)

    print("|===|===|===| FIN |===|===|===|")


def imprimir_torres(disco1, disco2, disco3, origen, medio, destino):
    if disco1 in origen:
        print(" *")
    else:
        print(" -")
    if disco2 in origen:
        print("* *")
    else:
        print("- -")
    if disco3 in origen:
        print("***")
    else:
        print("---")


    if disco1 in medio:
        print(" *")
    else:
        print(" -")
    if disco2 in medio:
        print("* *")
    else:
        print("- -")
    if disco3 in medio:
        print("***")
    else:
        print("---")


    if disco1 in destino:
        print(" *")
    else:
        print(" -")
    if disco2 in destino:
        print("* *")
    else:
        print("- -")
    if disco3 in destino:
        print("***")
    else:
        print("---")

    time.sleep(2)

torres_hanoi("Disco1", "Disco2", "Disco3", "Torre A", "Torre B", "Torre C")