class Autor:
    def __init__(self,nombre):
        self.nombre = nombre
        
class Libro:
    def __init__(self,titulo,autor):
        self.titulo = titulo
        self.autor = autor
        self.prestado = False
        
        
class Biblioteca:
    def __init__(self):
        self.libros = []
        
    def agregarlibro(self,libro):
        self.libros.append(libro)
        
    def buscar_autor(self,nombre_autor):
        return [libro for libro in self.libros if libro.autor.nombre == nombre_autor]
    
    def prestar_libro(self,titulo):
        for libro in self.libros:
            if libro.titulo == titulo and not libro.prestado:
                libro.prestado = True
                return True
        return False
    
    def libros_prestados(self):
        return [libro for libro in self.libros if libro.prestado]
    
    def buscar_por_titulo(self,titulo):
        return [libro for libro in self.libros if libro.titulo == titulo]
    
    
class Usuario:
    def __init__(self,nombre):
        self.nombre = nombre
        self.libros = []
        
    def tomar_prestado(self,biblioteca, titulo):
        if biblioteca.prestar_libro(titulo):
            self.libros.append(titulo)
            return True
        return False
    
autor1 = Autor("Gabriel Garcia Marquez")
autor2 = Autor("Miguel de Cervantes")
    
libro1 = Libro("Cien años de soledad",autor1)
libro2 = Libro("El quijote de la Mancha",autor2)
    
biblioteca = Biblioteca()
biblioteca.agregarlibro(libro1)
biblioteca.agregarlibro(libro2)
    
usuario = Usuario("John")

usuario.tomar_prestado(biblioteca,"Cien años de soledad")

biblioteca.libros_prestados()

        
