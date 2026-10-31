#Preguntar al usuario si el chico o chica y su nombre
nombres_Chicas_A = "EFGHIJKLM"
nombres_Chicos_B = "IJKLMNOPQ"
genero = int(input("Selecciona tu identidad de genero:\n(1/ Hombre -- 2/Mujer -- 3/ NB): "))
nombre = input("Introduce tu nombre: ")
#Mostramos el grupo del usuario dependiendo su genero y su nombre
#CHICAS GRUPO A: E F G H I J K L M
#       GRUPO B: RESTO
#CHICOS GRUPO A: A B C D E F G H / R S T U V W X Y Z
#       GRUPO B: RESTO (I J K L M N O P Q)
if (genero == 1) or (genero == 3): #Hombre o NB
    if nombre[0].upper() in nombres_Chicos_B:
        print("Perteneces al Grupo B,", nombre.title())
    else:
        print("Perteneces al Grupo A,", nombre.title())
elif (genero == 2) or (genero == 3): #Mujer o NB
    if nombre[0].upper() in nombres_Chicas_A:
        print("Perteneces al Grupo A,", nombre.title())
    else:
        print("Perteneces al Grupo B,", nombre.title())
else:
    pass