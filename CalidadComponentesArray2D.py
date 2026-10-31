#Tenemos que determinar que componenete es el de mayor calidad,
#cuantos componentes se produjeron cada mes y promedio
#de calidad de cada tipo de componente
#Columna 1: Fecha de produccion 
#Columna 2: Tipo de componente 
#Columna 3: Lote del componente
#Columna 4: Puntuacion de calidad del componente (entre 0 y 100)
import numpy as np
datos = np.array([
    ["01-01-2026", "Placa base", "Lote A", 95],
    ["02-01-2026", "Procesador", "Lote B", 73],
    ["01-02-2026", "Procesador", "Lote C", 90],
    ["02-02-2026", "Placa base", "Lote D", 84],
    ["01-03-2026", "Placa base", "Lote E", 80],
    ["02-03-2026", "Procesador", "Lote F", 65]
])

#Buscar qué componente es el de mayor calidad
tipos_componentes = datos[:, 1]
tipos_unicos = np.unique(tipos_componentes)
calidad = datos[:, 3]
promedios = np.zeros(len(tipos_unicos))
i = 0

for tipo in tipos_unicos:
    print(tipo)
    print(calidad[tipos_componentes == tipo])
    promedios[i] = np.mean(calidad[tipos_componentes == tipo])
    i = i + 1

indice_maximo = np.argmax(promedios)
tipo_bis = tipos_unicos[indice_maximo]

print("El tipo de componente de mayor calidad es el", tipo_bis)

#Cantidad de componentes producidos cada mes
fechas = datos[:, 0]
meses, counts = np.unique([fecha[0:5] for fecha in fechas], return_counts = True)

for i in range(len(meses)):
    print("Mes:", meses[i],"\n Cantidad producida:", counts[i])

#Puntuacion promedio de cada componente
promedio_por_tipo = np.zeros(len(tipos_unicos))

for i in range(len(tipos_unicos)):
    promedio_por_tipo[i] = np.mean(calidad[tipos_componentes == tipos_unicos[i]])
    print("La puntuacion promedio para", tipos_unicos[i], "es de", promedio_por_tipo[i])