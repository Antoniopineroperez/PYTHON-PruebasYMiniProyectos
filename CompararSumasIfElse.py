#Pedimos 3 numeros al usuario
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
num3 = int(input("Introduce el tercer número: "))
#Comprobamos si los numeros elegidos son iguales a la suma de los otros dos
if (num2 + num3 == num1):
    print("El primer número elegido (", num1, ") es la suma entre el segundo y el tercer número (", num2,"y", num3, ")")
elif (num1 + num3 == num2):
    print("El segundo número elegido (", num2, ") es la suma entre el primer y el tercer número (", num1,"y", num3, ")")
elif (num1 + num2 == num3):
     print("El tercer número elegido (", num3, ") es la suma entre el primer y el segundo número (", num1,"y", num2, ")")
else:
    print("Ningun número es igual a la suma entre los otros dos.")