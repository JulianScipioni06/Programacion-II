import json

class Libro:
    @classmethod
    def from_diccionario(cls, json_data): #Deserializacion
        datos = json.loads(json_data)
        return cls(datos["titulo"], datos["autor"], datos["genero"], datos["isbn"], datos["anioPublicacion"])
    
    def __init__(self, titulo:str, autor:str, genero:str, isbn:str, anioPublicacion:int):
        if not isinstance(titulo,str) or titulo.strip() == "":
            raise ValueError("titulo debe ser un string y no estar vacio!")
        if not isinstance(autor,str) or autor.strip() == "":
            raise ValueError("autor debe ser un string y no estar vacio!")
        if not isinstance(genero,str) or genero.strip() == "":
            raise ValueError("genero debe ser un string y no estar vacio!")
        if not isinstance(isbn,str) or isbn.strip() == "":
            raise ValueError("isbn debe ser un string y no estar vacio!")
        if not isinstance(anioPublicacion, int) or anioPublicacion <= 0:
            raise ValueError("Año de Publicacion debe ser un entero mayor que 0!")
        
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero
        self.__isbn = isbn
        self.__anioPublicacion = anioPublicacion
    
    def obtenerAnio(self):
        return self.__anioPublicacion
    
    def toDiccionario(self): #Serializacion
        dicc_libro = {"titulo": self.__titulo, "autor": self.__autor, "genero": self.__genero, "isbn": self.__isbn, "anioPublicacion": self.__anioPublicacion}
        
        return json.dumps(dicc_libro, ensure_ascii=False)
    
    def __str__(self):
        return (
            f"Titulo: {self.__titulo}\n"
            f"Autor: {self.__autor}\n"
            f"Genero: {self.__genero}\n"
            f"ISBN: {self.__isbn}\n"
            f"Año Publicacion: {self.__anioPublicacion}\n"
        )