#Imagina que estás desarrollando un sistema de reservas de vuelos para una
#aerolínea. Crea un sistema de clases que permita a los usuarios realizar
#reservas de vuelos. Aquí tienes una posible estructura:
#- Clase base: `Vuelo`
#- Atributos: número de vuelo, origen, destino, capacidad máxima,
#lista de pasajeros.
#- Métodos: agregar pasajero, verificar disponibilidad de asientos
#- Clase derivada: `VueloEspecial` (hereda de `Vuelo`)
#- Atributos adicionales: motivo del vuelo especial 
#(por ejemplo, vacaciones, trabajo)
#Resuelve el problema creando instancias de estas clases y realizando
#reservas para diferentes vuelos y tipos de vuelos especiales.

class Vuelo:
    def __init__(self, num_vuelo, origen, destino, capacidad_maxima):
        self.num_vuelo = num_vuelo
        self.origen = origen
        self.destino = destino
        self.capacidad_maxima = capacidad_maxima
        self.lista_pasajeros = []

    def añadir_pasajero(self, pasajero):
        if len(self.lista_pasajeros) < self.capacidad_maxima:
            self.lista_pasajeros.append(pasajero)
            print(f"Pasajero `{pasajero}´ añadido al vuelo correctamente.")
        else:
            print("No quedan más asientos disponibles.")

    def disponibilidad_asientos(self):
        asientos_disponibles = self.capacidad_maxima - len(self.lista_pasajeros)
        if asientos_disponibles > 0:
            print(f"Quedan {asientos_disponibles} asientos disponibles en este vuelo.")
        else:
            print("No quedan asientos disponibles para este vuelo.")

    def mostrar_pasajeros(self):
        print(f"Lista de pasajeros del vuelo número {self.num_vuelo} con origen {self.origen} y destino {self.destino}.")
        print(self.lista_pasajeros)


class VueloEspecial(Vuelo):
    def __init__(self, num_vuelo, origen, destino, capacidad_maxima, motivo):
        super().__init__(num_vuelo, origen, destino, capacidad_maxima)
        self.motivo = motivo


vuelo_normal1 = Vuelo("AB69", "ESP", "NY", 150)
vuelo_normal1.añadir_pasajero("Antonio")
print("")
vuelo_normal1.disponibilidad_asientos()
print("")
vuelo_normal1.mostrar_pasajeros()
print("")
print("")

vuelo_especial1 = VueloEspecial("AB70sp", "ESP", "NOR", 100, "Vacaciones")
print(f"Motivo del vuelo: {vuelo_especial1.motivo}")
vuelo_especial1.añadir_pasajero("Antonio")
vuelo_especial1.añadir_pasajero("Paula")
print("")
vuelo_especial1.disponibilidad_asientos()
print("")
vuelo_especial1.mostrar_pasajeros()