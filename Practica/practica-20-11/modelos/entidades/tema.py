class Tema:
    @classmethod
    def fromDiccionario(cls, data:dict):
        if not isinstance(data, dict):
            raise ValueError("Los datos deben ser un diccionario.")
        if "numero" not in data or "nombre" not in data or "enunciado" not in data:
            raise ValueError("El diccionario debe contener las claves 'numero', 'nombre' y 'enunciado'.")
        return cls(data["numero"],data["nombre"],data["enunciado"])
    
    def __init__(self, numero:int, nombre:str, enunciado:str):
        if not isinstance(numero, int) or numero <= 0:
            raise ValueError("El número debe ser un entero positivo.")
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre debe ser una cadena no vacía.")
        if not isinstance(enunciado, str) or enunciado.strip() == "":
            raise ValueError("El enunciado debe ser una cadena no vacía.")
        self.__numero = numero
        self.__nombre = nombre
        self.__enunciado = enunciado

    def obtenerNumero(self):
        return self.__numero
    
    def obtenerNombre(self):
        return self.__nombre
    
    def obtenerEnunciado(self):
        return self.__enunciado
    
    def establecerNombre(self, nombre:str):
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre debe ser una cadena no vacía.")
        self.__nombre = nombre

    def establecerEnunciado(self, enunciado:str):
        if not isinstance(enunciado, str) or enunciado.strip() == "":
            raise ValueError("El enunciado debe ser una cadena no vacía.")
        self.__enunciado = enunciado

    def toDiccionario(self):
        return {
            "numero": self.__numero,
            "nombre": self.__nombre,
            "enunciado": self.__enunciado
        }
    
    