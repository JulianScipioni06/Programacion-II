from playlist import Playlist
from cancion import Cancion
from suscripcionGratuita import SuscripcionGratuita
from SuscripcionPaga import SuscripcionPaga
from pais import Pais
from dispositivo import Dispositivo

class Test:
    @staticmethod
    def ejecutar():
        print("-"*70)
        print("test spotify")
        print("-"*70)
        print("creamos canciones")
        cancion1 = Cancion(1, "cancion1", 400, "Bachata")
        cancion2 = Cancion(2, "cancion2", 300, "Metal")
        cancion3 = Cancion(3, "cancion3", 250, "pop")
        print("-"*70)
        print(cancion1)
        print(cancion2)
        print(cancion3)
        print("-"*70)

        print("creamos dispositivos")
        dispositivo1 = Dispositivo(1, "compu", "Laptop")
        dispositivo2 = Dispositivo(2,"celu", "smartphone")
        print(dispositivo1)
        print("-"*70)
        print(dispositivo2)
        print("-"*70)
        argentina = Pais(1, "Argentina", 4)
        eeuu = Pais(2, "Estados Unidos", 5)

        susGratuita = SuscripcionGratuita("Nicolas", "nico@", 123, argentina )
        susPaga = SuscripcionPaga("joaquin", "Joaquin@", 23456, eeuu)
        print("-"*70)
        print(susGratuita)
        print("-"*70)
        print(susPaga)
        print("-"*70)

        print("habilitar dispositivos")
        susGratuita.habilitarDispositivo(dispositivo1)
        susPaga.habilitarDispositivo(dispositivo2)

        print("reproducir musica de canciones")
        susGratuita.reproducirMusica(dispositivo1, cancion1)
        susPaga.reproducirMusica(dispositivo2,cancion2)
        print("-"*70)
        print("creamos playlists")
        cachengue = Playlist(1, "cachengue")
        cachengue.agregarCancion(cancion3)
        cachengue.agregarCancion(cancion2)
        print("-"*70)
        print("reproducimos playlist")
        print("-"*70)
        susGratuita.reproducirMusica(dispositivo1,None,cachengue)
        print("-"*70)
        print("descargamos playlist en susPaga")
        susPaga.descargarMusica(None,cachengue)
        susPaga.descargarMusica(cancion3)
        print("-"*70)
        print("seleccionamos cancion y reproducimos")
        susPaga.elegirCancion("cancion3")
        print("-"*70)
if __name__ == "__main__":
    Test.ejecutar()