from fecha import Fecha

class Socio:
    #Constructor
    def __init__(self, nombre:str, fechaNacimiento:Fecha, fechaPenalizacion:Fecha = None):
        """
        Inicializa un Nuevo Objeto Socio.
        Parametros:
        - nombre = Nombre del Socio
        - fechaNacimiento = Fecha de Nacimiento del Socio
        - fechaPenalizacion = Fecha en la que fue penalizado el Socio
        """
        self.__nombre = nombre
        
        if not isinstance(fechaNacimiento,Fecha):
            raise TypeError("La fecha de Nacimiento debe ser de Tipo Fecha")
        self.__fechaNacimiento = fechaNacimiento
        
        if not isinstance(fechaPenalizacion,Fecha) and fechaPenalizacion is not None:
            raise TypeError("La fecha de Penalizacion debe ser de Tipo Fecha")
        self.__fechaPenalizacion = fechaPenalizacion
    
    #Comandos
    def establecerNombre(self, nombre:str):
        """Establece lo recibido por parametro como nombre."""
        self.__nombre = nombre
    
    def establecerFechaNacimiento(self, fecha:Fecha):
        """Establece lo recibido por parametro como fechaNacimiento."""
        if not isinstance(fecha, Fecha):
            raise TypeError("Tipo de Dato Invalido, debe ser de tipo 'Fecha'")
        self.__fechaNacimiento = fecha
    
    def establecerFechaPenalizacion(self, fecha:Fecha):
        """Establece lo recibido por parametro como fechaPenalizacion."""
        if not isinstance(fecha, Fecha):
            raise TypeError("Tipo de Dato Invalido, debe ser de tipo 'Fecha'")
        self.__fechaPenalizacion = fecha
    
    #Consultas
    def estaHabilitado(self, fecha:Fecha) -> bool:
        """Retorna True cuando no tiene fechaPenalizacion o cuando ésta es anterior a la fecha recibida en el parámetro."""
        if not isinstance(fecha,Fecha):
            raise TypeError("Tipo de Dato Invalido, debe ser de tipo 'Fecha'")
        return self.__fechaPenalizacion is None or self.__fechaPenalizacion.esAnterior(fecha)
    
    def obtenerNombre(self) -> str:
        """Devuelve el Nombre del Socio"""
        return self.__nombre
    
    def obtenerFechaNacimiento(self) -> Fecha:
        """Devuelve la Fecha de Nacimiento del Socio"""
        return self.__fechaNacimiento
    
    def obtenerFechaPenalizacion(self) -> Fecha:
        """Devuelve la Fecha de Penalizacion del Socio"""
        return self.__fechaPenalizacion
    
    def __str__(self):
        return f"DATOS DEL SOCIO: \n Nombre: {self.__nombre} \n Fecha de Nacimiento: {self.__fechaNacimiento} \n Fecha de Penalizacion: {self.__fechaPenalizacion} \n"