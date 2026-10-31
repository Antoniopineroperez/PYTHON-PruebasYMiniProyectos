#Pedimos al cliente que elija un tipo de hamburguesa
eleccion = int(input("¿Qué hamburguesa desea?:\n1) Hamburguesa clásica\t2)Hamburguesa vegana "))
#Mostramos los ingredientes extra de cada hamburguesa y le damos a elegir
if (eleccion == 1): #Clasica
    print("Ingredientes extra:")
    extra = int(input("1) Queso Idiazabal\t2) Bacon\n3) Huevo\t\t4) Ninguno\n "))
    if (extra == 1):
       extra = "queso idiazabal"
       print("Pedido de hamburguesa clásica con extra de", extra)
    elif (extra == 2):
       extra = "bacon"
       print("Pedido de hamburguesa clásica con extra de", extra)
    elif (extra == 3):
       extra = "huevo"
       print("Pedido de hamburguesa clásica con extra de", extra)
    elif (extra == 4):
       extra = "ningun extra"
       print("Pedido de hamburguesa clásica sin", extra)
else: #Vegana
    print("Ingredientes extra:")
    extra = int(input("1) Tofu\t2) Cebolla caramelizada\n3) Ningun extra\n "))
    if (extra == 1):
       extra = "tofu"
       print("Pedido de hamburguesa vegana con extra de", extra)
    elif (extra == 2):
       extra = "cebolla caramelizada"
       print("Pedido de hamburguesa vegana con extra de", extra)
    elif (extra == 3):
       extra = "ningun extra"
       print("Pedido de hamburguesa vegana sin", extra)