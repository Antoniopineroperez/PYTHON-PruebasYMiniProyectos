#Implementa un programa en Python que permita registrar y mantener un seguimiento 
#de los puntajes de un juego. El programa debe permitir a los jugadores ingresar sus nombres 
#y puntajes, almacenarlos en un diccionario y proporcionar funcionalidades para mostrar el 
#puntaje más alto, el promedio de puntajes y la cantidad total de jugadores.
puntuaje = {}

#Pedimos el username y su puntuación
j1 = input("NOMBRE JUGADOR 1:\n")
p1 = int(input("PUNTUACIÓN JUGADOR 1:\n"))
j2 = input("NOMBRE JUGADOR 2:\n")
p2 = int(input("PUNTUACIÓN JUGADOR 2:\n"))

puntuaje[j1] = p1
puntuaje[j2] = p2
print("")

#Mostramos el número de jugadores
print("Nº DE JUGADORES\n", len(puntuaje.keys()))
print("")

#Mostramos la puntuacion más alta
print("PUNTUACIÓN MÁS ALTA:\n", max(puntuaje.values()))
print("")

#Mostramos la media de las puntuaciones
puntos_totales = sum(puntuaje.values())
cantidad_jugadores = len(puntuaje.keys())
media = puntos_totales / cantidad_jugadores
print("PROMEDIO DE PUNTUACIÓN:\n", media)