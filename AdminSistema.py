#Creamos un script para comprobar si el usuario está 
#autorizado para entrar al sistema. Nuestro sistema
#tiene unas listas definidas de usuarios autorizados por Username y Password
usernames_autorizados = ["antonio666", "paulita13", "jesus67", "akualau"]
contraseñas_autorizadas = ["Danonino", "Nalita", "Gusi", "Wandy"]

usuario = False
psswd = False

#Comprobamos si los datos son correctos recorriendo las listas
while usuario == False:
    username = input("Introduce tu nombre de usuario:\n")
    for user in usernames_autorizados:
        if username in usernames_autorizados:
            usuario = True
            break
        else:
            print("Nombre de usuario erroneo, intentalo de nuevo")
            break

while psswd == False:
    contraseña = input("Introduce tu contraseña:\n")
    for i in contraseñas_autorizadas:
        if contraseña in contraseñas_autorizadas:
            psswd = True
            break
        else:
            print("Contraseña erronea, intentalo de nuevo")
            break

if usuario and psswd == True:
    print("¡Bienvenidx", username,"!")