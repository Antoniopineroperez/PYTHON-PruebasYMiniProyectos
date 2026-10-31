#Crea una clase "CuentaBancaria" con atributos como número de cuenta y
#saldo. Implementa métodos para depositar y retirar dinero, y muestra el
#saldo actual.

class CuentaBancaria:
    def __init__(self, numero_cuenta, saldo = 0):
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo

    def ingresar(self, cantidad):
        self.saldo = self.saldo + cantidad
        print("Se han ingresado", cantidad, "€")
        print("Saldo actual:", self.saldo, "€")

    def retirar(self, cantidad):
        if self.saldo >= cantidad:
            self.saldo = self.saldo - cantidad
            print("Se han retirado", cantidad, "€")
            print("Saldo disponible:", self.saldo, "€")
        else:
            print("No se puede retirar la cantidad indicada, saldo insuficiente.")

cuenta = CuentaBancaria("6060")
cuenta.ingresar(5400)
cuenta.retirar(1400)