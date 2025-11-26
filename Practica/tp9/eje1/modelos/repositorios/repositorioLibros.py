from modelos.entidades.libro import Libro
import json

class RepositorioLibro:
    FILE_PATH = r"D:\UNIVERSIDAD\SegundoCuatrimestre\Programacion-II\Practica\tp9\eje1\datos\libros.json"
    
    def __init__(self):
        self.__libros = self.__cargarTodos()
    
    def __cargarTodos(self):
        lista_libros = []
        
        try:
            with open(RepositorioLibro.FILE_PATH, "r") as file:
                datos = json.load(file)
                for l in datos:
                    lista_libros.append(Libro.fromDiccionario(l))
        except FileNotFoundError:
            print("No se encontro el archivo")
            
        return lista_libros
    
    def __guardarTodos(self):
        try:
            lista = []
            
            for libro in self.__libros:
                if isinstance(libro, Libro):
                    lista.append(libro.toDiccionario())
            
            with open(RepositorioLibro.FILE_PATH, "w")as file:
                json.dump(lista, file, indent=4)
            
        except FileNotFoundError:
            print("No se encontro el archivo")
    
    def obtenerTodos(self) -> list:
        return self.__libros
    
    def obtenerPorIsbn(self, isbn:int):
        for i in self.__libros:
            if isinstance(i,Libro):
                if i.obtenerIsbn() == isbn:
                    return i
        return None
    
    def existe(self, libro: Libro) -> bool:
        return libro in self.__libros
    
    def existeIsbn(self, isbn:int) -> bool:
        for i in self.__libros:
            if isinstance(i,Libro):
                if i.obtenerIsbn() == isbn:
                    return True
        return False
    
    def agregar(self, nuevoLibro:Libro):
        if not isinstance(nuevoLibro, Libro):
            raise TypeError("Se esperaba una instancia de Libro")
        
        if not self.existe(nuevoLibro):
            self.__libros.append(nuevoLibro)
            self.__guardarTodos()
    
    def modificarPorISBN(self, isbn:int, titulo:str, autor:str, genero:str, anio_publicacion:int, cantidad_ejemplares:int) -> bool:
        if self.existeIsbn(isbn):
            libro = self.obtenerPorIsbn(isbn)
            libro.establecerTitulo(titulo)
            libro.establecerAutor(autor)
            libro.establecerGenero(genero)
            libro.establecerAnio(anio_publicacion)
            libro.establecerEjemplares(cantidad_ejemplares)
            
            self.__guardarTodos()
            return True
        return False
    
    def eliminarPorISBN(self, isbn:int):
        if self.existeIsbn(isbn):
            libro = self.obtenerPorIsbn(isbn)
            
            self.__libros.remove(libro)
            self.__guardarTodos()
            return True
        return False