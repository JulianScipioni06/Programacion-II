class ExamenAsignado:
    @classmethod
    def fromDiccionario(cls, data:dict):
        if not isinstance(data, dict):
            raise ValueError("Los datos deben ser un diccionario.")
        if "legajo" not in data or "numeroTema" not in data or "confirmado" not in data:
            raise ValueError("El diccionario debe contener las claves 'legajo', 'numeroTema' y 'confirmado'.")
        return cls(data["legajo"], data["numeroTema"], data["confirmado"])
    
    def __init__(self, legajo:int, numeroTema:int, confirmado:bool=False):
        if not isinstance(legajo, int) or legajo <= 0:
            raise ValueError("El legajo debe ser un entero positivo.")
        if not isinstance(numeroTema, int) or numeroTema <= 0:
            raise ValueError("El número de tema debe ser un entero positivo.")
        if not isinstance(confirmado, bool):
            raise ValueError("El valor de confirmado debe ser booleano.")
        self.__legajo = legajo
        self.__numeroTema = numeroTema
        self.__confirmado = confirmado

    def obtenerLegajo(self):
        return self.__legajo
    
    def obtenerNumeroTema(self):
        return self.__numeroTema
    
    def obtenerConfirmado(self):
        return self.__confirmado
    
    def establecerConfirmado(self, confirmado:bool):
        if not isinstance(confirmado, bool):
            raise ValueError("El valor de confirmado debe ser booleano.")
        self.__confirmado = confirmado

    def establerLegajo(self, legajo:int):
        if not isinstance(legajo, int) or legajo <= 0:
            raise ValueError("El legajo debe ser un entero positivo.")
        self.__legajo = legajo

    def establecerNumeroTema(self, numeroTema:int):
        if not isinstance(numeroTema, int) or numeroTema <= 0:
            raise ValueError("El número de tema debe ser un entero positivo.")
        self.__numeroTema = numeroTema

    def toDiccionario(self):
        return {
            "legajo": self.__legajo,
            "numeroTema": self.__numeroTema,
            "confirmado": self.__confirmado
        }
    
    