#Pedimos al usuario un precio
precio_producto = float(input("Establece el precio del producto: "))
#Si el precio <100 imprimimos comprar
#Si el precio esta entre 100-150 imprimimos hold
#Si el precio 150> imprimimos vender
if (precio_producto < 100):
    print("COMPRAR")
elif (precio_producto >= 100) and (precio_producto <= 150):
    print("HOLD")
else:
    print("VENDER")