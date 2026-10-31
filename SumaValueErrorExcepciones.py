#SUMA Y VALUEERROR
#Un problema común al solicitar una entrada numérica ocurre cuando las personas 
#ingresan texto en lugar de números. Cuando intentas convertir la entrada a un entero (int), 
#obtendrás un ValueError. Escribe un programa que solicite dos números. Suma los números 
#y muestra el resultado. Captura el ValueError si alguno de los valores de entrada no es un 
#número e imprime un mensaje de error amigable. Prueba tu programa ingresando dos números y
#luego ingresando texto en lugar de un número. Envuelve tu código del en un bucle while para 
#que el usuario pueda continuar ingresando números incluso si comete un error ingresando 
#texto en lugar de un número.
intentar = True
while intentar == True:
    try: 
        num1 = int(input("Introduce el primer número a sumar: "))
        num2 = int(input("Introduce el segundo número a sumar: "))
        resultado = num1 + num2
        print("El resultado de la suma es: ", resultado)
        intentar = False
    except ValueError:
        print("Error: ¡El dato a introducir debe ser un número!")