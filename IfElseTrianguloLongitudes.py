#Pedimos al usuario 3 longitudes
long1 = float(input("Introduce la primera longitud (cm): "))
long2 = float(input("Introduce la segunda longitud (cm): "))
long3 = float(input("Introduce la tercera longitud (cm): "))
#Comprobamos si la suma de 2 de esas longitudes son mayores que uno de los lados
if (long1 + long2 > long3) and (long1 + long3 > long2) and (long2 + long3 > long1):
    print("Las longitudes son adecuadas para crear un triangulo.")
else:
    print("las longitudes no son adecuadas para crear un triangulo.")