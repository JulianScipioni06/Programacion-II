from abc import ABC, abstractmethod
from datetime import date

class Empleado(ABC):
    def __init__(self, nombre:str, apellido:str, dni:int, anioIngreso:int):
        if not isinstance(nombre,str) or nombre.strip() == "":
            raise ValueError("El nombre debe ser un string valido.")
        if not isinstance(apellido,str) or apellido.strip() == "":
            raise ValueError("El apellido debe ser un string valido.")
        if not isinstance(dni,int) or dni < 0:
            raise ValueError("El dni debe ser un numero valido")
        if not isinstance(anioIngreso,int) or anioIngreso <= 0 or anioIngreso > date.today().year:
            raise ValueError("El Año de Ingreso debe ser un numero valido")
        
        self._nombre = nombre
        self._apellido = apellido
        self._dni = dni
        self._anioIngreso = anioIngreso
    
    
    @abstractmethod 
    def obtenerSalario(self) -> float:
        pass
    
    def nombreCompleto(self) -> str:
        return f"{self._apellido} {self._nombre}"
    
    def antiguedadEnAnios(self) -> int:
        anioActual = date.today().year
        return anioActual - self._anioIngreso
    
    def __str__(self):
        return f"{self.nombreCompleto()} - DNI: {self._dni} - Año de Ingreso: {self._anioIngreso} - Antiguedad: {self.antiguedadEnAnios()}"