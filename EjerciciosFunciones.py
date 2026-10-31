#1. Define una función llamada "saludar" que tome un parámetro "nombre"
#y muestre un saludo personalizado.
print("EJERCICIO 1")
print("")

def saludar(nombre):
    print("")
    print("Hola,", nombre.title())

nombre = input("Introduce tu nombre:\n")
saludar(nombre)

print("------------------------------------------------------")

#2.Crea una función llamada "suma" que tome dos parámetros "a" y "b" e
#imprima la suma de ambos.
print("EJERCICIO 2")
print("")

def suma(a, b):
    print("")
    print("El resultado de la suma es:", a + b)

num1 = int(input("Introduce el primer numero:\n"))
num2 = int(input("Introduce el segundo numero:\n"))
suma(num1, num2)

print("------------------------------------------------------")

#3. Escribe una función llamada "calcular_area_rectangulo" que tome dos parámetros "base" 
#y "altura" y calcule el área de un rectángulo.
print("EJERCICIO 3")
print("")

def calcular_area_rectangulo(base, altura):
    print("")
    print("El area del rectangulo es de", base * altura, "cm^2")

base = int(input("Introduce la base del rectangulo en cm:\n"))
altura = int(input("Introduce la altura del rectangulo en cm:\n"))
calcular_area_rectangulo(base, altura)

print("------------------------------------------------------")

#4. Define una función llamada "imprimir_lista" que tome una lista como parámetro y la 
#imprima en la consola.
print("EJERCICIO 4")
print("")

def imprimir_lista(lista):
    print(lista)

mi_lista = [1, 2, 3, 4, 55, 666, 777]
imprimir_lista(mi_lista)    

print("------------------------------------------------------")

#5. Crea una función llamada "es_par" que tome un número como parámetro e imprima True 
#si es par, o False si es impar.
print("EJERCICIO 5")
print("")

def es_par(num):
    print("")
    if num % 2 == 0:
        print("True")
    else:
        print("False")

numero = int(input("Introduce un número para comprobar si es par:\n"))
es_par(numero)

print("------------------------------------------------------")

#6. Escribe una función llamada "concatenar_strings" que tome dos parámetros "cadena1" y 
#“cadena2" e imprima la concatenación de ambas cadenas.
print("EJERCICIO 6")
print("")

def concatenar_strings(cadena1, cadena2):
    print("")
    print(cadena1 + " " + cadena2)

frase1 = input("Introduce la primera frase / palabra:\n")
frase2 = input("Introduce la segunda frase / palabra:\n")
print("")
print("Resultado:")
concatenar_strings(frase1, frase2)

print("------------------------------------------------------")

#7. Define una función llamada "obtener_maximo" que tome una lista de números como parámetro 
#y devuelva el número máximo de la lista.
print("EJERCICIO 7")
print("")

def obtener_maximo(list_num):
    print("")
    print("El número más alto de esta lista es el ", max(list_num))

lista_numeros = [9, 70, 564, 2, 654, 13]
obtener_maximo(lista_numeros)

print("------------------------------------------------------")

#8. Crea una función llamada "convertir_fahrenheit_a_celsius" que tome un parámetro 
#"fahrenheit" y devuelva su equivalente en grados Celsius.
print("EJERCICIO 8")
print("")

def convertir_fahrenheit_a_celsius(fahrenheit):
    print("")
    print(fahrenheit, "ºF son ", (fahrenheit - 32) / 1.8, "ºC")

fahren = int(input("Introduce una cifra de fahrenheits a convertir a celsius:\n"))
convertir_fahrenheit_a_celsius(fahren)

print("------------------------------------------------------")

#9. Escribe una función llamada "calcular_edad" que tome dos parámetros: "año_actual" y 
#"año_nacimiento" y calcule la edad de una persona.
print("EJERCICIO 9")
print("")

def calcular_edad(año_actual, año_nacimiento):
    print("")
    print("La edad sería de ", año_actual - año_nacimiento, " años.")

fecha1 = int(input("Introduce el año actual:\n"))
fecha2 = int(input("Introduce el año de nacimiento:\n"))
calcular_edad(fecha1, fecha2)

print("------------------------------------------------------")

#10. Define una función llamada "es_divisible" que tome dos parámetros "num" y "divisor" 
#e imprima True si "num" es divisible por "divisor", o False si no lo es.
print("EJERCICIO 10")
print("")

def es_divisible(num, divisor):
    print("")
    if num % divisor == 0:
        print("True")
    else:
        print("False")

print("Comprobamos si un número es divisible por otro")
print("")
num1_1 = int(input("Introduce un número:\n"))
divisor = int(input("Introduce un número para que sea el divisor:\n"))
es_divisible(num = num1_1, divisor = divisor)

print("------------------------------------------------------")

#11. Crea una función llamada "mostrar_info_persona" que tome tres argumentos de palabra 
#clave: "nombre", "edad" y "ciudad". La función debe imprimir en la consola la información 
#de una persona en un formato legible.
print("EJERCICIO 11")
print("")

def mostrar_info_persona(nombre, edad, ciudad):
    print("")
    print("Nombre: ", nombre)
    print("Edad: ", edad)
    print("Localidad: ", ciudad)

nom = input("Introduce un nombre:\n")
edad = int(input("Introduce la edad:\n"))
ciudad = input("Introduce la localidad:\n")
print("")
print("Datos:")
mostrar_info_persona(nombre = nom, edad = edad, ciudad = ciudad)

print("------------------------------------------------------")

#12. Escribe una función llamada "calcular_promedio" que tome una lista de números como 
#parámetro y calcule el promedio de esos números. Si no se proporciona una lista, debe usar 
#una lista vacía por defecto.
print("EJERCICIO 12")
print("")

def calcular_promedio(list_num = []):
    if len(list_num) == 0:
        print("No se ha proporcionado ningun valor a la lista numérica.")
        print("El resultado es: 0")
    else:
        print("Promedio de la lista numérica: ", sum(list_num) / len(list_num))

calcular_promedio(list_num = [19, 800, 54])

print("------------------------------------------------------")

#13. Crea una función llamada "calcular_potencia" que tome dos parámetros "base" y 
#"exponente", y calcule la potencia de la base elevada al exponente. Utiliza 2 como valor 
#por defecto para el exponente.
print("EJERCICIO 13")
print("")

def calcular_potencia(base, exponente):
    print("")
    print("La potencia de", base, " elevado a", exponente, " es de", base**exponente)

num_base = int(input("Introduce el número base:\n"))
exponente = int(input("Introduce el número al que se va elevar el anterior:\n"))
calcular_potencia(base = num_base, exponente = exponente)

print("------------------------------------------------------")

#14. Define una función llamada "imprimir_info_alumno" que tome un argumento posicional 
#“nombre”(y sin valor por defecto) y varios argumentos de palabra clave: "edad", "curso" 
#y “promedio" (puedes ponerles como valor por defecto None). La función debe imprimir la
#información del alumno en un formato legible.
print("EJERCICIO 14")
print("")

def imprimir_info_alumno(nombre, edad = None, curso = None, promedio = None):
    print("")
    print("Nombre: ", nombre)
    if edad is not None:
        print("Edad: ", edad)
    if curso is not None:
        print("Curso: ", curso)
    if promedio is not None:
        print("Promedio: ", promedio)

edad_antonio = int(input("Introduce tu edad:\n"))
curso = input("Introduce el curso actual:\n")
promedio = float(input("Introduce el promedio de notas:\n"))
imprimir_info_alumno("Antonio", edad_antonio, curso, promedio)

print("------------------------------------------------------")
