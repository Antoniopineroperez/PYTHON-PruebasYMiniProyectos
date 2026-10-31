#Crear tupla de 3 elementos imprimiendo sus elementos en lineas separadas
print("EJERCICIO 1")
tupla1 = ("Limon", "Lima", "Fresa")
print(tupla1[0])
print(tupla1[1])
print(tupla1[2])

print("-------------------------------------------------")

#Crear una lista de 3 elementos y la modificamos. Igual con la tupla.
print("EJERCICIO 2")
lista1 = [1, 2, 3]
print(lista1, "Lista sin modificar")
tupla2 = (1, 2, 3)
print(tupla2, "Tupla sin modificar")

lista1[0] = 6
print(lista1, "Lista modificada")

print(tupla2)
print("Las tuplas no se pueden modificar")

print("-------------------------------------------------")

#Creamos una tupla de enteros y devolvemos la suma del conjunto
print("EJERCICIO 3")
tupla_suma = (5, 80, 33, 21, 78)
print(tupla_suma)
sumatotal = sum(tupla_suma)
print(sumatotal)

print("-------------------------------------------------")

#Creamos una tupla con strings, despues, creamos otra tupla 
#nueva que contenga el primer caracter de cada string de la primera tupla
print("EJERCICIO 4")

lista = []
tupla_strings = ("Perro", "Gato", "Ninfa")
print(tupla_strings)

for palabra in tupla_strings:
    lista.append(palabra[0])

tupla_letras = tuple(lista)
print(tupla_letras)

print("-------------------------------------------------")

#Creamos una tupla de numeros enteros, después hacemos que el script
#devuelva la multiplicacion de los numeros pares
print("EJERCICIO 5")

tupla_numeros = (1, 14, 60, 55, 58, 101, 123)
resultado = 1

for i in tupla_numeros:
    if i % 2 == 0:
        resultado = resultado * i

print("Tupla normal:\n", tupla_numeros)
print("Resultado de la multiplicacion:\n", resultado)

print("-------------------------------------------------")

#Creamos una tupla de numeros y después, el script debe devolver 
#la tupla en orden descendente

print("EJERCICIO 6")

tupla_normal = (6, 8, 50, 1, 3)
tupla_descendente = tuple(sorted(tupla_normal, reverse = True))

print("Tupla normal", tupla_normal)
print("Tupla orden descendente", tupla_descendente)

print("-------------------------------------------------")

#Creamos una tupla de numeros enteros repetidos, hacemos un script 
#que borre los que esten repetidos

print("EJERCICIO 7")

tupla_repes = (1, 1, 1, 2, 3, 3, 4, 5, 6, 6, 7, 8, 8, 9)
print("Tupla repetidos:\n", tupla_repes)

set_no_repes = set(tupla_repes)
tupla_no_repes = tuple(set_no_repes)
print("Tupla con numeros únicos:\n", tupla_no_repes)

print("-------------------------------------------------")


#Pedimos al usuario un número entero. Creamos una tupla de numeros.
#Si el numero introducido por el usuario se encuentra en la tupla,
#devolvemos el valor True y sino False

print("EJERCICIO 8")

tupla_nums = (1, 32, 65, 88, 89, 60, 2, 12, 18, 25, 29, 101, 109)
user_num = int(input("Introduce un número entero a comprobar:\n"))

if user_num in tupla_nums:
    print("Verdadero")
    print(tupla_nums)
else:
    print("Falso")
    print(tupla_nums)

print("-------------------------------------------------")

#Creamos dos tuplas, después las unimos en una sola

print("EJERCICIO 9")

tupla_uno = ("Hola", 1, "tal", 3)
tupla_dos = ("que", 2, "estas", 4)

print("Tuplas sin fusionar:")
print(tupla_uno, tupla_dos)

tupla_fusion = tuple(zip(tupla_uno, tupla_dos))
print("Tupla fusionada con zip()")
print(tupla_fusion)

tupla_fusion2 = tuple(tupla_uno + tupla_dos)
print("Tupla fusionada con ¨+¨")
print(tupla_fusion2)

print("-------------------------------------------------")

#Creamos una tupla de números enteros, devolvemos 
#el número más alto y más bajo de la tupla.

print("EJERCICIO 10")

tupla_minmax = (4, 60, 23, 22, 21, 8, 100)

print("TUPLA")
print(tupla_minmax)

print("\nEl número más alto de la tupla es:\n", max(tupla_minmax))
print("El número más bajo de la tupla es:\n", min(tupla_minmax))

print("-------------------------------------------------")

#Creamos una tupla de strings. Devolvemos los strings
#más largos y más cortos

print("EJERCICIO 11")

tupla_palabras = ("Perro", "Gato", "Ninfa", "Cocodrilo")
palabra_larga = max(tupla_palabras, key=len)
palabra_corta = min(tupla_palabras, key=len)

print("TUPLA")
print(tupla_palabras)

print("\nLa palabra más larga de la tupla es:\n", palabra_larga)
print("La palabra más corta de la tupla es:\n", palabra_corta)

print("-------------------------------------------------")

#Creamos una tupla y devolvemos su valor pero invertido

print("EJERCICIO 12")

tupla_default = ("Uno", "Dos", "Tres")
tupla_reverse = tuple(reversed(tupla_default))

print("Tupla normal:\n", tupla_default)
print("Tupla revertida:\n", tupla_reverse)

print("-------------------------------------------------")

#Creamos una tupla de tuplas, cada tupla interna debe tener 2 elementos.
#Hacemos que el script nos devuelva una nueva tupla que sus elementos
#sean la suma de los dos elementos de cada tupla interna

print("EJERCICIO 13")

tupla_multi = ((50, 70), (6, 7), (14, 77))
print("Tupla original:\n", tupla_multi)

tupla_resultado = (sum(tupla_multi[0]), sum(tupla_multi[1]), sum(tupla_multi[2]))
print("Tupla final:\n", tupla_resultado)