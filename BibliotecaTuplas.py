#Una biblioteca tiene una lista de libros y sus autores. 
#Crea un programa que tome la lista de libros y sus autores 
#como una lista de tuplas, donde cada tupla contiene el título 
#del libro y el nombre del autor, y devuelva una nueva lista de tuplas 
#que contenga el título del libro y el apellido del autor.
lista_libros = [("Juego de tronos", "Antonio Piñero"), 
                ("El señor de los anillos", "Paula Martin"), 
                ("El gato con botas", "Jesus Vaquero")]
lista_titulos = []
lista_autor = []
lista_final = []

print("Nuestra biblioteca contiene los siguientes ejemplares:\n", lista_libros)

#Extraemos el titulo de los libros
lista_titulos.append(lista_libros[0][0])
lista_titulos.append(lista_libros[1][0])
lista_titulos.append(lista_libros[2][0])

#Extraemos el apellido del autor
lista_autor.append(lista_libros[0][1][7:14])
lista_autor.append(lista_libros[1][1][5:12])
lista_autor.append(lista_libros[2][1][5:13])

#Formamos la lista con los titulos y apellidos
tupla1 = (lista_titulos[0], lista_autor[0])
lista_final.append(tupla1)
tupla2 = (lista_titulos[1], lista_autor[1])
lista_final.append(tupla2)
tupla3 = (lista_titulos[2], lista_autor[2])
lista_final.append(tupla3)
print("La lista final quedaría asi:\n", lista_final)