#Crear un array 2D con longitud dada por el usuario y lleno de 1s
import numpy as np
#Le pedimos al usuario la dimension del array
cifra = int(input("Introduce el número de filas del array: "))
cifra2 = int(input("Introduce el número de columnas del array: "))
#Creamos el array lleno de 1s con los datos recibidos
array_2d = np.ones((cifra, cifra2), dtype = np.int64)
#Lo mostramos
print("El array 2D creado es:")
print(array_2d)
#Creamos una matriz de identidad con la dimension de nuestro array
matriz_id = np.eye(cifra, cifra2)
print("La matriz creada a partid de la dimensión introducida:")
print(matriz_id)
#Concatenamos ambas estructuras horizontal y verticalmente
concat_horizontal = np.concatenate((array_2d, matriz_id), axis = 1)
print("Concatenación horizontal:")
print(concat_horizontal)

concat_vertical = np.concatenate((array_2d, matriz_id), axis = 0)
print("Concatenación vertical:")
print(concat_vertical)