from cancion import Cancion

class Playlist:
    def __init__(self, codigo:int, nombre:str):
        if not isinstance(codigo, int):
            raise TypeError("Codigo debe ser entero")
        if codigo < 0:
            raise ValueError("Codigo no debe ser negativo")
        if not isinstance(nombre,str):
            raise TypeError("Nombre debe ser string")
        if nombre == "" or nombre.isspace():
            raise ValueError("Nombre no debe estar vacio")
        
        self.__codigo = codigo
        self.__nombre = nombre
        self.__canciones = []
    
    def agregarCancion(self, cancion:'Cancion'):
        if not isinstance(cancion,Cancion):
            raise TypeError("Cancion debe ser instancia de Cancion")
        
        if not cancion in self.__canciones:
            self.__canciones.append(cancion)
        else:
            raise ValueError("La cancion no se puedo agregar porque ya existe en la playlist")
    
    def eliminarCancion(self, cancion:'Cancion'):
        if not isinstance(cancion,Cancion):
            raise TypeError("Cancion debe ser instancia de Cancion")
        if cancion in self.__canciones:
            self.__canciones.remove(cancion)
        else:
            raise ValueError("La cancion no se encontro en la lista")
    
    def obtenerCanciones(self):
        return self.__canciones