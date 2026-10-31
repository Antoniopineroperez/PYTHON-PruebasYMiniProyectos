#Creamos la lista
numeros = list(range(1, 11))
print (numeros, "Lista normal")
#Comprobamos los numeros pares de la lista, introducimos los números pares en otra lista;
#le damos la vuelta y la mostramos
num_pares = []
for i in numeros:
    if i % 2 == 0:
        num_pares.append(i)
    else:
        continue
num_pares.reverse()
print (num_pares," Lista de numeros pares invertida")
#Imprimimos el cuadrado de cada número de la lista Numeros
print ("Potencia de cada número de la lista Numeros:")
for i in numeros:
    print (i ** 2)
#Imprimimos el número mas pequeño de la lista
num_menor = numeros[0]
for i in numeros:
    if i < num_menor:
        num_menor = i
    else:
        continue
print ("El numero menor de la lista es", num_menor)
#Imprimimos el número mas grande de la lista
num_mayor = numeros[0]
for i in numeros:
    if i > num_mayor:
        num_mayor = i
    else:
        continue
print ("El numero mayor de la lista es", num_mayor)
#Sumamos los numeros de la lista con bucles
sumatotal = 0
for i in numeros:
    sumatotal = sumatotal + i
print ("BUCLE --> La suma total de los números de la lista es", sumatotal)
#Sumamos los numeros de la lista sin bucles
sumafinal = sum(numeros)
print ("SIN BUCLES --> La suma total de los números de la lista es", sumafinal)
#Buscamos la posicion del número 8 en la lista normal y en la de pares inversa
posicion_uno = numeros.index(8)
print ("La posicion del número 8 en la lista Numeros es", posicion_uno)
posicion_dos = num_pares.index(8)
print ("La posicion del número 8 en la lista Num_pares es", posicion_dos)