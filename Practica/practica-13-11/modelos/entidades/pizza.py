class Pizza:
    __clase_id = 0
    
    @classmethod
    def __obtenerUltimoId(cls) -> int:
        Pizza.__clase_id += 1
        return Pizza.getUltimoId()
    
    @classmethod
    def getUltimoId(cls)->int:
        return Pizza.__clase_id
    
    @classmethod
    def establecerUltimoId(cls, id:int):
        Pizza.__clase_id = id
    
    @classmethod
    def fromDiccionario(cls, dicc:dict) -> 'Pizza':
        return cls(dicc["id"],dicc["nombre"],dicc["precio"],dicc["puntuacion"],dicc["horneada"],)
    
    def __init__(self, id:int|None, nombre:str, precio:float, puntuacion:int, horneada:bool):
        if not isinstance(nombre,str) or nombre.strip() == "":
            raise ValueError("Nombre debe ser un string no nulo")
        if not isinstance(precio, (int,float)) or precio < 0:
            raise ValueError("precio debe ser numero mayor que 0")
        if not isinstance(puntuacion, int) or puntuacion < 0 or puntuacion > 10:
            raise ValueError("puntuacion debe ser entero entre 0 y 10")
        if not isinstance(horneada,bool):
            raise ValueError("horneada debe ser boolean")
        
        if id is None:
            self.__id = Pizza.__obtenerUltimoId()
        else:
            self.__id = id

        # ESTOS SIEMPRE TIENEN QUE ASIGNARSE
        self.__nombre = nombre
        self.__precio = precio
        self.__puntuacion = puntuacion
        self.__horneada = horneada
    
    #Comandos Triviales
    def establecerNombre(self, nombre:str):
        if not isinstance(nombre,str) or nombre.strip() == "":
            raise ValueError("Nombre debe ser un string no nulo")
        
        self.__nombre = nombre
    
    def establecerPrecio(self, precio:float):
        if not isinstance(precio, (int,float)) or precio < 0:
            raise ValueError("precio debe ser numero mayor que 0")
        
        self.__precio = precio
    
    def establecerPuntuacion(self, puntuacion:int):
        if not isinstance(puntuacion, int) or puntuacion < 0 or puntuacion > 10:
            raise ValueError("puntuacion debe ser entero entre 0 y 10")
        
        self.__puntuacion = puntuacion
    
    def establecerHorneada(self, horneada:bool):
        if not isinstance(horneada,bool):
            raise ValueError("horneada debe ser boolean")
        
        self.__horneada = horneada
    
    def obtenerId(self) -> int:
        return self.__id
    
    def obtenerNombre(self) -> str:
        return self.__nombre
    
    def obtenerPrecio(self) -> float:
        return self.__precio
    
    def obtenerPuntuacion(self) -> int:
        return self.__puntuacion

    def obtenerHorneada(self) -> bool:
        return self.__horneada

    def __str__(self):
        return f"Datos de Pizza{self.__nombre}:\n - ID: {self.__id}\n - Precio: {self.__precio}\n - Puntuacion: {self.__puntuacion}\n - Horneada: {self.__horneada}\n"
    
    def toDiccionario(self) -> dict:
        return {
            "id": self.__id,
            "nombre": self.__nombre,
            "precio": self.__precio,
            "puntuacion": self.__puntuacion,
            "horneada": self.__horneada
        }