class Pais:
    def __init__(self, codigo:int, nombre:str, cantDispositivos:int):
        if not isinstance(codigo, int):
            raise TypeError("Codigo debe ser entero")
        if codigo < 0:
            raise ValueError("Codigo no debe ser negativo")
        if not isinstance(nombre,str):
            raise TypeError("Nombre debe ser string")
        if nombre == "" or nombre.isspace():
            raise ValueError("Nombre no debe estar vacio")
        if not isinstance(cantDispositivos, int):
            raise TypeError("Cantidad de Dispositivos debe ser entero")
        if cantDispositivos <= 0:
            raise ValueError("Cantidad de Dispositivos no debe ser negativo")
        
        self.__codigo = codigo
        self.__nombre = nombre
        self.__cantDispositivos = cantDispositivos
    
    def obtenerCodigo(self):
        return self.__codigo
    
    def ontenerNombre(self):
        return self.__nombre
    
    def obtenerCantDispositivos(self):
        return self.__cantDispositivos
    
    def __str__(self):
        return f"Codigo: {self.__codigo}\n Nombre: {self.__nombre}\n Cantidad de Dispositivos: {self.__cantDispositivos}\n"