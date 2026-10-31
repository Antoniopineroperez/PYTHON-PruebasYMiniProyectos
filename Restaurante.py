#Definimos las variables
precio_ensalada = 12
precio_sopa = 10
precio_dorada = 18
precio_arroz = 14
precio_lasaña = 15
precio_brownie = 8
precio_helado = 6
precio_cafe = 3.5
precio_refresco = 5.5
#Preguntamos al cliente qué ha consumido
refresco = input("¿Cantidad de refrescos consumidos?:")
refresco = float(refresco)
ensalada = input("¿Cantidad de ensalada consumida?:")
ensalada = int(ensalada)
sopa = input("¿Cantidad de sopa consumida?:")
sopa = int(sopa)
dorada = input("¿Cantidad de dorada consumida?:")
dorada = int(dorada)
arroz = input("¿Cantidad de arroz consumido?:")
arroz = int(arroz)
lasaña = input("¿Cantidad de lasaña consumida?:")
lasaña = int(lasaña)
brownie = input("¿Cantidad de brownie consumido?:")
brownie = int(brownie)
helado = input("¿Cantidad de helado consumido?:")
helado = int(helado)
cafe = input("¿Cantidad de café consumido?:")
cafe = float(cafe)
#Sumamos las cantidades
suma_refresco = precio_refresco * refresco
suma_ensalada = precio_ensalada * ensalada
suma_sopa = precio_sopa * sopa
suma_dorada = precio_dorada * dorada
suma_arroz = precio_arroz * arroz
suma_lasaña = precio_lasaña * lasaña
suma_brownie = precio_brownie * brownie
suma_helado = precio_helado * helado
suma_cafe = precio_cafe * cafe
suma_total = suma_refresco + suma_arroz + suma_brownie + suma_cafe + suma_dorada + suma_ensalada + suma_helado + suma_lasaña + suma_sopa
#Mostramos la cuenta
print("IMPORTE REFRESCOS: ", suma_refresco, " €")
print("IMPORTE ENSALADAS: ", suma_ensalada, " €")
print("IMPORTE SOPAS: ", suma_sopa, " €")
print("IMPORTE DORADAS: ", suma_dorada, " €")
print("IMPORTE ARROCES: ", suma_arroz, " €")
print("IMPORTE LASAÑAS: ", suma_lasaña, " €")
print("IMPORTE BROWNIES: ", suma_brownie, " €")
print("IMPORTE HELADOS: ", suma_helado, " €")
print("IMPORTE DORADAS: ", suma_cafe, " €")
print("IMPORTE TOTAL: ", suma_total, " €")