from inmueble import Inmueble

class Departamento(Inmueble):
    def __init__(self, codigo:int, domicilio:str = "-", propietario:str = "", metrosCuadrados:int = 0, estado:int = 0, gastosComunes: float = 0.0, cochera: bool = False):
        super().__init__(codigo, domicilio, propietario, metrosCuadrados, estado)
        
        if not isinstance(gastosComunes,(int, float)):
            raise TypeError("Gastos Comunes debe ser un numero.")
        if gastosComunes < 0:
            raise ValueError("Gastos Comunes no puede ser negativo")
        if not isinstance(cochera,bool):
            raise TypeError("Cochera debe ser un boolean")
        
        self.__gastosComunes = gastosComunes
        self.__cochera = cochera
    
    #Comandos Triviales
    def establecerGastosComunes(self, gastos:float):
        if not isinstance(gastos,(int, float)):
            raise TypeError("Gastos Comunes debe ser un numero.")
        if gastos < 0:
            raise ValueError("Gastos Comunes no puede ser negativo")
        
        self.__gastosComunes = gastos
    
    def establecerCochera(self, tieneCochera:bool):
        if not isinstance(tieneCochera,bool):
            raise TypeError("Cochera debe ser un boolean")
        
        self.__cochera = tieneCochera
    
    def copiarValores(self, otroDepartamento: 'Departamento'):
        if not isinstance(otroDepartamento, Departamento):
            raise TypeError("otroDepartamento debe ser una instancia de Departamento")
        
        super().copiarValores(otroDepartamento)
        self.__gastosComunes = otroDepartamento.obtenerGastosComunes()
        self.__cochera = otroDepartamento.obtenerCochera()
    
    #Consultas Triviales
    def obtenerGastosComunes(self) -> float:
        return self.__gastosComunes
    
    def obtenerCochera(self) -> bool:
        return self.__cochera
    
    def esIgualQue(self, otroDepartamento: 'Departamento'):
        mismoAtributos = super().esIgualQue(otroDepartamento)
        mismosGastos = self.__gastosComunes == otroDepartamento.obtenerGastosComunes()
        mismaCochera = self.__cochera == otroDepartamento.obtenerCochera()
        
        return mismoAtributos and mismosGastos and mismaCochera
    
    def clonar(self) -> 'Departamento':
        return Departamento(self._codigo, self._domicilio, self._propietario, self._metrosCuadrados, self._estado, self.__gastosComunes, self.__cochera)
    
    def __str__(self):
        return (
            f"{super().__str__()}\n"
            f"Gastos Comunes: {self.__gastosComunes}\n"
            f"Cochera: {self.__cochera}\n"
        )
    
    def __repr__(self):
        return f"Departamento('{self._codigo}', '{self._domicilio}', '{self._propietario}', '{self._metrosCuadrados}', '{self._estado}', '{self.__gastosComunes}', '{self.__cochera}')"
    
    #Consultas
    def costoAlquiler(self, base):
        """Calcula el costo del alquiler sumando la base más 100 por cada m² del inmueble."""
        if not isinstance(base, (int,float)):
            raise TypeError("Base debe ser un numero")
        if base < 0:
            raise ValueError("Base debe ser positivo")
        
        if self.__cochera:
            return super().costoAlquiler(base) + 2000
        else:
            return super().costoAlquiler(base)
    
    def precioVenta(self, m2):
        return super().precioVenta(m2)