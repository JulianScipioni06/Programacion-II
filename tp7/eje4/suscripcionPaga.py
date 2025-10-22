from suscripcion import Suscripcion
from pais import Pais
from cancion import Cancion
from playlist import Playlist
from dispositivo import Dispositivo

class SuscripcionPaga(Suscripcion):
    def __init__(self, nombre:str, email:str, telefono:int, pais: 'Pais'):
        super().__init__(nombre, email, telefono, pais)
        self.__maxDispositivos = pais.obtenerCantDispositivos()
        self.__dispositivos = []
        self.__cancionesDescargadas = []

    def reproducirMusica(self, dispositivo: 'Dispositivo', cancion: 'Cancion | None' = None, playlist: 'Playlist | None' = None):
        if not isinstance(dispositivo, Dispositivo):
            raise TypeError("dispositivo debe ser instancia de Dispositivo")
        if cancion == None and playlist == None:
            raise ValueError("debe reproducir una cancion o playlist")
        if cancion != None and playlist !=None:
            raise ValueError("no se puede reproducir canciones y playlis a la vez")
        if not dispositivo in self.__dispositivos:
            raise ValueError("el dispositivo no esta habilitado")
        if cancion != None:
            if not isinstance(cancion, Cancion):
                raise TypeError("cancion debe ser instancia de Cancion")
            print(f"Dispositivo: {dispositivo.obtenerNombre()}")
            cancion.reproducir()
        else:
            if not isinstance(playlist, Playlist):
                raise TypeError("playlist debe ser instancia de Playlist")
            print(f"Dispositivo: {dispositivo.obtenerNombre()}")
            for can in playlist.obtenerCanciones():
                if isinstance(can, Cancion):
                    can.reproducir()
        
    def descargarMusica(self,cancion: 'Cancion | None' = None, playlist: 'Playlist | None' = None ):
        if cancion == None and playlist == None:
            raise ValueError("debe reproducir una cancion o playlist")
        if cancion != None and playlist !=None:
            raise ValueError("no se puede reproducir canciones y playlis a la vez")
        if cancion != None:
            if not isinstance(cancion, Cancion):
                raise TypeError("cancion debe ser instancia de Cancion")
            if not cancion in self.__cancionesDescargadas:
                self.__cancionesDescargadas.append(cancion)
            else:
                print("la cancion ya estaba descargada")
        else:
            if not isinstance(playlist, Playlist):
                raise TypeError("playlist debe ser instancia de Playlist")
            for can in playlist.obtenerCanciones():
                if isinstance(can, Cancion):
                    if not can in self.__cancionesDescargadas:
                        print("descargando cancion")
                        self.__cancionesDescargadas.append(can)
                    else:
                        print("la cancion ya estaba descargada")
    
    def elegirCancion(self, nombre:str):
        repetir = True
        i = 0
        while repetir and i < len(self.__cancionesDescargadas):
            if self.__cancionesDescargadas[i].obtenerNombre()== nombre:
                print("Cancion seleccionada")
                self.__cancionesDescargadas[i].reproducir()
                repetir = False
            i += 1
        if repetir == True:
            print("cancion no encontrada")

    def habilitarDispositivo(self, dispositivo: Dispositivo):
        if not isinstance(dispositivo, Dispositivo):
            raise TypeError("dispositivo debe ser Dispositivo")
        if not dispositivo in self.__dispositivos:
            if len(self.__dispositivos) < self._pais.obtenerCantDispositivos():
                self.__dispositivos.append(dispositivo)
            else:
                print("dispositivos maximos alcanzados")
        else:
            print("el dispositivo ya estab habilitado")

    def __str__(self):
        return (
            f"Suscripcion Paga \n"
            f"{super().__str__()}"
            f"Max dispositivos: {self._pais.obtenerCantDispositivos()} \n"
            f"dispositivos: {self.__dispositivos}\n"
            )