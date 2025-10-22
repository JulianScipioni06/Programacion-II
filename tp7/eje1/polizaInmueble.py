class PolizaInmueble:
    def __init__(self, numero:int, incendio:float = 0, explosion:float = 0, robo:float = 0):
        if not isinstance(numero, int):
            raise TypeError("El numero de poliza debe ser Entero")
        if numero <= 0:
            raise ValueError("Numero de Poliza debe ser positivo")
        if not isinstance(incendio, (int, float)):
            raise TypeError("El valor por incendio debe ser un numero")
        if incendio < 0:
            raise ValueError("El valor por incendio no puede ser negativo")
        if not isinstance(explosion, (int, float)):
            raise TypeError("El valor depor explosion debe ser un numero")
        if explosion < 0:
            raise ValueError("El valor por explosion no puede ser negativo")
        if not isinstance(robo, (int, float)):
            raise TypeError("El valor por robo debe ser un numero")
        if robo < 0:
            raise ValueError("El valor por robo no puede ser negativo")
        
        self._numero = numero
        self._incendio = incendio
        self._explosion = explosion
        self._robo = robo
    
    #Comandos
    def establecerNumero(self, numero:int):
        """Establece como Numero de Poliza el numero recibido por parametro."""
        if not isinstance(numero, int):
            raise TypeError("El numero de poliza debe ser Entero")
        if numero <= 0:
            raise ValueError("Numero de Poliza debe ser positivo")
        
        self._numero = numero
    
    def establecerIncendio(self, incendio:float):
        """Establece como valor por incendio el numero recibido por parametro."""
        if not isinstance(incendio, (int, float)):
            raise TypeError("El valor por incendio debe ser un numero")
        if incendio < 0:
            raise ValueError("El valor por incendio no puede ser negativo")
        
        self._incendio = incendio
    
    def establecerExplosion(self, explosion:float):
        """Establece como valor por explosion el numero recibido por parametro."""
        if not isinstance(explosion, (int, float)):
            raise TypeError("El valor depor explosion debe ser un numero")
        if explosion < 0:
            raise ValueError("El valor por explosion no puede ser negativo")
        
        self._explosion = explosion
    
    def establecerRobo(self, robo:float):
        """Establece como valor por robo el numero recibido por parametro."""
        if not isinstance(robo, (int, float)):
            raise TypeError("El valor por robo debe ser un numero")
        if robo < 0:
            raise ValueError("El valor por robo no puede ser negativo")
        
        self._robo = robo
    
    def copiarValores(self, otraPoliza:'PolizaInmueble'):
        """Copia los valores del estado interno de 'otraPoliza' en self.(Superficial)"""
        if isinstance(otraPoliza,PolizaInmueble):
            self._numero = otraPoliza.obtenerNumero()
            self._incendio = otraPoliza.obtenerIncendio()
            self._explosion = otraPoliza.obtenerExplosion()
            self._robo = otraPoliza.obtenerRobo()
        else:
            raise TypeError("otraPoliza deb ser una instancia de PolizaInmueble")
    
    #Consultas
    def obtenerNumero(self) -> int:
        """Devuelve el numero de poliza."""
        return self._numero
    
    def obtenerIncendio(self) -> int|float:
        """Devuelve el valor por incendio de la poliza."""
        return self._incendio
    
    def obtenerExplosion(self) -> int|float:
        """Devuelve el valor por explosion de la poliza."""
        return self._explosion
    
    def obtenerRobo(self) -> int|float:
        """Devuelve el valor por robo de la poliza."""
        return self._robo
    
    def costoPoliza(self) -> int|float:
        """Devuelve la suma de los 3 valores de la poliza como total."""
        return self._incendio + self._explosion + self._robo
    
    def esIgualQue(self, otraPoliza:'PolizaInmueble') -> bool:
        """Deveulve True si los valores del estado interno de cada objeto son equivalentes.(Superficial)"""
        if not isinstance(otraPoliza,PolizaInmueble):
            raise TypeError("otraPoliza deb ser una instancia de PolizaInmueble")
        
        mismoNumero = self._numero == otraPoliza.obtenerNumero()
        mismoIncendio = self._incendio == otraPoliza.obtenerIncendio()
        mismaExplosion = self._explosion == otraPoliza.obtenerExplosion()
        mismoRobo = self._robo == otraPoliza.obtenerRobo()
        
        return mismoNumero and mismoIncendio and mismaExplosion and mismoRobo
    
    def clonar(self) -> 'PolizaInmueble':
        """Devuelve un nuevo objeto de tipo PolizaInmueble con el mismo estado interno que self. (Superficial)"""
        return PolizaInmueble(self._numero, self._incendio, self._explosion, self._robo)
    
    def __str__(self) -> str:
        return (
            f"Numero: {self._numero}\n"
            f"Incendio: {self._incendio}\n"
            f"Explosion: {self._explosion}\n"
            f"Robo: {self._robo}\n"
        )
    
    def __repr__(self):
        return f"PolizaInmueble('{self._numero}', '{self._incendio}', '{self._explosion}', '{self._robo}')"