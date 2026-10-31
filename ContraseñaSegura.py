#Pedimos al usuario que introduzca una contraseña
passwd = input("Introduce una contraseña: ")

#Comprobamos que la contraseña es segura
if ("a" in passwd or "e" in passwd or "i" in passwd or "o" in passwd or "u" in passwd) and ("*" in passwd or "#" in passwd):
    print("Contraseña establecida, nivel alto de seguridad")
else:
    print("La contraseña no es segura")