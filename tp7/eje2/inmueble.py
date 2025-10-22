class Inmueble:
    def __init__(self, codigo: int, domicilio: str = "-", propietario: str = "", metrosCuadrados: int = 0, estado: int = 0):
        if not isinstance(codigo, int):
            raise TypeError("Codigo debe ser un entero")
        if codigo < 0:
            raise ValueError("Codigo debe ser positivo")
        if not isinstance(domicilio, str):
            raise TypeError("Domicilio debe ser string")
        if domicilio == "" or domicilio.isspace():
            raise ValueError("Domicilio no puede estar vacio")
        if not isinstance(propietario, str):
            raise TypeError("propietario debe ser string")
        if propietario == "" or propietario.isspace():
            raise ValueError("propietario no puede estar vacio")
        if not isinstance(metrosCuadrados, int):
            raise TypeError("Metros Cuadrados debe ser un entero")
        if metrosCuadrados < 0:
            raise ValueError("Metros cuadrados debe ser positivo")
        if not isinstance(estado, int):
            raise TypeError("estado debe ser un entero")
        if estado not in (0, 1, 2):
            raise ValueError("Estado debe ser 0 (libre), 1 (alquilado) o 2 (en venta)")
        
        self._codigo = codigo
        self._domicilio = domicilio
        self._propietario = propietario
        self._metrosCuadrados = metrosCuadrados
        self._estado = estado
    
    #Comandos Triviales
    def establecerCodigo(self, codigo: int):
        if not isinstance(codigo, int):
            raise TypeError("Codigo debe ser un entero")
        if codigo < 0:
            raise ValueError("Codigo debe ser positivo")
        self._codigo = codigo
        
    def establecerDomicilio(self, domicilio: str):
        if not isinstance(domicilio, str):
            raise TypeError("Domicilio debe ser string")
        if domicilio == "" or domicilio.isspace():
            raise ValueError("Domicilio no puede estar vacio")
        self._domicilio = domicilio
        
    def establecerPropietario(self, propietario: str):
        if not isinstance(propietario, str):
            raise TypeError("propietario debe ser string")
        if propietario == "" or propietario.isspace():
            raise ValueError("propietario no puede estar vacio")
        self._propietario = propietario
        
    def establecerMetrosCuadrados(self, metrosCuadrados: int):
        if not isinstance(metrosCuadrados, int):
            raise TypeError("Metros Cuadrados debe ser un entero")
        if metrosCuadrados < 0:
            raise ValueError("Metros cuadrados debe ser positivo")
        
        self._metrosCuadrados = metrosCuadrados
        
    def establecerEstado(self, estado: int):
        if not isinstance(estado, int):
            raise TypeError("estado debe ser un entero")
        if estado not in (0, 1, 2):
            raise ValueError("Estado debe ser 0 (libre), 1 (alquilado) o 2 (en venta)")
        
        self._estado = estado
    
    def copiarValores(self, otroInmueble: 'Inmueble'):
        self._codigo = otroInmueble.obtenerCodigo()
        self._domicilio = otroInmueble.obtenerDomicilio()
        self._propietario = otroInmueble.obtenerPropietario()
        self._metrosCuadrados = otroInmueble.obtenerMetrosCuadrados()
        self._estado = otroInmueble.obtenerEstado()
    
    #Consultas Triviales
    def obtenerCodigo(self) -> int:
        return self._codigo
    
    def obtenerDomicilio(self) -> str:
        return self._domicilio
    
    def obtenerPropietario(self) -> str:
        return self._propietario
    
    def obtenerMetrosCuadrados(self) -> int:
        return self._metrosCuadrados
    
    def obtenerEstado(self) -> int:
        return self._estado
    
    def esIgualQue(self, otroInmueble: 'Inmueble') -> bool:
        mismoCodigo = self._codigo == otroInmueble.obtenerCodigo()
        mismoDomicilio =self._domicilio == otroInmueble.obtenerDomicilio()
        mismoPropietario = self._propietario == otroInmueble.obtenerPropietario()
        mismosMetrosCuadrados = self._metrosCuadrados == otroInmueble.obtenerMetrosCuadrados()
        mismoEstado = self._estado == otroInmueble.obtenerEstado()
        
        return mismoCodigo and mismoDomicilio and mismoPropietario and mismosMetrosCuadrados and mismoEstado
    
    def clonar(self) -> 'Inmueble':
        return Inmueble(self._codigo, self._domicilio, self._propietario, self._metrosCuadrados, self._estado)
    
    #Consultas
    def costoAlquiler(self, base: int) -> float:
        """Calcula el costo del alquiler sumando la base más 100 por cada m² del inmueble."""
        if not isinstance(base, (int,float)):
            raise TypeError("Base debe ser un numero")
        if base < 0:
            raise ValueError("Base debe ser positivo")
        
        return base + 100 * self.obtenerMetrosCuadrados() 
    
    def precioVenta(self, m2: float) -> float:
        if not isinstance(m2, (int,float)):
            raise TypeError("m2 debe ser un numero")
        if m2 < 0:
            raise ValueError("m2 debe ser positivo")
        
        return self._metrosCuadrados * m2
    
    #Metodos str y repr
    def __str__(self) -> str:
        return (
            f"Codigo: {self._codigo}\n"
            f"Domicilio: {self._domicilio}\n"
            f"Propietario: {self._propietario}\n"
            f"Metros Cuadrados: {self._metrosCuadrados}\n"
            f"Estado: {self._estado}\n"
        )
    
    def __repr__(self) -> str:
        return f"Inmueble('{self._codigo}', '{self._domicilio}', '{self._propietario}', '{self._metrosCuadrados}', '{self._estado}')"