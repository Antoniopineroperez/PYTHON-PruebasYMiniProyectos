"""Estás desarrollando un sistema de autenticación para una aplicación web y deseas implementar 
un sistema de inicio de sesión que verifique si las credenciales proporcionadas por el usuario 
son válidas antes de permitir el acceso a ciertas funciones. Además, deseas que una vez que 
el usuario haya iniciado sesión correctamente, se le proporcione información personal.
Implementa lo siguiente:
1. Un registro de usuarios que contenga información adicional, 
como el nombre completo y el correo electrónico.
2. Un decorador llamado verificar_inicio_sesion que acepte el nombre de usuario y la
contraseña como argumentos. Este decorador verificará si las credenciales proporcionadas 
son válidas comparándolas con el registro de usuarios. Si las credenciales son válidas, 
la función decorada se ejecutará y se le pasará como argumento la información personal del usuario.
3. Una función llamada informacion_usuario que imprima la información personal del usuario 
después de que haya iniciado sesión correctamente. 
Implementa este sistema de inicio de sesión utilizando decoradores."""

usuarios = [
    {"nombre": "Antonio Piñero Pérez", "correo": "antoniopperez@gmail.com", "contraseña": "garbanzo"},
    {"nombre": "Paula Martin Rebolo", "correo": "paunalita@gmail.com", "contraseña": "nalitamarron"},
    {"nombre": "Jesus Vaquero", "correo": "jesuslolxd@gmail.com", "contraseña": "gusigusi"}
]

#Comprobamos que el inicio de sesión es correcto
login = False
contador = 1
while login == False and contador < 4:
    #Pedimos las credenciales al usuario
    print(f"Intento {contador} de 3:")
    username = input("Introduce el nombre de usuario:\n")
    password = input("Introduce tu contraseña:\n")
    
    for nombre in usuarios:
        if username in nombre["nombre"] and password == nombre["contraseña"]:
            print("")
            print(f"¡Inicio de sesión correcto, bienvenidx!")
            print(f"Información personal:\n{nombre['nombre']}, {nombre['correo']}")
            login = True
            break
        else:
            pass

    contador = contador + 1
    print("")

if contador == 4:
    print("Número de intentos superado, cerrando programa.")