class Cancion:
    def __init__(self, codigo:int, nombre:str, duracion:int, genero:str):
        if not isinstance(codigo, int):
            raise TypeError("Codigo debe ser entero")
        if codigo < 0:
            raise ValueError("Codigo no debe ser negativo")
        if not isinstance(nombre,str):
            raise TypeError("Nombre debe ser string")
        if nombre == "" or nombre.isspace():
            raise ValueError("Nombre no debe estar vacio")
        if not isinstance(duracion, int):
            raise TypeError("Duracion debe ser entero")
        if duracion <= 0:
            raise ValueError("Duracion no debe ser negativo")
        if not isinstance(genero,str):
            raise TypeError("Genero debe ser string")
        if genero == "" or genero.isspace():
            raise ValueError("Genero no debe estar vacio")
        
        self.__codigo = codigo
        self.__nombre = nombre
        self.__duracion = duracion
        self.__genero = genero
    
    def reproducir(self):
        print(f"reproduciendo cancion {self.__nombre}")
    
    def obtenerCodigo(self):
        return self.__codigo
    
    def obtenerNombre(self):
        return self.__nombre
    
    def obtenerDuracion(self):
        return self.__duracion
    
    def obtenerGenero(self):
        return self.__genero
    
    def __str__(self):
        return f"Codigo: {self.__codigo}\n - Nombre: {self.__nombre}\n - Duracion: {self.__duracion} segundos\n - Genero: {self.__genero}"