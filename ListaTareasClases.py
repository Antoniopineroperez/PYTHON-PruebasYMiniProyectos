#Crea una clase "ListaTareas" que contenga una lista de tareas pendientes.
#Implementa métodos para agregar una tarea, marcar una tarea como
#completada y mostrar todas las tareas

class ListaTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append({"tarea": tarea, "completada": False})

    def completar(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice-1]["completada"] = True
            #Pongo el -1 para cuando el usuario (por ejemplo)
            #quiera marcar la tarea 1 como completada, introduzca el valor
            #1 en vez del 0 para acceder a la primera tarea,
            #asi es más intuitivo.

    def mostrar_tareas(self):
        for indice, tarea in enumerate(self.tareas):
            if tarea["completada"]:
                estado = "Completada"
            else:
                estado = "Pendiente"
            print(f"{indice + 1}. {tarea["tarea"]} - {estado}")
        print("")


lista_tareas = ListaTareas()
lista_tareas.agregar_tarea("Hacer la compra")
lista_tareas.agregar_tarea("Sacar a la perra")
lista_tareas.agregar_tarea("Hacer la comida")
lista_tareas.mostrar_tareas()
lista_tareas.completar(1)
lista_tareas.completar(2)
lista_tareas.mostrar_tareas()