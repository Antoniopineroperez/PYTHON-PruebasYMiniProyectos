#Calcular promedio de temperatura, humedad y presion atmosferica 
#de diferentes ciudades durante un año
#Columna 1: temperatura
#Columna 2: humedad
#Columna 3: presion atmosferica
#Columna 4: mes
import numpy as np
datos = np.array([
    [18, 73, 1021, 1],
    [17, 73, 1009, 1],
    [22, 69, 1013, 2],
    [23, 64, 1017, 2],
    [21, 55, 1020, 3],
    [22, 52, 1016, 3],
    [22, 46, 1005, 4],
    [24, 46, 1001, 4],
    [25, 43, 1008, 5],
    [23, 38, 1025, 5],
    [29, 39, 1011, 6],
    [32, 37, 1021, 6],
    [33, 30, 1030, 7],
    [32, 31, 1000, 7],
    [32, 36, 1017, 8],
    [33, 38, 1002, 8],
    [33, 43, 1008, 9],
    [31, 52, 1010, 9],
    [27, 60, 1010, 10],
    [27, 64, 1023, 10],
    [21, 69, 1019, 11],
    [20, 72, 1014, 11],
    [18, 74, 1021, 11],
    [18, 71, 1006, 12],
    [15, 72, 1016, 12]
])

#Extraemos datos de cada columna
datos_temp = np.array([grados[0] for grados in datos])
datos_hum = np.array([humedad[1] for humedad in datos])
datos_prs = np.array([presion[2] for presion in datos])
datos_meses = np.array([mes[3] for mes in datos])

media_temp = np.zeros(12)
media_hum = np.zeros(12)
media_prs = np.zeros(12)

#Calculamos las medias de cada tipo de dato
for i in range(12):
    media_temp[i] = np.mean(datos_temp[datos_meses == i+1])
    media_hum[i] = np.mean(datos_hum[datos_meses == i+1])
    media_prs[i] = np.mean(datos_prs[datos_meses == i+1])
    #Mostramos los resultados
    print("La temperatura promedio en el mes", i+1, "fue de", media_temp[i], "grados")
    print("La humedad promedio en el mes", i+1, "fue de", media_hum[i])
    print("La presión atmosférica promedio en el mes", i+1, "fue de", media_prs[i], "bar")