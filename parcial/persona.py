from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre:str, edad:int):
        if not isinstance(nombre, str):
            raise TypeError("nombre debe ser de tipo string")
        if nombre.strip() == "":
            raise ValueError("nombre no puede estar vacio")
        if not isinstance(edad, int):
            raise TypeError("edad debe ser un numero entero")
        if edad < 0:
            raise ValueError("edad debe ser positivo")
        
        self._nombre = nombre
        self._edad = edad
    
    @abstractmethod
    def beber(self) -> str:
        pass
    
    @abstractmethod
    def hablar(self) -> str:
        pass
    
    @abstractmethod
    def saludar(self) -> str:
        pass
    
    def __str__(self):
        return f"Nombre: {self._nombre}\n Edad: {self._edad}\n"