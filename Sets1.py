#Creamos un set y borramos uno de los elementos
print("EJERCICIO 14")

set1 = {1, 2, 3, 4 ,5}
print("Set original\n", set1)

set1.remove(5)
print("Set modificado:\n", set1)

print("-------------------------------------------------")

#Creamos un set vacio
print("EJERCICIO 15")

empty_set = set()
print("Esto es un set vacio:\n", empty_set)
print(type(empty_set))

print("-------------------------------------------------")

#Creamos 2 sets, tenemos que encontrar su union, interseccion y diferencia
print("EJERCICIO 16")

set_uno = {1, 2, 3, 4}
set_dos = {4, 5, 6, 7}
print("Estos son los sets:\n", set_uno, set_dos)

print("Esta es su unión:\n", set_uno | set_dos)
print("Esta es su intersección:\n", set_uno & set_dos)
print("Esta es su diferencia:\n", set_uno - set_dos)

print("-------------------------------------------------")

#Creamos 2 sets, ahora hacemos un script que devuelva
#un set con solo los elementos comunes de ambos sets
print("EJERCICIO 17")

set_a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set_b = {1, 4, 5, 7, 9, 10, 20, 90, 100}
print("Sets originales:\n", set_a, set_b)

set_c = set_a & set_b
print("Set de elementos comunes de los sets anteriores:\n", set_c)

print("-------------------------------------------------")

#Devolvemos el valor maximo y minimo de un set de números
print("EJERCICIO 18")

set_nums = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print("Set original:\n", set_nums)

print("Número mayor del set:", max(set_nums))
print("Número menor del set:", min(set_nums))

print("-------------------------------------------------")

#Creamos dos sets, después hacemos que el script nos
#devuelva un set con los elementos unicos de ambos sets
print("EJERCICIO 19")

set_1 = {"Perro", "Piña", "Coco"}
set_2 = {"Coco", "Perro", "Sandia"}
print("Sets originales:\n", set_1, set_2)

set_unicos = set_1 ^ set_2
print("Set de elementos unicos de los sets anteriores:\n", set_unicos)

print("-------------------------------------------------")

#Creamos un set con nombres de colores, luego pedimos al usuario
#que introduzca el nombre de un color y comprobamos si esta en el set
print("EJERCICIO 20")

set_colores = {"Rojo", "Verde", "Morado", "Negro", "Turquesa", "Blanco"}
color_user = input("Introduce un color a comprobar: ")
color_eleccion = color_user.title()

if color_eleccion in set_colores:
    print("El color", color_eleccion, "está en el set!")
else:
    print("El color", color_eleccion, "no está en el set :(")

print("El set original es:\n", set_colores)

print("-------------------------------------------------")

#Creamos dos sets, después hacemos que el script nos devuelva
#un set que contenga los elementos que están en el primer set pero
#no en el segundo
print("EJERCICIO 21")

set_01 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set_02 = {6, 7, 8, 9}
print("Sets originales:\n", set_01, set_02)

set_03 = set_01 - set_02
print("Set de elementos del primer set pero quitando los que estén en el segundo:\n", set_03)

print("-------------------------------------------------")

#Creamos un set de números enteros, luego hacemos un script que
#devuelva el producto de todos los números del set
print("EJERCICIO 22")

set_multi = {2, 6, 9, 10}
print("Set original:\n", set_multi)

resultado = 1

for i in set_multi:
    resultado = resultado * i

print("El resultado de la multiplicación de los números del set es:", resultado)