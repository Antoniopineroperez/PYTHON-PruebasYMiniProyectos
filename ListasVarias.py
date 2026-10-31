#Creamos una lista, después comprobamos que elementos de la lista;
#estan repetidos, los que lo estén, los metemos en otra lista;
#y los borramos de la lista original, despúes imprimimos la lista original
lista_original = [1, 1, 2, 3, 4, 4, 5, 6, 6, 6, 6, 7, 8]
lista_repes = []
lista_unicos = []
for i in lista_original:
    if lista_original.count(i) > 1:
        if i not in lista_repes:
            lista_repes.append(i)
    else:
        lista_unicos.append(i)
print ("LISTA ORIGINAL:\n", lista_original)
print ("RESULTADO ELEMENTOS UNICOS:\n", lista_unicos)
print ("RESULTADO ELEMENTOS REPETIDOS:\n", lista_repes)

#Salto de ejercicio
print ("-----------------------------------------------------------")

#Creamos dos listas y las fusionamos con orden ascendente
lista_a = [1, 2, 3, 70, 64, 13]
lista_b = [5, 80, 81, 67, 169]
lista_fusion = lista_a + lista_b
lista_fusion.sort()
print ("Lista a:\n", lista_a)
print ("Lista b:\n", lista_b)
print ("Lista fusionada(ascendente):\n", lista_fusion)

#Salto de ejercicio
print ("-----------------------------------------------------------")

#Creamos una lista y buscamos el segundo número más alto
lista_aa = [7, 70, 777, 700, 701]
print ("LISTA ORIGINAL:\n", lista_aa)
lista_aa.sort()
print ("LISTA ORDENADA:\n", lista_aa)
print ("El segundo número mas alto de la lista es", lista_aa[-2])

#Salto de ejercicio
print ("-----------------------------------------------------------")

#Creamos una lista numérica, después pedimos al usuario que introduzca un número.
#Mostramos al usuario cuantos números de la lista son mayores que el introducido.
print ("COMPROBAR CUANTOS NÚMEROS DE UNA LISTA SON MAYORES AL INPUT DEL USUARIO")

lista_numeros = [6, 16, 26, 36, 46, 56, 66, 69]
print (lista_numeros)
eleccion_user = int(input("Introduce un número entero:"))
contador = 0

for i in lista_numeros:
    if i > eleccion_user:
        contador = contador + 1
    else:
        continue

print ("Hay", contador, "números mas altos que", eleccion_user)

#Salto de ejercicio
print ("-----------------------------------------------------------")

#Creamos una lista numérica, luego pedimos un número al usuario.
#Hacemos una suma de todos los números de la lista que sean divisibles
#por el número del usuario.
print("SUMAR SOLO LOS NÚMEROS DE UNA LISTA QUE SEAN DIVISIBLES POR EL INPUT DEL USUARIO")

lista_num = [1, 10, 24, 33, 41, 52, 53, 167]
lista_suma = []
num_user = int(input("Introduce un número entero:"))

for i in lista_num:
    if i % num_user == 0:
        lista_suma.append(i)
    else:
        continue

print ("Los números que son divisibles por", num_user, "son:")
print (lista_suma)
total = sum(lista_suma)
print ("La suma total de los números de la lista que son divisibles por", num_user, "es:")
print (total)

#Salto de ejercicio
print ("-----------------------------------------------------------")

#Creamos una lista numérica, pedimos al usuario un número;
#comprobamos el número más alto de la lista y que sea menor al introducido.
print("COMPROBAR NUMERO MAYOR DE UNA LISTA Y MENOR QUE EL INPUT DEL USUARIO")

lista_aaa = [1, 5, 10, 15, 20, 25, 30, 35, 40, 50, 100, 400, 1000]
numero_user = int(input("Introduce un número:"))
num_final = []

for i in lista_aaa:
    if i < numero_user:
        num_final.append(i)

num_final.sort()
print("El número más grande de la lista y menor que", numero_user, "es", num_final[-1])

#Salto de ejercicio
print ("-----------------------------------------------------------")

#Creamos dos listas, comparamos sus elementos y extraemos los que sean iguales
lista_uno = ["platino", "oro", "plata", "bronce"]
lista_dos = ["oro", "platino", "diamante", "esmeralda"]
lista_comunes = []

print (lista_uno)
print (lista_dos)

for i in lista_uno:
    for comun in lista_dos:
        if i == comun:
            lista_comunes.append(i)

print ("Los elementos en comun de las dos listas son:", lista_comunes)

#Salto de ejercicio
print ("-----------------------------------------------------------")

#Contamos las veces que aparece un elemento en una lista
lista_1 = [1, 11, 11, 11, 100, 100, 1, 100, 5, 6, 12, 70]
repes = []
print(lista_1)

for i in lista_1:
    if i not in repes:
        repes.append(i) #con estas lineas 129 y 130, hacemos que muestre el conteo de cada numero en 1 sola linea
        print ("El elemento", i, "aparece", {lista_1.count(i)}, "veces en la lista.")

#Salto de ejercicio
print ("-----------------------------------------------------------")

#Creamos una lista con números positivos y negativos, hacemos un script qu;
#introduzca los positivos en otra lista a parte
listaPYN = [-1, 2, 50, -555, -40, 9]
lista_positivos = []
print (listaPYN)

for i in listaPYN:
    if i > 0:
        lista_positivos.append(i)
    else:
        continue

print ("Esta es la lista de los números positivos de la lista anterior:\n", lista_positivos)

#Salto de ejercicio
print ("-----------------------------------------------------------")

#Creamos una lista de palabras, hacemos un script que almacene el tamaño
#de las palabras de la lista en otra lista
lista_palabras = ["coco", "mango", "chocolate"]
lista_tamaño = []

print (lista_palabras)

for i in lista_palabras:
    lista_tamaño.append(len(i))

print ("RESULTADO:", lista_tamaño)

#Salto de ejercicio
print ("-----------------------------------------------------------")

#Hacemos una lista de palabras, luego creamos un script que copie
#esa lista en mayusculas.
lista_minus = ["coco", "mango", "chocolate"]
lista_mayus = []
print (lista_minus)

for i in lista_minus:
    lista_mayus.append(i.upper())

print ("RESULTADO TRANSFORMACION A MAYUSCULAS:\n", lista_mayus)