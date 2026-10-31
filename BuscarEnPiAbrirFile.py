#BUSCANDO EN PI
#Busca si tu fecha de nacimiento esta en los primeros 10000 digitos de pi 
#(y en que posición. Puedes usar find()).

def buscar_en_pi(archivo, fecha):
    with open(archivo, "r") as file:
        numeros = file.read()
        posicion = numeros.find(fecha)
        return posicion

fecha = input("Introduce tu fecha de nacimiento: (Formato 000000[como si fuera 00/00/00, dd/mm/aa])\n")
archivo = "pi_10000.txt"
resultado = buscar_en_pi(archivo, fecha)
if resultado != -1:
    print(f"Tu fecha de nacimiento `{fecha}´ está dentro del número Pi en la posición {resultado}")
else:
    print(f"Tu fecha de nacimiento `{fecha}´ no está dentro del número Pi.")