class Alumno:
    __ID = 0
    
    @classmethod
    def fromDiccionario(cls, diccionario:dict):
        if not isinstance(diccionario, dict):
            raise ValueError("El argumento debe ser un diccionario.")
        if "legajo" not in diccionario or "nombre" not in diccionario or "apellido" not in diccionario:
            raise ValueError("El diccionario debe contener las claves 'legajo', 'nombre' y 'apellido'.")
        return cls(
            legajo=diccionario["legajo"],
            nombre=diccionario["nombre"],
            apellido=diccionario["apellido"],
            id=diccionario.get("id", None)
        )

    @classmethod
    def establecerUltimoID(cls, ultimo_id):
        if not isinstance(ultimo_id, int) or ultimo_id < 0:
            raise ValueError("El ID debe ser un entero no negativo.")
        cls.__ID = ultimo_id

    @classmethod
    def obtenerUltimoID(cls):
        return cls.__ID
    
    @classmethod
    def generarID(cls):
        cls.__ID += 1
        return cls.__ID
    
    def __init__(self, legajo:int, nombre:str, apellido:str, id:int|None=None):
        # Validaciones básicas
        if not isinstance(legajo, int) or legajo <= 0:
            raise ValueError("El legajo debe ser un entero positivo.")
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre debe ser una cadena no vacía.")
        if not isinstance(apellido, str) or apellido.strip() == "":
            raise ValueError("El apellido debe ser una cadena no vacía.")
        if id is not None and (not isinstance(id, int) or id <= 0):
            raise ValueError("El ID debe ser un entero positivo si se proporciona.")
        if id is None:
            id = self.generarID()
        self.__id = id
        self.__legajo = legajo
        self.__nombre = nombre
        self.__apellido = apellido

    def obtenerID(self):
        return self.__id
    
    def obtenerLegajo(self):
        return self.__legajo
    
    def obtenerNombre(self):
        return self.__nombre
    
    def obtenerApellido(self):
        return self.__apellido
    
    def establecerLegajo(self, legajo:int):
        if not isinstance(legajo, int) or legajo <= 0:
            raise ValueError("El legajo debe ser un entero positivo.")
        self.__legajo = legajo

    def establecerNombre(self, nombre:str):
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre debe ser una cadena no vacía.")
        self.__nombre = nombre

    def establecerApellido(self, apellido:str):
        if not isinstance(apellido, str) or apellido.strip() == "":
            raise ValueError("El apellido debe ser una cadena no vacía.")
        self.__apellido = apellido

    def __str__(self):
        return f"ID: {self.__id}, Legajo: {self.__legajo}, Nombre: {self.__nombre}, Apellido: {self.__apellido}"
    
    def toDiccionario(self):
        return {
            "id": self.__id,
            "legajo": self.__legajo,
            "nombre": self.__nombre,
            "apellido": self.__apellido
        }
    