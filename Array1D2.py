#Creamos un array de 15 elementos del 1 al 100 aleatoriamente
import numpy as np
array_random = np.random.randint(1, 100, size = 15, dtype = np.int64) #funcion de nums aleatorios
print(array_random)

#Multiplicamos los elementos del array con un bucle y con funciones para compararlos
resultado = 1
for i in array_random:
    resultado = resultado * i
print("El resultado de la multiplicacion de los elementos del array usando bucles es:", resultado)

resultado2 = np.prod(array_random)
print("El resultado de la multiplicacion de los elementos del array usando funciones es:", resultado2)

#Creamos otro array semejante al anterior pero con números decimales entre 0 y 1
array_random2 = np.random.random(15)
print(array_random2)

#Sumamos los elementos de los dos arrays, elemento por elemento
#Usaremos bucles, operadores y funciones
print("--------------------------------------------------")
print("ARRAYS:")
print(array_random)
print(array_random2)
sumatotal = 0
for i in array_random:
    sumatotal = sumatotal + i
    for a in array_random2:
        sumatotal = sumatotal + a
print("El resultado de la suma de todos los elementos de ambos arrays usando bucles es:", sumatotal)

print("--------------------------------------------------")

suma_operadores = array_random + array_random2
print("El resultado de la suma de todos los elementos de ambos arrays usando operadores es:", suma_operadores)

print("--------------------------------------------------")

suma_numpy = np.add(array_random, array_random2)
print("El resultado de la suma de todos los elementos de ambos arrays usando funciones numpy es:", suma_numpy)

#Ahora hacemos lo mismo pero con restas
print("--------------------------------------------------")
print("ARRAYS:")
print(array_random)
print(array_random2)
restatotal = 0
for i in array_random:
    restatotal = i - restatotal
    for a in array_random2:
        restatotal = a - restatotal
print("El resultado de la resta de todos los elementos de ambos arrays usando bucles es:", restatotal)

print("--------------------------------------------------")

resta_operadores = array_random - array_random2
print("El resultado de la resta de todos los elementos de ambos arrays usando operadores es:", resta_operadores)

print("--------------------------------------------------")

resta_numpy = np.subtract(array_random, array_random2)
print("El resultado de la resta de todos los elementos de ambos arrays usando funciones numpy es:", resta_numpy)

#Ahora hacemos lo mismo pero con multiplicaciones
print("--------------------------------------------------")
print("ARRAYS:")
print(array_random)
print(array_random2)
multitotal = 1
for i in array_random:
    multitotal = i * multitotal
    for a in array_random2:
        multitotal = a * multitotal
print("El resultado de la multiplicacion de todos los elementos de ambos arrays usando bucles es:", multitotal)

print("--------------------------------------------------")

multi_operadores = array_random * array_random2
print("El resultado de la multiplicacion de todos los elementos de ambos arrays usando operadores es:", multi_operadores)

print("--------------------------------------------------")

multi_numpy = np.multiply(array_random, array_random2)
print("El resultado de la multiplicacion de todos los elementos de ambos arrays usando funciones numpy es:", multi_numpy)

#Buscamos el valor mas alto del primer array creado
print("--------------------------------------------------")
print(array_random)
valor_alto = max(array_random)
print("El valor mas alto del primer array es:", valor_alto)

#Calculamos la media, mediana y deviacion estandar de ambos arrays
print("--------------------------------------------------")
print("Media ARRAY 1")
media1 = np.mean(array_random)
print(media1)

print("Media ARRAY 2")
media2 = np.mean(array_random2)
print(media2)

print("Mediana ARRAY 1")
median1 = np.median(array_random)
print(median1)

print("Mediana ARRAY 2")
median2 = np.median(array_random2)
print(median2)

print("Desviacion estandar ARRAY 1")
ds1 = np.std(array_random)
print(ds1)

print("Desviacion estandar ARRAY 2")
ds2 = np.std(array_random2)
print(ds2)