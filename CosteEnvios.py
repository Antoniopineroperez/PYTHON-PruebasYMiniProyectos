"""Imagina que estás trabajando en un sistema de gestión de costos 
de envío para una empresa de logística. El sistema debe calcular el 
costo de envío para diferentes destinos, distancias y pesos de paquetes.
Implementa una función llamada calcular_costo_envio que tome como entrada
un destino, una distancia en kilómetros y un peso en kilogramos, y devuelva
el costo total del envío.
Requerimientos:
1. El costo base de envío es de $5.0.
2. El costo por kilómetro de distancia es de $0.1.
3. El costo por kilogramo de peso es de $0.2.
Implementa la función de manera eficiente utilizando memoización para evitar
recalcular el costo para los mismos destinos, distancias y pesos."""

registro_envios = [
    {"ciudad": "Madrid", "distancia": 100, "peso": 51},
    {"ciudad": "Avila", "distancia": 201, "peso": 130},
    {"ciudad": "Toledo", "distancia": 91, "peso": 180},
]

def calcular_coste_envio(registro):
    for elemento in registro:
        print(f"Ciudad: {elemento["ciudad"]} -- Distancia(km): {elemento["distancia"]} -- Peso(kg): {elemento["peso"]}")
        coste_total = (elemento["distancia"] * 0.1) + (elemento["peso"] * 0.2)
        print(f"El coste total del envío a {elemento["ciudad"]} sería ${coste_total}")
        print("")

calcular_coste_envio(registro_envios)