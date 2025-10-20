class Dispositivo:
    def __init__(self, id:int, nombre:str, tipo:str):
        if not isinstance(id, int):
            raise TypeError("id debe ser entero")
        if id < 0:
            raise ValueError("id no debe ser negativo")
        if not isinstance(nombre, str):
            raise TypeError("nombre debe ser string")
        if nombre == "" or nombre.isspace():
            raise ValueError("nombre no debe estar vacio")
        if not isinstance(tipo, str):
            raise TypeError("tipo debe ser string")
        if tipo == "" or tipo.isspace():
            raise ValueError("tipo no debe estar vacio")
        self.__id = id
        self.__nombre = nombre
        self.__tipo = tipo

    def obtenerNombre(self):
        return self.__nombre
    
    def __str__(self):
        return (
            f"id: {self.__id}\n"
            f"nombre: {self.__nombre}\n"
            f"tipo: {self.__tipo}\n"
        )