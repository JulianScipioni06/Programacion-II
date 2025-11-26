class Libro:
    @classmethod
    def fromDiccionario(cls, dicc:dict) -> 'Libro':
        return cls(dicc["isbn"], dicc["titulo"], dicc["autor"], dicc["genero"], dicc["anio_publicacion"], dicc["cantidad_ejemplares"])
    
    def __init__(self, isbn:int, titulo:str, autor:str, genero:str, anio_publicacion:int, cantidad_ejemplares:int):
        if not isinstance(isbn, int) or isbn < 0:
            raise ValueError("isbn debe ser un entero positivo.")
        if not isinstance(titulo, str) or titulo.strip() == "":
            raise ValueError("titulo debe ser un string no nulo.")
        if not isinstance(autor, str) or autor.strip() == "":
            raise ValueError("autor debe ser un string no nulo.")
        if not isinstance(genero, str) or genero.strip() == "":
            raise ValueError("genero debe ser un string no nulo.")
        if not isinstance(anio_publicacion, int) or anio_publicacion < 0:
            raise ValueError("anio_publicacion debe ser un entero positivo.")
        if not isinstance(cantidad_ejemplares, int) or cantidad_ejemplares < 0:
            raise ValueError("cantidad_ejemplares debe ser un entero positivo.")
        
        self.__isbn = isbn
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero
        self.__anio_publicacion = anio_publicacion
        self.__cantidad_ejemplares = cantidad_ejemplares
    
    #Comandos Triviales
    def establecerIsbn(self, isbn:int):
        if not isinstance(isbn, int) or isbn < 0:
            raise ValueError("isbn debe ser un entero positivo.")
        
        self.__isbn = isbn
    
    def establecerTitulo(self, titulo:str):
        if not isinstance(titulo, str) or titulo.strip() == "":
            raise ValueError("titulo debe ser un string no nulo.")
        
        self.__titulo = titulo
    
    def establecerAutor(self, autor:str):
        if not isinstance(autor, str) or autor.strip() == "":
            raise ValueError("autor debe ser un string no nulo.")
        
        self.__autor = autor
    
    def establecerGenero(self, genero:str):
        if not isinstance(genero, str) or genero.strip() == "":
            raise ValueError("genero debe ser un string no nulo.")
        
        self.__genero = genero
    
    def establecerAnio(self, anio_publicacion:int):
        if not isinstance(anio_publicacion, int) or anio_publicacion < 0:
            raise ValueError("anio_publicacion debe ser un entero positivo.")
        
        self.__anio_publicacion = anio_publicacion
    
    def establecerEjemplares(self, cantidad_ejemplares:int):
        if not isinstance(cantidad_ejemplares, int) or cantidad_ejemplares < 0:
            raise ValueError("anio_publicacion debe ser un entero positivo.")
        
        self.__cantidad_ejemplares = cantidad_ejemplares
    
    #Consultas Triviales
    def obtenerIsbn(self) -> int:
        return self.__isbn
    
    def obtenerTitulo(self) -> str:
        return self.__titulo
    
    def obtenerAutor(self) -> str:
        return self.__autor
    
    def obtenerGenero(self) -> str:
        return self.__genero
    
    def obtenerAnio(self) -> int:
        return self.__anio_publicacion
    
    def obtenerEjemplares(self) -> int:
        return self.__cantidad_ejemplares
    
    def esIgual(self, otroLibro:'Libro') -> bool:
        mismoIsbn = self.__isbn == otroLibro.obtenerIsbn()
        mismoTitulo = self.__titulo == otroLibro.obtenerTitulo()
        mismoAutor = self.__autor == otroLibro.obtenerAutor()
        mismoGenero = self.__genero == otroLibro.obtenerGenero()
        mismoAnio = self.__anio_publicacion == otroLibro.obtenerAnio()
        mismosEjemplares = self.__cantidad_ejemplares == otroLibro.obtenerEjemplares()
        
        return mismoIsbn and mismoTitulo and mismoAutor and mismoGenero and mismoAnio and mismosEjemplares
    
    def toDiccionario(self) -> dict:
        return {
            "isbn": self.__isbn,
            "titulo": self.__titulo,
            "autor": self.__autor,
            "genero": self.__genero,
            "anio_publicacion": self.__anio_publicacion,
            "cantidad_ejemplares": self.__cantidad_ejemplares
        }
    
    def __str__(self):
        return (
            f"Libro: {self.__titulo}\n"
            f"- ISBN: {self.__isbn}\n"
            f"- Autor: {self.__autor}\n"
            f"- Genero: {self.__genero}\n"
            f"- Año Publicacion: {self.__anio_publicacion}\n"
            f"- Ejemplares: {self.__cantidad_ejemplares}"
        )