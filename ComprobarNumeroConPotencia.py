#Pedimos un número y potencia al usuario
num = input("Introduce un número a comprobar: ")
num = int(num)
pot = input("Introduce una potencia para elevar el número anterior: ")
pot = int(pot)
num_final = num ** pot
#Comprobamos que el número resultante es par o impar
if (num_final % 2 == 0):
    print("El número ", num, "elevado a ", pot, "es ", num_final, ", el cual es par.")
else:
    print("El número ", num, "elevado a ", pot, "es ", num_final, ", el cual es impar.")