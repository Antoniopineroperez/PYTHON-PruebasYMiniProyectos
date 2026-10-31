#FACTORIAL
#Implementa una función recursiva llamada factorial que calcule el factorial de
#un número entero positivo. El factorial de un número n se define como el
#producto de todos los números enteros positivos desde 1 hasta n.
#(El factorial de 0 y de 1 es igual a 1)
numero = int(input("Introduce un número positivo: "))

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)
    
print("El resultado de la funcion es: ", factorial(numero))

#POTENCIA
#Implementa una función recursiva llamada potencia que calcule el resultado
#de elevar un número a una potencia dada. Puedes asumir que tanto el
#número como la potencia son enteros no negativos.
num = int(input("Introduce un número positivo: "))
potencia_user = int(input("Introduce un número de potencia: "))

def potencia(num, pot):
    if pot == 0:
        return 1
    else:
        return num * potencia(num, pot - 1)

print("El resultado de la potencia es: ", potencia(num, potencia_user))


#SUMA ELEMENTOS DE UNA LISTA
#Crea una función recursiva llamada suma_lista que calcule la suma de todos
#los elementos de una lista de enteros. Puedes asumir que la lista no está vacía.
lista = [1, 60, 75, 108]

def suma_lista(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + suma_lista(lista[1:])

print(lista)
print("La suma de los números de la lista es: ", suma_lista(lista))

#NUMERO TRIANGULAR
#Crea una función recursiva llamada numero_triangular que calcule el n-ésimo
#número triangular. Un número triangular se obtiene al sumar todos los
#números naturales desde 1 hasta n.
num_trn = int(input("Introduce un número positivo: "))

def numero_triangular(num):
    if num == 1:
        return 1
    else:
        return num + numero_triangular(num - 1)

print("El número triangular es: ", numero_triangular(num_trn))