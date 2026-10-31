#Cada estudiante tiene:
# 2 EXAMENES
# 1 TRABAJO FINAL
# 1 PARTICIPACION EN CLASE
# Calcular la nota final teniendo en cuenta que:
# EXAMENES CUENTAN 30% CADA UNO DE NOTA FINAL
# TRABAJO CUENTA 30%
# PARTICIPACION CUENTA 10%

import numpy as np
#Primera columna examen 1, segunda columna examen 2
#tercera columna trabajo final, cuarta columna participacion clase
#Cada fila es un alumno
calificaciones = np.array((
    [10, 6, 7, 2],
    [2, 5, 10, 10],
    [8, 3, 3, 10],
    [8, 7, 5, 5]
))

#Calculamos la nota final de cada estudiante
examen1 = calificaciones[:, 0]
examen2 = calificaciones[:, 1]
trabajo = calificaciones[:, 2]
participacion = calificaciones[:, 3]

nota_final = examen1 * 0.3 + examen2 * 0.3 + trabajo * 0.3 + participacion * 0.1

print(f"Alumno 1, nota final: {nota_final[0]:.2f}")
print(f"Alumno 2, nota final: {nota_final[1]:.2f}")
print(f"Alumno 3, nota final: {nota_final[2]:.2f}")
print(f"Alumno 4, nota final: {nota_final[3]:.2f}")