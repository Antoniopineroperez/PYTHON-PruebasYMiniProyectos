#Calculamos la factuacion mensual de ciertos tipos de articulos
#vendidos a lo largo de un año dada una tabla de datos (array2d)
#Cada fila es una venta
#Primera columna: fecha de venta
#Segunda columna: total de facturacion de la venta
#Tercera columna: categoria del articulo vendido
import numpy as np
ventas = np.array((
    ["2026-01-01", 201, "cafe"],
    ["2026-01-02", 54, "merch"],
    ["2026-01-03", 187, "artilugios"],
    ["2026-02-01", 64, "cafe"],
    ["2026-02-02", 102, "cafe"],
    ["2026-02-03", 102, "artilugios"],
    ["2026-03-01", 170, "artilugios"],
    ["2026-03-02", 289, "cafe"],
    ["2026-03-03", 190, "merch"]
))

#Extraemos las facturaciones
facturaciones = np.array([dinero[1] for dinero in ventas])

#Sumamos la facturación total de cada mes
mes01 = sum(facturaciones[0:3].astype(int))
mes02 = sum(facturaciones[3:6].astype(int))
mes03 = sum(facturaciones[6:9].astype(int))
print("Total de ventas mes 1:")
print(mes01)
print("Total de ventas mes 2:")
print(mes02)
print("Total de ventas mes 3:")
print(mes03)