#CLASE PERSONA
#Define una clase Persona con atributos como nombre, edad y profesión.
#Luego, crea varios objetos de esta clase y muestra su información.

class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion

persona1 = Persona("Antonio", 27, "Desarrollador Web")
persona2 = Persona("Paula", 27, "Perfumista")

print(persona1.nombre, persona1.edad, persona1.profesion)
print(persona2.nombre, persona2.edad, persona2.profesion)
print("")
print("--------------------------------------------------------")

#CALCULADORA BÁSICA
#Crea una clase llamada "Calculadora" con métodos para sumar, restar,
#multiplicar y dividir. Crea objetos de esta clase y realiza 
#algunas operaciones básicas.

class Calculadora:
    def sumar(self, a, b):
        return a + b
    def restar(self, a, b):
        return a - b
    def multiplicar(self, a, b):
        return a * b
    def dividir(self, a, b):
        return a / b
        
calculadora = Calculadora()

repetir = True
while repetir == True:
    eleccion = int(input("Elige qué operacion hacer: (Introduce el número)\n""1) Sumar\t2)Restar\t3)Multiplicar\t4)Dividir\n"))
    if eleccion == 1:
        num1 = int(input("Elige el primer número:\n"))
        num2 = int(input("Elige el segundo número:\n"))
        print("Resultado: ", calculadora.sumar(num1, num2))
    if eleccion == 2:
        num1 = int(input("Elige el primer número:\n"))
        num2 = int(input("Elige el segundo número:\n"))
        print("Resultado: ", calculadora.restar(num1, num2))
    if eleccion == 3:
        num1 = int(input("Elige el primer número:\n"))
        num2 = int(input("Elige el segundo número:\n"))
        print("Resultado: ", calculadora.multiplicar(num1, num2))
    if eleccion == 4:
        num1 = int(input("Elige el primer número:\n"))
        num2 = int(input("Elige el segundo número:\n"))
        print("Resultado: ", calculadora.dividir(num1, num2))

    print("")
    preguntar = input("¿Quieres hacer algún otro calculo?  Si | No\n")
    preguntar = preguntar.title()
    if preguntar == "Si":
        repetir = True
    else:
        repetir = False

print("")
print("--------------------------------------------------------")
print("")

#LIBRO
#Crea una clase "Libro" con atributos como título, autor y año de publicación.
#Luego, crea varios objetos Libro y muestra su información.

class Libro:
    def __init__(self, titulo, autor, año):
        self.titulo = titulo
        self.autor = autor
        self.año = año

libro1 = Libro("Juego de Tronos", "George R. R. Martin", 1996)
libro2 = Libro("Silmarillion", "J. R. R. Tolkien", 1977)
libro3 = Libro("El señor de los anillos", "J. R. R. Tolkien", 1954)

print(libro1.titulo, " ", libro1.autor, " ", libro1.año)
print(libro2.titulo, " ", libro2.autor, " ", libro2.año)
print(libro3.titulo, " ", libro3.autor, " ", libro3.año)

print("")
print("--------------------------------------------------------")
print("")

#RECTÁNGULO
#Crea una clase "Rectangulo" con atributos de longitud y ancho. Implementa
#un método para calcular el área y el perímetro del rectángulo.

class Rectangulo:
    def __init__(self, ancho, altura):
        self.ancho = ancho
        self.altura = altura
    def calc_area(self):
        area = self.ancho * self.altura
        return area
    def calc_perimetro(self):
        return 2 * (self.ancho + self.altura)

ancho = int(input("Introduce el ancho del rectangulo:\n"))
altura = int(input("Introduce la altura del rectangulo:\n"))
rectangulo1 = Rectangulo(ancho, altura)

print("")
print("El area del rectangulo es de", rectangulo1.calc_area(), "cm2.")
print("El perímetro del rectangulo es de", rectangulo1.calc_perimetro(), "cm2.")

print("")
print("--------------------------------------------------------")
print("")

#DADO
#Crea una clase "Dado" que simule el lanzamiento de un dado de 6 caras.
#Implementa un método para lanzar el dado y mostrar el resultado
#(quizás te convenga usar el modulo random).

import random
class Dado:
    def lanzar_dado(self):
        lanzamiento = random.randint(1, 20)
        return lanzamiento

dado1 = Dado()
dado2 = Dado()

resultado1 = dado1.lanzar_dado()
resultado2 = dado2.lanzar_dado()

print("Resultado del dado 1:", resultado1)
print("Resultado del dado 2:", resultado2)

print("")
print("--------------------------------------------------------")
print("")


#COCHE
#Crea una clase "Coche" con atributos como marca, modelo y año.
#Implementa un método para encender el coche y otro para apagarlo 
#(puedes simular el encendido y apagado con una variable booleana).

class Coche:
    def __init__(self, marca, color, año):
        self.marca = marca
        self.color = color
        self.año = año
        self.encendido = False
    def encender(self):
        self.encendido = True
    def apagar(self):
        self.encendido = False

mi_coche = Coche("Hyundai", "Red Dragon", 2023)

mi_coche.encender()
print("El coche está encendido:", mi_coche.encendido)
mi_coche.apagar()
print("El coche está encendido:", mi_coche.encendido)
print("El coche está apagado")

print("")
print("--------------------------------------------------------")
print("")
