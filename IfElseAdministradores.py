#Establecer los usuarios del sistema
adm1 = "alejandro"
adm2 = "naomi"
adm3 = "sergio"
#Pedir nombre al usuario por pantalla
nombre = input("Introduce tu nombre de usuario: ")
nombre = nombre.replace(".", "")
nombre = nombre.replace("#", "")
#Comprobamos el user y saludamos
if nombre.lower() == adm1:
    print("¡Bienvenido, ", nombre.title(), "! (Admin)")
elif nombre.lower() == adm2:
    print("¡Bienvenida, ", nombre.title(), "! (Admin)")
elif nombre.lower() == adm3:
    print("¡Bienvenido, ", nombre.title(), "! (Admin)")
else:
    print("¡Bienvenidx, ", nombre.title(), "!")