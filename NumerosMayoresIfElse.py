#Pedimos 4 números al usuario
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
num3 = int(input("Introduce el tercer número: "))
num4 = int(input("Introduce el cuarto número: "))
#Mostramos el numero mayor entre los 4
if num1 > num2 and num1 > num3 and num1 > num4:
    print("El número", num1, "es mayor que los demás números introducidos")
elif num2 > num1 and num2 > num3 and num2 > num4:
    print("El número", num2, "es mayor que los demás números introducidos")
elif num3 > num1 and num3 > num2 and num3 > num4:
    print("El número", num3, "es mayor que los demás números introducidos")
else:
    print("El número", num4, "es mayor que los demás números introducidos")