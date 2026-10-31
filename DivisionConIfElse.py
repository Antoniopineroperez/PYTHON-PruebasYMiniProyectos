#Pedimos al usuario 2 numeros
num1 = input("Introduce el dividendo: ")
num1 = float(num1)
num2 = input("Introduce el divisor: ")
num2 = float(num2)
#Mostramos la division por pantalla

if (num2 == 0.0):
    print("ERROR: El divisor no puede ser 0")
else:
    division = num1 / num2
    print(num1, "entre", num2, "es", division)