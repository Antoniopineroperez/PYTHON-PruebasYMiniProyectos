#Pedir al usuario su edad y su salario mensual neto
edad = int(input("Introduce tu edad: "))
salario_mes = float(input("Introduce tu salario neto mensual: "))
#Calculamos si se le aplica algun tipo impositivo
# < 15000€/año (5%) -- 15000 a 25000€/año (15%) -- 25000 a 35000€/año (20%)
# 35000 a 60000€/año (30%) -- > 60000€/año (45%)
salario_año = salario_mes * 12
print("Tu salario neto anual es de", salario_año)
if (edad >= 18):
    if (salario_año < 15000):
        print("Te corresponde un 5 por ciento de impuestos.\nTOTAL: -", salario_año / 5, "€")
    elif (salario_año >= 15000) and (salario_año < 25000):
        print("Te corresponde un 15 por ciento de impuestos.\nTOTAL: -", salario_año / 15, "€")
    elif (salario_año >= 25000) and (salario_año < 35000):
        print("Te corresponde un 20 por ciento de impuestos.\nTOTAL: -", salario_año / 20, "€")
    elif (salario_año >= 35000) and (salario_año < 60000):
        print("Te corresponde un 30 por ciento de impuestos.\nTOTAL: -", salario_año / 30, "€")
    elif (salario_año >= 60000):
        print("Te corresponde un 45 por ciento de impuestos.\nTOTAL: -", salario_año / 45, "€")
else:
    print("No eres mayor de edad, no se puede hacer el calculo.") 