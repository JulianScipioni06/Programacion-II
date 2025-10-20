from abc import ABC, abstractmethod
from pais import Pais
from dispositivo import Dispositivo
from cancion import Cancion
from playlist import Playlist

class Suscripcion(ABC):
    def __init__(self, nombre:str, email:str, telefono:int, pais:'Pais'):
        if not isinstance(nombre,str):
            raise TypeError("Nombre debe ser string")
        if nombre == "" or nombre.isspace():
            raise ValueError("Nombre no debe estar vacio")
        if not isinstance(email,str):
            raise TypeError("Email debe ser un string")
        if email == "" or email.isspace():
            raise ValueError("Email no debe estar vacio")
        if not "@" in email:
            raise ValueError("Email no valido")
        if not isinstance(telefono, int):
            raise TypeError("Telefono debe ser entero")
        if telefono <= 0:
            raise ValueError("Telefono no debe ser negativo")
        if not isinstance(pais,Pais):
            raise TypeError("Pais debe ser de tipo 'Pais'")
        
        self._nombre = nombre
        self._email = email
        self._telefono = telefono
        self._pais = pais
    
    @abstractmethod
    def reproducirMusica(self, dispositivo:'Dispositivo', cancion: 'Cancion|None' = None, playlist: 'Playlist|None' = None):
        pass
    
    def __str__(self):
        return f"Nombre: {self._nombre}\n Email: {self._email}\n Telefono: {self._telefono}\n Pais: {self._pais.ontenerNombre()}\n"