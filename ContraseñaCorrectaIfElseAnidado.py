#Pedimos al usuario la contraseña correcta
pwd_correcta = "Aguacate1*"
pwd_user = input("Introduce la contraseña: ")
#Comprobamos si la contraseña es correcta, tiene 2 oportunidades
if pwd_user.casefold() == pwd_correcta.casefold():
    print("¡Contraseña correcta!")
    #.casefold() es para comparar el string sin distinguir minusculas de mayusculas
else:
    print("Contraseña incorrecta, 1 intento restante")
    pwd_user = input("Introduce de nuevo la contraseña: ")
    if pwd_user.casefold() == pwd_correcta.casefold():
        print("¡Contraseña correcta!")
    else:
        print("Contraseña incorrecta, número de intentos superado.")
        