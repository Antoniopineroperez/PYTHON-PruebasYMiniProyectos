#Definiendo variables
rbm1 = 20000 * 0.03
rbmplus = 35000 * 0.05
rbmtodoterreno = 60000 * 0.07

#Pedimos al usuario que introduzca el numero de coches vendidos
num_rbm1 = input("Introduce el número de RBM Serie 1 vendidos este mes:")
num_rbm1 = float(num_rbm1) #Transformamos el valor introducido a numero decimal
total_rbm1 = rbm1 * num_rbm1 #Numero de coches vendidos X comision por cada coche vendido

num_rbmplus = input("Introduce el número de RBM Serie Plus vendidos este mes:")
num_rbmplus = float(num_rbmplus)
total_rbmplus = rbmplus * num_rbmplus

num_rbmtodoterreno = input("Introduce el número de RBM Todoterreno vendidos este mes:")
num_rbmtodoterreno = float(num_rbmtodoterreno)
total_rbmtodoterreno = rbmtodoterreno * num_rbmtodoterreno
#Imprimimos por pantalla el resultado
print("COMISIONES TOTALES POR RBM SERIE 1: ", total_rbm1, " euros.")
print("COMISIONES TOTALES POR RBM SERIE PLUS: ", total_rbmplus, " euros.")
print("COMISIONES TOTALES POR RBM TODOTERRENO: ", total_rbmtodoterreno, " euros.")