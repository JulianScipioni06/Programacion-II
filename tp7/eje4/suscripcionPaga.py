from suscripcion import Suscripcion
from pais import Pais
from cancion import Cancion
from playlist import Playlist

class SuscripcionPaga(Suscripcion):
    def __init__(self, nombre:str, email:str, telefono:int, pais:'Pais'):
        super().__init__(nombre, email, telefono, pais)
        self.__maxDispositivos = pais.obtenerCantDispositivos()
        self.__dispositivos = []
    
    
    