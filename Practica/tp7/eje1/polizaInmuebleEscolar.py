from polizaInmueble import PolizaInmueble

class PolizaInmuebleEscolar(PolizaInmueble):
    def __init__(self, numero: int, incendio: float = 0, explosion: float = 0, robo: float = 0, cantPersonas: int = 0, montoEquipamiento:float = 0.0, montoMobiliario:float = 0.0, montoPersona:float = 0.0):
        super().__init__(numero,incendio,explosion,robo)
        if not isinstance(cantPersonas, int):
            raise TypeError("Cantidad de Personas debe ser Entero")
        if cantPersonas < 0:
            raise ValueError("Cantidad de Personas debe ser positivo")
        if not isinstance(montoEquipamiento, (int, float)):
            raise TypeError("El monto por equipamiento debe ser un numero")
        if montoEquipamiento < 0:
            raise ValueError("El monto por equipamiento no puede ser negativo")
        if not isinstance(montoMobiliario, (int, float)):
            raise TypeError("El monto por mobiliario debe ser un numero")
        if montoMobiliario < 0:
            raise ValueError("El monto por mobiliario no puede ser negativo")
        if not isinstance(montoPersona, (int, float)):
            raise TypeError("El monto por persona debe ser un numero")
        if montoPersona < 0:
            raise ValueError("El monto por equipamiento no puede ser negativo")
        
        self.__cantPersonas = cantPersonas
        self.__montoEquipamiento = montoEquipamiento
        self.__montoMobiliario = montoMobiliario
        self.__montoPersona = montoPersona
    
    #Comandos
    def establecerCantPersonas(self, cantPersonas:int):
        """Establece como cantidad de personas el numero recibido por parametro."""
        if not isinstance(cantPersonas, int):
            raise TypeError("La cantidad de personas debe ser Entero")
        if cantPersonas <= 0:
            raise ValueError("cantidad de personas debe ser positivo")
        
        self.__cantPersonas = cantPersonas
    
    def establecerMontoEquipamientos(self, montoEquipamiento:float):
        """Establece como monto por equipamiento el numero recibido por parametro."""
        if not isinstance(montoEquipamiento, (int, float)):
            raise TypeError("El monto por equipamiento debe ser un numero")
        if montoEquipamiento < 0:
            raise ValueError("El monto por equipamiento no puede ser negativo")
        
        self.__montoEquipamiento = montoEquipamiento
    
    def establecerMontoMobiliario(self, montoMobiliario:float):
        """Establece como monto por mobiliario el numero recibido por parametro."""
        if not isinstance(montoMobiliario, (int, float)):
            raise TypeError("El monto por mobiliario debe ser un numero")
        if montoMobiliario < 0:
            raise ValueError("El monto por mobiliario no puede ser negativo")
        
        self.__montoMobiliario = montoMobiliario
    
    def establecerMontoPersona(self, montoPersona:float):
        """Establece como monto por persona el numero recibido por parametro."""
        if not isinstance(montoPersona, (int, float)):
            raise TypeError("El monto por persona debe ser un numero")
        if montoPersona < 0:
            raise ValueError("El monto por persona no puede ser negativo")
        
        self.__montoPersona = montoPersona
    
    def copiarValores(self, otraPolizaEscolar:'PolizaInmuebleEscolar'):
        """Copia los valores del estado interno de 'otraPolizaEscolar' en self.(Superficial)"""
        if isinstance(otraPolizaEscolar,PolizaInmuebleEscolar):
            self._numero = otraPolizaEscolar.obtenerNumero()
            self._incendio = otraPolizaEscolar.obtenerIncendio()
            self._explosion = otraPolizaEscolar.obtenerExplosion()
            self._robo = otraPolizaEscolar.obtenerRobo()
            self.__cantPersonas = otraPolizaEscolar.obtenerCantPersonas()
            self.__montoEquipamiento = otraPolizaEscolar.obtenerMontoEquipamiento()
            self.__montoMobiliario = otraPolizaEscolar.obtenerMontoMobiliario()
            self.__montoPersona = otraPolizaEscolar.obtenerMontoPersona()
        else:
            raise TypeError("otraPolizaEscolar deb ser una instancia de PolizaInmuebleEscolar")
    
    #Consultas
    def obtenerCantPersonas(self) -> int:
        """Devuelve la cantidad de personas."""
        return self.__cantPersonas
    
    def obtenerMontoEquipamiento(self) -> int:
        """Devuelve el monto por equipamiento."""
        return self.__montoEquipamiento
    
    def obtenerMontoMobiliario(self) -> int:
        """Devuelve el monto por mobiliario."""
        return self.__montoMobiliario
    
    def obtenerMontoPersona(self) -> int:
        """Devuelve el monto por persona."""
        return self.__montoPersona
    
    def costoPoliza(self) -> int|float:
        """Devuelve la suma de los 3 valores de la poliza como total. Si hay mas de 5 personas suma un adicional"""
        total_base = self._incendio + self._explosion + self._robo
        if self.__cantPersonas > 5:
            return total_base * (1 + 0.30)
        else:
            return total_base
    
    def esIgualQue(self, otraPoliza:'PolizaInmuebleEscolar') -> bool:
        """Deveulve True si los valores del estado interno de cada objeto son equivalentes.(Superficial)"""
        if not isinstance(otraPoliza,PolizaInmuebleEscolar):
            raise TypeError("otraPoliza debe ser una instancia de PolizaInmuebleEscolar")
        
        mismoNumero = self._numero == otraPoliza.obtenerNumero()
        mismoIncendio = self._incendio == otraPoliza.obtenerIncendio()
        mismaExplosion = self._explosion == otraPoliza.obtenerExplosion()
        mismoRobo = self._robo == otraPoliza.obtenerRobo()
        mismaCantPersona = self.__cantPersonas == otraPoliza.obtenerCantPersonas()
        mismoMontoEquip = self.__montoEquipamiento == otraPoliza.obtenerMontoEquipamiento()
        mismoMontoMob = self.__montoMobiliario == otraPoliza.obtenerMontoMobiliario()
        mismoMontoPer = self.__montoPersona == otraPoliza.obtenerMontoPersona()
        
        return mismoNumero and mismoIncendio and mismaExplosion and mismoRobo and mismaCantPersona and mismoMontoEquip and mismoMontoMob and mismoMontoPer
    
    def clonar(self) -> 'PolizaInmuebleEscolar':
        """Devuelve un nuevo objeto de tipo PolizaInmuebleEscolar con el mismo estado interno que self. (Superficial)"""
        return PolizaInmuebleEscolar(self._numero, self._incendio, self._explosion, self._robo, self.__cantPersonas, self.__montoEquipamiento, self.__montoMobiliario, self.__montoPersona)
    
    def __str__(self):
        return (
            f"{super().__str__()}\n"
            f"Cant Personas: {self.__cantPersonas}\n"
            f"Monto Equipamiento: {self.__montoEquipamiento}\n"
            f"Monto Mobiliario: {self.__montoMobiliario}\n"
            f"Monto Persona: {self.__montoPersona}\n"
        )
    
    def __repr__(self):
        return f"PolizaInmuebleEscolar('{self._numero}', '{self._incendio}', '{self._explosion}', '{self._robo}', '{self.__cantPersonas}', '{self.__montoEquipamiento}', '{self.__montoMobiliario}', '{self.__cantPersonas}')"