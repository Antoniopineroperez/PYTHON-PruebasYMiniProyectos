#Crea un sistema de gestión de una biblioteca utilizando clases en Python.
#Debes implementar las siguientes clases:
#1. “Libro”: Representa un libro con atributos como título, autor 
#y número de ejemplares disponibles.
#2. “Usuario”: Representa a un usuario de la biblioteca con atributos como
#nombre, número de identificación y lista de libros prestados.
#3. “Biblioteca”: Representa la biblioteca en sí, con métodos para agregar
#libros, prestar libros a usuarios, devolver libros y mostrar el inventario.

class Libro:
    def __init__(self, titulo, autor, stock):
        self.titulo = titulo
        self.autor = autor
        self.stock = stock

class Usuario:
    def __init__(self, nombre, num_id):
        self.nombre = nombre
        self.num_id = num_id
        self.libros_prestados = []

class Biblioteca:
    def __init__(self):
        self.lista_libros = []

    def añadir_libros(self, libro):
        self.lista_libros.append(libro)

    def prestar_libro(self, usuario, titulo):
        for libro in self.lista_libros:
            if libro.titulo == titulo and libro.stock > 0:
                usuario.libros_prestados.append(libro)
                libro.stock = libro.stock - 1
                print(f"El libro {titulo} ha sido prestado a {usuario.nombre}")
                return
            
        print(f"El libro {titulo} no está disponible actualmente.")

    def devolver_libro(self, usuario, titulo):
        for libro in usuario.libros_prestados:
            if libro.titulo == titulo:
                usuario.libros_prestados.remove(libro)
                libro.stock = libro.stock + 1
                print(f"El libro {titulo} ha sido devuelto a la biblioteca por {usuario.nombre}")

    def inventario(self):
        for libro in self.lista_libros:
            print(f"{libro.titulo} de {libro.autor} -- Stock: {libro.stock}")

biblioteca = Biblioteca()
libro1 = Libro("El señor de los anillos", "Tolkien", 16)
libro2 = Libro("El Silmarillion", "Tolkien", 9)
biblioteca.añadir_libros(libro1)
biblioteca.añadir_libros(libro2)

usuario1 = Usuario("Antonio", "669969")
usuario2 = Usuario("Paula", "123456")
biblioteca.prestar_libro(usuario1, "El señor de los anillos")
biblioteca.prestar_libro(usuario1, "El señor de los anillos")
biblioteca.prestar_libro(usuario2, "El Silmarillion")

print("")
biblioteca.devolver_libro(usuario1, "El señor de los anillos")

print("")
biblioteca.inventario()