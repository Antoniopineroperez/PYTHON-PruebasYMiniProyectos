#Crea una clase "Pila" que represente una pila (stack) básica. Implementa
#métodos para agregar elementos a la pila, quitar elementos y mostrar el
#contenido actual.

class Pila:
    def __init__(self):
        self.elementos = []

    def añadir(self, elemento):
        self.elementos.append(elemento)

    def extraer(self):
        if len(self.elementos) == 0:
            print("No se puede quitar ningun elemento, la lista está vacia.")
        else:
            self.elementos.pop()

    def mostrar_elementos(self):
        for elemento in self.elementos:
            print(elemento)
        print(self.elementos)


stack = Pila()
stack.añadir(1)
stack.añadir(20)
stack.añadir(66)
stack.mostrar_elementos()
print("")

print("Extraemos el último elemento")
stack.extraer()
stack.mostrar_elementos()
print("")

print("Extraemos todo y mostramos el mensaje de error.")
stack.extraer()
stack.extraer()
stack.extraer()
stack.mostrar_elementos()