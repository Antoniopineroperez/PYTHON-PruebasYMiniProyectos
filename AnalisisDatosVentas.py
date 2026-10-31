"""Imagina que eres parte de una empresa de comercio electrónico y tienes
información detallada sobre las ventas de productos. Cada venta se representa
como un diccionario, que incluye el nombre del producto, la fecha de venta, el monto 
de la venta y la ubicación del comprador. Realiza un análisis avanzado de estas ventas.
1. Filtra las ventas realizadas en el último trimestre del año.
2. Selecciona solo las ventas de productos con un monto superior a $500.
3. Agrupa las ventas por ubicación del comprador.
4. Calcula el promedio del monto de venta para cada ubicación.
5. Ordena las ubicaciones por el promedio del monto de venta de forma
descendente. Utiliza funciones lambda."""

from datetime import datetime
ventas = [
    {"producto": "RAM", "fecha": "21-09-2026", "coste": 640, "ubicacion": "Toledo"},
    {"producto": "RAM", "fecha": "21-11-2026", "coste": 1890, "ubicacion": "Malaga"},
    {"producto": "RAM", "fecha": "23-12-2026", "coste": 2100, "ubicacion": "Toledo"},
    {"producto": "RAM", "fecha": "22-08-2026", "coste": 430, "ubicacion": "Madrid"},
    {"producto": "Procesador", "fecha": "24-10-2026", "coste": 1006, "ubicacion": "Toledo"},
    {"producto": "Procesador", "fecha": "23-11-2026", "coste": 499, "ubicacion": "Madrid"}
]

def analisis_ventas(ventas):

    #Filtramos el ultimo trimestre
    ventas_filtradas = [venta for venta in ventas if datetime.strptime(venta["fecha"], "%d-%m-%Y").month >= 10]
    
    
    #Seleccionamos las ventas mayores a $500
    ventas_filtradas = [venta for venta in ventas_filtradas if venta["coste"] > 500]
    
    
    #Agrupar ventas por ubicacion de comprador
    ventas_agrupadas = {}

    print("Las ventas mayores a $500 en el último trimestre agrupadas por ubicación son:")
    for venta in ventas_filtradas:
        ubicacion = venta["ubicacion"]
        if ubicacion is not ventas_agrupadas:
            ventas_agrupadas[ubicacion] = []

        ventas_agrupadas[ubicacion].append(venta)
    
    print(ventas_agrupadas)


    #Calculamos el promedio de facturacion de ventas por ubicacion
    promedio_ventas = {}

    print("")
    print("PROMEDIO VENTAS POR UBICACION:")
    for ubicacion in ventas_agrupadas:
        ventas_por_ubicacion = ventas_agrupadas[ubicacion]
        promedio_ventas[ubicacion] = sum(venta["coste"] for venta in ventas_por_ubicacion) / len(ventas_por_ubicacion)
    
    print(promedio_ventas)


    #Ordenamos en orden descendente las ubicaciones por promedio de ventas
    ubicaciones_ordenadas = sorted(promedio_ventas, key=lambda ubicacion:promedio_ventas[ubicacion], reverse=True)

    print("")
    print("ORDEN DESCENDENTE DE PROMEDIO DE VENTAS POR UBICACION:")
    for ubicacion in ubicaciones_ordenadas:
        print(f"{ubicacion}: {promedio_ventas[ubicacion]}")

analisis_ventas(ventas)