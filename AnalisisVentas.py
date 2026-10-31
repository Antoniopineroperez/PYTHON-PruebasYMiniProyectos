#Queremos analizar las ventas por dia durante los ultimos 30 dias 
#en un negocio
#Creamos una lista con los dias de la semana y otra
#con las ventas del mes ordenadamente
ventas_mes = [82, 15, 44, 95, 36, 32, 29, 18, 14, 87, 70, 12, 76, 55, 59, 
              98, 89, 28, 30, 65, 78, 85, 72, 26, 90, 54, 94, 58, 96, 81]
dias_semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sábado", "Domingo"]
ventas_totales = [0, 0, 0, 0, 0, 0, 0]
contador_dias = 0

#Sumamos las ventas totales al dia de la semana
for venta in ventas_mes:
    ventas_totales[contador_dias] = ventas_totales[contador_dias] + venta
    contador_dias = contador_dias + 1
    if contador_dias == 7: #Cuando el dia llegue a Domingo, reiniciamos la semana a Lunes
        contador_dias = 0

#Mostramos por pantalla el resultado
for i in range(len(dias_semana)):
    print(dias_semana[i], ":", ventas_totales[i], "€")