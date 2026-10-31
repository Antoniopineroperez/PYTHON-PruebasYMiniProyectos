#Pedimos los datos del usuario
nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
nota = float(input("Introduce tu nota de media: "))
#Comprobamos si puede optar a beca
if (edad >= 17) and (edad <= 21) and (nota >= 8):
    print("¡Enhorabuena", nombre, ", eres apto para solicitar la beca!")
else:
    print("Lo sentimos", nombre, ", no eres apto para solicitar la beca, estos son los motivos:")
    print("REQUISITOS:")
    print("Edad --> entre 17 y 21 años")
    print("Nota media mínima --> 8")
    print("---------------------------")
    print("TUS DATOS:")
    print("Edad --> ", edad)
    print("Nota de media --> ", nota)