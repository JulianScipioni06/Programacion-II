from suscripcion import Suscripcion
from pais import Pais
from cancion import Cancion
from dispositivo import Dispositivo
from playlist import Playlist

class SuscripcionGratuita(Suscripcion):
    def __init__(self, nombre:str, email:str, telefono:int, pais:'Pais'):
        super().__init__(nombre, email, telefono, pais)
        
        self.__tiempoSinPublicidad = 500
        self.__tiempoReproducido = 0
    
    def reproducirMusica(self, dispositivo:'Dispositivo', cancion:'Cancion', playlist:'Playlist'):
        if not isinstance(dispositivo, Dispositivo):
            raise TypeError("Dispositivo debe ser instancia de Dispositivo")
        if cancion == None and playlist == None:
            raise ValueError("Debe reproducir una playlist o una cancion")
        if cancion != None and playlist != None:
            raise ValueError("No se puede reproducir Canciones y Playlist a la misma vez")
        if cancion != None:
            if not isinstance(cancion, Cancion):
                raise TypeError("Cancion debe ser instancia de Cancion")
            self.__reproducirCancion(cancion)
        else:
            if not isinstance(playlist,Playlist):
                raise TypeError("Playlist debe ser de tipo Playlist")
            for can in playlist.obtenerCanciones():
                if isinstance(can, Cancion):
                    self.__reproducirCancion(can)
            
    def interrumpirConPublicidad(self):
        print("Espacio Publicitario, para disfrutar de tiempo sin limites pasate al plan premium")
        self.__tiempoReproducido = 0
    
    def __reproducirCancion(self, cancion:'Cancion'):
        cancion.reproducir()
        self.__tiempoReproducido += cancion.obtenerDuracion()
        if self.__tiempoReproducido >= self.__tiempoSinPublicidad:
            self.interrumpirConPublicidad()
    
    def __str__(self):
        return (f"Subscripcion Gratuita\n {super().__str__()} timepo sin publicidad: {self.__tiempoSinPublicidad} timepo sin publicidad: {self.__tiempoReproducido}")