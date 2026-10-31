"""Imagina que estás desarrollando un sistema complejo que incluye múltiples
funciones críticas. Para asegurarte de que todo funcione correctamente y para
realizar un seguimiento del tiempo de ejecución de estas funciones, decides
implementar un decorador de registro (logger) con tiempo de ejecución.
El decorador debería realizar las siguientes acciones:
1. Antes de llamar a la función original (puedes incluir cualquier función),
debe imprimir un mensaje indicando que la función está a punto de
ejecutarse.
2. Después de que la función se haya ejecutado, debe imprimir un mensaje
que incluya el tiempo que tardó la función en ejecutarse.
3. Si la función original arroja una excepción, el decorador debe manejarla e
imprimir un mensaje adecuado, indicando que se ha producido una excepción."""

#Importamos los modulos necesarios y nuestras funciones
import time as time
from FuncionesPython.ComprobarPasswordSegura import comprobar_passwd
from FuncionesPython.GeneradorPasswordSegura import generador_passwd

#Iniciamos el temporizador de script
inicio = time.perf_counter()

#Pedimos al usuario que cree una contraseña
contraseña = input("Introduce tu contraseña:\n")

#Iniciamos el temporizador para ejecutar el comprobador de contraseñas
print("El programa va a ejecutarse en:")
time.sleep(1)
contador = 3
while contador > 0:
    print(contador, "...")
    time.sleep(1)
    contador = contador - 1

#Una vez terminado el temporizador, iniciamos la funcion para comprobar si la contraseña es segura    
valido = comprobar_passwd(contraseña)

#Si lo es, se lo hacemos saber al usuario y mostramos el tiempo de ejecucion del script
if valido == True:
    fin = time.perf_counter()
    print(f"Tiempo exacto de ejecución del programa: {fin - inicio:.6f} segundos")
#Si no lo es, generamos una nueva contraseña con nuestra funcion y se lo mostramos,
#al igual que el tiempo de ejecucion del script
else:
    print("Generando una contraseña segura para ti...")
    time.sleep(2)
    generador_passwd()
    fin = time.perf_counter()
    print(f"Tiempo exacto de ejecución del programa: {fin - inicio:.6f} segundos")