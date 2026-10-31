#Pedir tiempos de los atletas
minutos_hannah = input("Introduce los minutos de Hannah Neise:")
segundos_hannah = input("Introduce los segundos de Hannah Neise:")
centesimas_hannah = input("Introduce las centésimas de Hannah Neise:")

minutos_jackie = input("Introduce los minutos de Jackie Narracott:")
segundos_jackie = input("Introduce los segundos de Jackie Narracott:")
centesimas_jackie = input("Introduce las centésimas de Jackie Narracott:")

minutos_kimberly = input("Introduce los minutos de Kimberly Bos:")
segundos_kimberly = input("Introduce los segundos de Kimberly Bos:")
centesimas_kimberly = input("Introduce las centésimas de Kimberly Bos:")
#Convertir los tiempos a segundos
tiempo_hannah = float(minutos_hannah) * 60 + float(segundos_hannah) + float(centesimas_hannah) * 0.01

tiempo_jackie = float(minutos_jackie) * 60 + float(segundos_jackie) + float(centesimas_jackie) * 0.01

tiempo_kimberly = float(minutos_kimberly) * 60 + float(segundos_kimberly) + float(centesimas_kimberly) * 0.01
#Calculamos la velocidad media de cada jugador y lo mostramos por pantalla
velocidad_hannah = 100 / tiempo_hannah

velocidad_jackie = 100 / tiempo_jackie

velocidad_kimberly = 100 / tiempo_kimberly


print("Velocidad media de Hannah Neise: ", velocidad_hannah, "m/s")

print("Velocidad media de Jackie Narracott: ", velocidad_jackie, "m/s")

print("Velocidad media de Kimberly Bos: ", velocidad_kimberly, "m/s")