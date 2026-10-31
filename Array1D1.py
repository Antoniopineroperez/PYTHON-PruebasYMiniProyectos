#Creamos un array de 8 elementos lleno de 0s
import numpy as np
array1 = np.zeros(8, dtype = np.int64) #dtype es para especificar que 
print(array1, "Array1")                         #el array son solo numeros integrales

#Lo rellenamos del numero 2
array1.fill(2)
print(array1, "Array1")

#Creamos otro array con numeros pares del 1 al 10
array2 = np.arange(0, 11, 2, dtype = np.int64)
print(array2, "Numeros pares del array2 (1 a 10)")

#Sumamos los elementos del array2 con un bucle y con un metodo de
#numpy para compararlos.
sumatotal = 0
for i in array2:
    sumatotal = sumatotal + i
print("La suma total del array2 usando bucles es:", sumatotal)

sumatotal2 = sum(array2)
print("La suma total del array2 usando funciones es:", sumatotal2)

#Revertimos el array2 para que quede en su valor original de 1 a 10
array2_revertido = array2.reshape(-1)#<-----# -1 hace calculo automatico de
array2_revertido = np.arange(1,11)          # filas y columnas del array en 
print(array2_revertido, "Array2 revertido") # base a los datos disponibles

#Comparamos los elementos comunes de los 3 arrays y los mostramos
comunes, = np.intersect1d(np.intersect1d(array1, array2), array2_revertido)
#intersect1d compara los elementos comunes de 2 arrays, como hay 3 arrays, anidamos la funcion
print(comunes)

#Creamos un array lleno de 1s dada la cantidad indicada por el usuario
cifra = int(input("Introduce la cantidad de elementos del array que quieres crear:"))
array_user = np.ones(cifra, dtype = np.int64)
print(array_user, "Array personalizado por input")