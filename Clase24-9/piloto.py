class Piloto:
    #Constructor
    def __init__(self, nombre:str, apellido:str, nro_inscripcion:int, experiencia:int, activo:bool):
        if not isinstance(nro_inscripcion, int) or nro_inscripcion < 0:
            raise ValueError("El Nro de Inscripcion deber un Entero Positivo")
        if not isinstance(experiencia, int) or experiencia < 0:
            raise ValueError("La experiencia de un Piloto debe ser un Entero Positivo")
        if not isinstance(activo,bool):
            raise TypeError("La actividad de un Piloto deber ser un booleano")
        
        self.__nombre = nombre
        self.__apellido = apellido
        self.__nro_inscripcion = nro_inscripcion
        self.__experiencia = experiencia
        self.__activo = activo
    
    def ObtenerNombre(self) -> str:
        return self.__nombre
    def ObtenerApelido(self) -> str:
        return self.__apellido
    def ObtenerNroInscripcion(self) -> int:
        return self.__nro_inscripcion
    def ObtenerExperiencia(self) -> int:
        return self.__experiencia
    def ObtenerActividad(self) -> bool:
        return self.__activo
    
    def ActualizarActividad(self, nuevoEstado:bool):
        self.__activo = nuevoEstado