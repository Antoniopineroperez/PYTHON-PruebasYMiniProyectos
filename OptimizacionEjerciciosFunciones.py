#REFACTORIZACIÓN:
#Revisa los ejercicios del modulo “Python para Principiantes”. ¿Hay algún
#ejercicio que pudiese dividirse en funciones? ¿Y alguno que podría
#optimizarse usando bloques try-except? Si es así reescríbelos usando 
#estas estructuras.

print("OPTIMIZACIÓN CON FUNCION DE EJERCICIO ANTERIOR")
print("Mostrar los 4 ultimos digitos de la tarjeta de credito \n")

#Pedimos al usuario el número de tarjeta de crédito
num_tarjeta = input("Introduce el número de la tarjeta de crédito: (Formato 0000 0000 0000)\n")

#Creamos la funcion para mostrar los números ocultos menos los 4 últimos
def ultimos_4_digitos_tarjeta(num_tarjeta):
    resultado = num_tarjeta[10:14]
    print("")
    print("**** ****", resultado)
    return resultado

ultimos_4_digitos_tarjeta(num_tarjeta)

print("---------------------------------------------------------")


print("OPTIMIZACIÓN CON TRY EXCEPT DE EJERCICIO ANTERIOR")
print("Repetir todas las letras de una palabra de 5 caracteres justos")

#Creamos la funcion para repetir las letras
def repetir_letras(palabra):
    print(palabra[0] + palabra[0] + palabra[1] + palabra[1] + palabra[2] + palabra[2] + palabra[3] + palabra[3] + palabra[4] + palabra[4])

#Pedir al usuario que introduzca 5 caracteres seguidos,
#si no lo hace bien, volvemos a pedirselo.
repetir = True
while repetir == True:
    print("")
    palabra = input("Introduce una palabra de 5 caracteres exactos:\n")
    if palabra.isalpha() and len(palabra) == 5:
        print("")
        repetir_letras(palabra)
        repetir = False
    else:
        print("")
        print("ERROR")
        print("Has introducido un valor incorrecto, solo se admiten letras y que sean 5 letras exactas, intentalo de nuevo.")