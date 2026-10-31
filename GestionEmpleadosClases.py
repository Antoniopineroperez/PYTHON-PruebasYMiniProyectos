#Supongamos que estás construyendo un sistema de gestión de empleados
#para una empresa. Crea un sistema de clases que maneje la información de
#los empleados, incluyendo empleados a tiempo completo y 
#empleados a tiempo parcial.
#- Clase base: `Empleado`
#- Atributos: nombre, apellido, salario base
#- Clase derivada: `EmpleadoTiempoCompleto` (hereda de `Empleado`)
#- Atributo adicional: bono anual
#- Clase derivada: `EmpleadoTiempoParcial` (hereda de `Empleado`)
#- Atributo adicional: horas trabajadas por semana
#Resuelve el problema creando instancias de estas clases y calculando los
#salarios totales para diferentes tipos de empleados.

class Empleado:
    def __init__(self, nombre, apellido, salario):
        self.nombre = nombre
        self.apellido = apellido
        self.salario = salario


class EmpleadoFullTime(Empleado):
    def __init__(self, nombre, apellido, salario, bono_anual):
        super().__init__(nombre, apellido, salario)
        self.bono_anual = bono_anual

    def calcular_salario_completo(self):
        return(print(f" El salario completo de {self.nombre} es de {self.salario + self.bono_anual}€"))


class EmpleadoParcial(Empleado):
    def __init__(self, nombre, apellido, salario, horas_semana):
        super().__init__(nombre, apellido, salario)
        self.horas_semana = horas_semana

    def calcular_salario_completo(self):
        return(print(f" El salario completo de {self.nombre} es de {self.salario + 1.5*self.horas_semana*4*12}€"))

empleado1 = EmpleadoFullTime("Antonio", "Piñero Pérez", 32000, 4000 )
empleado2 = EmpleadoFullTime("Paula", "Martin Rebolo", 32000, 4200)
empleado3 = EmpleadoParcial("Jesus", "Vaquero", 20000, 20)
empleado4 = EmpleadoParcial("Laura", "Moncin", 21000, 25)
empleado1.calcular_salario_completo()
empleado2.calcular_salario_completo()
empleado3.calcular_salario_completo()
empleado4.calcular_salario_completo()