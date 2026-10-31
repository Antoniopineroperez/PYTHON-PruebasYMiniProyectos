"""Crea un script que solicite una contraseña, analice si es segura y si no lo es sugiera 
una nueva contraseña. Para ello puedes crear un script validador.py que contenga una funcion
validar_contrasena que reciba una cadena y verifique si cumple con los requisitos mínimos de 
una contraseña segura (por ejemplo, longitud mínima, presencia de letras mayúsculas, letras
minúsculas, números y caracteres especiales). La función debe devolver un valor booleano que 
indique si la contraseña es válida o no. Por otro lado puedes crear otro script creador.py 
con una función llamada generar_contrasena que genere contraseñas seguras de forma aleatoria. 
La función debe permitir especificar la longitud de la contraseña y qué tipos de caracteres 
deben incluirse (por ejemplo, letras mayúsculas, letras minúsculas, números y caracteres 
especiales).(Para el generador de contraseñas puedes probar a usar los modulos random y string)"""

import time #Importar modulo para parar el script x segundos
import random #Importar modulo para randomizar nuestra contraseña nueva
import string #Importar modulo para generar letras, numeros y caracteres especiales en nuestra funcion
from FuncionesPython.ComprobarPasswordSegura import comprobar_passwd
from FuncionesPython.GeneradorPasswordSegura import generador_passwd

contraseña_user = input("Introduce tu contraseña:\n")

valido = comprobar_passwd(contraseña_user)
if valido:
    pass
else:
    print("Generando una contraseña segura aleatoria para ti...")
    time.sleep(2)
    generador_passwd()