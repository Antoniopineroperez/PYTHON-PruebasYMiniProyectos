#Crea un programa que valide un formulario de registro. Crea una función llamada 
#validar_formulario que reciba diferentes campos de un formulario 
#(nombre, correo electrónico y número de teléfono) y verifique si los valores ingresados 
#cumplen con los requisitos especificados, siendo estos:
#1. Que el nombre tenga una longitud minima de 3 caracteres
#2. Que el teléfono este conformado por dígitos y tenga una longitud de 9 caracteres
#3. Que el email contenga un “@“ y un “.”
def validar_formulario(nombre, correo, tlf):
    print("")
    if len(nombre) < 3:
        return False
    if "@" and "." not in correo:
        return False
    if type(tlf) != int:
        return False
    tlf = str(tlf)
    if len(tlf) != 9:
        return False

    return True
            
nombre = input("Introduce tu nombre:\n")
correo = input("Introduce tu correo electronico:\n")
telefono = int(input("Introduce tu número de telefono:\n"))

valido = validar_formulario(nombre, correo, telefono)

if valido:
    print("El formulario es válido.")
else:
    print("El formulario no es válido.")