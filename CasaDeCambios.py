#Pedir un número concreto de euros a covertir
print("¿Cuántos euros quieres convertir a dólares?:")
euros = input()
euros = float(euros)
#Convertir la cantidad de euros aportada por el usuario
dolares = euros * 1.2
#Calculamos cuanto se queda la casa y cuanto se le da al cliente
porcentaje_casa = dolares / 10
resto_cliente = dolares - porcentaje_casa
#Le damos el recibo al cliente
print("TOTAL BRUTO:", dolares, "dólares.")
print("-10% HONORARIOS:", porcentaje_casa, " dólares.")
print("TOTAL A RECIBIR:", resto_cliente, " dólares.")