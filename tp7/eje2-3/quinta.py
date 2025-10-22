from inmueble import Inmueble

class Quinta(Inmueble):
    def __init__(self, codigo:int, domicilio:str = "-", propietario:str = "", metrosCuadrados:int = 0, estado:int = 0, metrosParque: float = 0):
        super().__init__(codigo, domicilio, propietario, metrosCuadrados, estado)
        
        if not isinstance(metrosParque,int):
            raise TypeError("Metros parque debe ser un entero.")
        if metrosParque < 0:
            raise ValueError("Metros Parque no puede ser negativo")
        
        self.__metrosParque = metrosParque
    
    #Comandos Triviales
    def establecerMetrosParque(self, metros:int):
        if not isinstance(metros,int):
            raise TypeError("Metros parque debe ser un entero.")
        if metros < 0:
            raise ValueError("Metros Parque no puede ser negativo")
        
        self.__metrosParque = metros
    
    def copiarValores(self, otraQuinta: 'Quinta'):
        if not isinstance(otraQuinta, Quinta):
            raise TypeError("otraQuinta debe ser una instancia de Quinta")
        
        super().copiarValores(otraQuinta)
        self.__metrosParque = otraQuinta.obtenerMetrosParque()
    
    #Consultas Triviales
    def obtenerMetrosParque(self) -> float:
        return self.__metrosParque
    
    def esIgualQue(self, otraQuinta: 'Quinta'):
        mismoAtributos = super().esIgualQue(otraQuinta)
        mismosMetros = self.__metrosParque == otraQuinta.obtenerMetrosParque()
        
        return mismoAtributos and mismosMetros
    
    def clonar(self) -> 'Quinta':
        return Quinta(self._codigo, self._domicilio, self._propietario, self._metrosCuadrados, self._estado, self.__metrosParque)
    
    def __str__(self):
        return (
            f"{super().__str__()}\n"
            f"Metros Parque: {self.__metrosParque}\n"
        )
    
    def __repr__(self):
        return f"Quinta('{self._codigo}', '{self._domicilio}', '{self._propietario}', '{self._metrosCuadrados}', '{self._estado}', '{self.__metrosParque}')"
    
    #Consultas
    def costoAlquiler(self, base):
        """Calcula el costo del alquiler sumando la base más 100 por cada m² del inmueble."""
        if not isinstance(base, (int,float)):
            raise TypeError("Base debe ser un numero")
        if base < 0:
            raise ValueError("Base debe ser positivo")
        
        adicional = self.__metrosParque // 15
        
        return super().costoAlquiler(base) + 500 * adicional
    
    def precioVenta(self, m2):
        return super().precioVenta(m2) + (self.__metrosParque * m2) / 2