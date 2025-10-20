class Dispositivo:
    def __init__(self, id:int, nombre:str, tipo:str):
        if not isinstance(id, int):
            raise TypeError("ID debe ser entero")
        if id < 0:
            raise ValueError("ID no debe ser negativo")
        if not isinstance(nombre,str):
            raise TypeError("Nombre debe ser string")
        if nombre == "" or nombre.isspace():
            raise ValueError("Nombre no debe estar vacio")
        if not isinstance(tipo,str):
            raise TypeError("Tipo debe ser string")
        if tipo == "" or tipo.isspace():
            raise ValueError("Tipo no debe estar vacio")
        
        self.__id = id
        self.__nombre = nombre
        self.__tipo = tipo
    
    def obtenerId(self):
        return self.__id
    
    def obtenerNombre(self):
        return self.__nombre
    
    def obtenerTipo(self):
        return self.__tipo
    
    def __str__(self):
        return f"ID Dispositivo: {self.__id}\n Nombre: {self.__nombre}\n Tipo: {self.__tipo}\n"