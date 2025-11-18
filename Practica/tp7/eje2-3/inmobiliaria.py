from inmueble import Inmueble

class Inmobiliaria:
    def __init__(self):
        self.__propiedades = []
    
    #Comandos
    def insertar(self, propiedad:Inmueble):
        if not isinstance(propiedad, Inmueble):
            raise TypeError("La propiedad a insertar debe ser un objeto de tipo Inmueble")
        if propiedad not in self.__propiedades:
            self.__propiedades.append(propiedad)
        else:
            raise ValueError("La propiedad ya existe en la lista!")
    
    def eliminar(self, propiedad:Inmueble):
        if not isinstance(propiedad, Inmueble):
            raise TypeError("La propiedad a insertar debe ser un objeto de tipo Inmueble")
        if propiedad in self.__propiedades:
            self.__propiedades.remove(propiedad)
        else:
            raise ValueError("La propiedad no existe!")
    
    def copiarValores(self, otraInmobiliaria:'Inmobiliaria'):
        if not isinstance(otraInmobiliaria, Inmobiliaria):
            raise TypeError("La inmobiliaria a copiar debe ser un objeto de tipo Inmueble")
        self.__propiedades = []
        
        for propiedad in otraInmobiliaria.obtenerPropiedades():
            self.__propiedades.append(propiedad.clonar())
    
    #Consultas
    def obtenerPropiedades(self):
        return self.__propiedades
    
    def estaInmueble(self, codigo:int)