class Autmovil:
    
    #Constructor
    def __init__(self, marca:str, modelo:str, anio:int, velocidadMaxima:float, velocidadActual:float):
        if not isinstance(anio,int) or anio > 0:
            raise ValueError("El año debe ser un Entero Positivo.")
        if not isinstance(velocidadMaxima, float) or velocidadMaxima > 0:
            raise ValueError("El año debe ser un Numero Positivo.")
        if not isinstance(velocidadActual, float) or velocidadActual > 0:
            raise ValueError("El año debe ser un Numero Positivo.")
        
        self.__marca = marca
        self.__modelo = modelo
        self.__anio = anio
        self.__velocidadMaxima = velocidadMaxima
        self.__velocidadActual = velocidadActual
        
    #Comandos
    def EstablecerMarca(self, marca:str):
        self.__marca = marca
    
    def EstablecerModelo(self, modelo:str):
        self.__modelo = modelo
    
    def EstablecerAnio(self, anio:int):
        self.__anio = anio
    
    def EstablecerVelocidadMaxima(self, velMaxima:float):
        self.__velocidadMaxima = velMaxima
    
    def EstablecerVelocidadActual(self, velActual:float):
        self.__velocidadActual = velActual
    
    def Acelerar(self,incrementoVelocidad:int):
        self.__velocidadActual += incrementoVelocidad
    
    def Desacelerar(self,decrementoVelocidad:int):
        self.__velocidadActual += decrementoVelocidad
    
    def FrenarPorCompleto(self):
        self.__velocidadActual = 0
    
    #Consultas
    