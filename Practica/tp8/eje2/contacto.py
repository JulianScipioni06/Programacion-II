import json

class Contacto:
    @classmethod
    def from_diccionario(cls, dicc:dict):
        if not isinstance(dicc,dict):
            raise Exception("La funcion debe recibir un diccionario!")
        
        return cls(dicc["nombre"], dicc["apellido"], dicc["telefono"], dicc["correo_electronico"], dicc["direccion"])
    
    def __init__(self, nombre:str, apellido:str, telefono:str, correo_electronico:str, direccion:str):
        if not isinstance(nombre,str) or nombre.strip() == "":
            raise ValueError("Nombre debe ser un string y no estar vacio!")
        if not isinstance(apellido,str) or apellido.strip() == "":
            raise ValueError("apellido debe ser un string y no estar vacio!")
        if not isinstance(telefono,str) or telefono.strip() == "":
            raise ValueError("telefono debe ser un string y no estar vacio!")
        if not isinstance(correo_electronico,str) or correo_electronico.strip() == "":
            raise ValueError("correo_electrónico debe ser un string y no estar vacio!")
        if not isinstance(direccion,str) or direccion.strip() == "":
            raise ValueError("direccion debe ser un string y no estar vacio!")
        
        self.__nombre = nombre
        self.__apellido = apellido
        self.__telefono = telefono
        self.__correo_electronico = correo_electronico
        self.__direccion = direccion
    
    def to_diccionario(self):
        return {
            "nombre": self.__nombre,
            "apellido": self.__apellido,
            "telefono": self.__telefono,
            "correo_electronico": self.__correo_electronico,
            "direccion": self.__direccion,
            }
    
    def __str__(self):
        return (
            f"Nombre: {self.__nombre}\n"
            f"Apellido: {self.__apellido}\n"
            f"Telefono: {self.__telefono}\n"
            f"Correo Electronico: {self.__correo_electronico}\n"
            f"Direccion: {self.__direccion}\n"
        )