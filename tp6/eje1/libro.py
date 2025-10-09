class Libro:
    #Constructor
    def __init__(self, nombre:str, autor:str, editorial:str, categoria:str):
        """
        Inicializa un nuevo Objeto Libro.
        Parametros:
        - nombre = Titulo del Libro
        - autor = Autor del Libro
        - editorial = Editorial del Libro
        - categoria = Categoria del Libro
        """
        self.__nombre = nombre
        self.__autor = autor
        self.__editorial = editorial
        
        if categoria.upper() in ['A','B','C']:
            self.__categoria = categoria.upper()
        else:
            raise ValueError("Esa Cataegoria No existe!")
    
    #Consultas
    def obtenerNombre(self) -> str:
        """Devuelve el Titulo del Libro"""
        return self.__nombre
    
    def obtenerAutor(self) -> str:
        """Devuelve el Autor del Libro"""
        return self.__autor
    
    def obtenerEditorial(self) -> str:
        """Devuelve la Editorial del Libro"""
        return self.__editorial
    
    def obtenerCategoria(self) -> str:
        """Devuelve la Categoria del Libro"""
        return self.__categoria
    
    def __str__(self):
        return f"DATOS DEL LIBRO: \n Nombre: {self.__nombre}\n Autor: {self.__autor}\n Editorial: {self.__editorial}\n Categoria: {self.__categoria}\n"