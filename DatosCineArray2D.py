#Determinar que género de pelicula es el mas popular,
#cuantas pelis se lanzaron en cada decada y duración promedio 
#de cada género dada una tabla de datos
#Columna 1: Pelicula
#Columna 2: Género
#Columna 3: Duracion
#Columna 4: Fecha lanzamiento
import numpy as np
peliculas = np.array([
    ["Peli 1", "scifi", 142, 2001],
    ["Peli 2", "accion", 128, 2004],
    ["Peli 3", "scifi", 130, 2005],
    ["Peli 4", "drama", 110, 2008],
    ["Peli 5", "scifi", 121, 2011],
    ["Peli 6", "accion", 112, 2012],
    ["Peli 7", "scifi", 137, 2012],
    ["Peli 8", "scifi", 122, 2015],
    ["Peli 9", "scifi", 149, 2019],
    ["Peli 10", "drama", 109, 2020]
])

#Extraemos los datos del array
generos, conteos = np.unique(peliculas[:, 1], return_counts = True)
duracion = np.array([mins[2] for mins in peliculas])
fechas = np.array([fecha[3] for fecha in peliculas])

#Mostramos el género mas popular de la tabla
conteos_desc = np.argsort(conteos)[::-1]
genero_popular = generos[conteos_desc[0]]
print("El género más popular es", genero_popular.title())

#Mostramos cuantas pelis se lanzaron en cada decada
decada_0010 = []
decada_1020 = []
for i in fechas:
    if int(i) >= 2000 and int(i) < 2010:
        decada_0010.append(i)
    else:
        decada_1020.append(i)

print("Se han lanzado", len(decada_0010), "peliculas en la decada de 2000/2010")
print("Se han lanzado", len(decada_1020), "peliculas en la decada de 2010/2020")

#Duracion promedio de las pelis de cada género
todos_generos = peliculas[:, 1]
dur_media = np.zeros(len(generos))
for mins in range(len(generos)):
    dur_media[mins] = np.mean(duracion[todos_generos == generos[mins]].astype(float))
    print("Duracion media de las peliculas de tipo", generos[mins].title(), "es de", dur_media[mins], "minutos.")