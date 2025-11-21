class Ciudad:
    @classmethod
    def fromDiccionario(cls, dicc:dict) -> 'Ciudad':
        return cls(dicc["nombre"], dicc["provincia"], dicc["puntosTuristicos"])
    
    def __init__(self, nombre:str, provincia:str, puntosTuristicos:str):
        if not isinstance(nombre,str) or nombre.strip() == "":
            raise ValueError("Nombre debe ser un string y no estar vacio!")
        if not isinstance(provincia,str) or provincia.strip() == "":
            raise ValueError("Provincia debe ser un string y no estar vacio!")
        if not isinstance(puntosTuristicos,str) or puntosTuristicos.strip() == "":
            raise ValueError("puntosTuristicos debe ser un string y no estar vacio!")
        
        self.__nombre = nombre
        self.__provincia = provincia
        self.__puntosTuristicos = puntosTuristicos
    
    def obtenerNombre(self) -> str:
        return self.__nombre
    
    def obtenerProvincia(self) -> str:
        return self.__provincia
    
    def obtenerPuntos(self) -> str:
        return self.__puntosTuristicos
    
    def esIgualProf(self, otraCiudad:'Ciudad') -> bool:
        mismoNombre = self.__nombre == otraCiudad.obtenerNombre()
        mismaProvincia = self.__provincia == otraCiudad.obtenerProvincia()
        mismosPuntos = self.__puntosTuristicos == otraCiudad.obtenerPuntos()
        
        return mismoNombre and mismaProvincia and mismosPuntos
    
    def toDiccionario(self):
        return {
            "nombre": self.__nombre,
            "provincia": self.__provincia,
            "puntosTuristicos": self.__puntosTuristicos
        }
    
    def __str__(self):
        return f"Ciudad: {self.obtenerNombre()}, {self.obtenerProvincia()}\n Puntos Turisticos: {self.obtenerPuntos()}"