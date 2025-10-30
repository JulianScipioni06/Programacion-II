from persona import Persona
from bebida import Bebida

class Cliente(Persona):
    def __init__(self, nombre: str, edad: int, dinero: float, bebidaFavorita:Bebida = None):
        super().__init__(nombre, edad)
        """
        Inicializa un nuevo objeto Cliente.
        Parametros:
        - nombre: Nombre del cliente
        - edad: Edad del cliente
        - dinero: Dinero disponible del cliente
        - bebidaFavorita: Bebida favorita del cliente
        """
        if not isinstance(dinero,(int,float)):
            raise TypeError("dinero debe ser un numero")
        if dinero < 0:
            raise ValueError("dinero no puede ser negativo")
        if not isinstance(bebidaFavorita,Bebida) and bebidaFavorita is not None:
            raise TypeError("bebidaFavorita debe ser una instancia de tiopo bebida")
        
        self.__dinero = dinero
        self.__bebidaFavorita = bebidaFavorita
    
    #Comandos Triviales
    def establecerNombre(self, nombre:str):
        """Establece el nombre del cliente con lo recibido por parametro"""
        if not isinstance(nombre, str):
            raise TypeError("nombre debe ser de tipo string")
        if nombre.strip() == "":
            raise ValueError("nombre no puede estar vacio")
        
        self._nombre = nombre
    
    def establecerEdad(self, edad:int):
        """Establece la edad del cliente con lo recibido por parametro"""
        if not isinstance(edad, int):
            raise TypeError("edad debe ser un numero entero")
        if edad < 0:
            raise ValueError("edad debe ser positivo")
        
        self._edad = edad
    
    def establecerDinero(self, cantDinero:float):
        """Establece el dinero del cliente con lo recibido por parametro"""
        if not isinstance(cantDinero,(int,float)):
            raise TypeError("cantDinero debe ser un numero")
        if cantDinero < 0:
            raise ValueError("cantDinero no puede ser negativo")
        
        self.__dinero = cantDinero
    
    def establecerBebidaFavorita(self, bebida:Bebida):
        """Establece la bebida favorita del cliente con lo recibido por parametro"""
        if not isinstance(bebida,Bebida):
            raise TypeError("bebida debe ser una instancia de tipo bebida")
        
        self.__bebidaFavorita = bebida
    
    #Comandos
    def beber(self):
        """imprime por pantalla (print) el texto "Que rica mi <<nombre de la bebida favorita>>"""
        print(f"Que rica mi {self.__bebidaFavorita.obtenerNombre()}")
    
    def hablar(self):
        """imprime por pantalla (print) el texto "Cantinero, deme otra <<nombre de la bebida favorita>>"""
        print(f"Cantinero, deme otra {self.__bebidaFavorita.obtenerNombre()}")
    
    def saludar(self):
        """imprime por pantalla (print) el texto "Buenas tardes Moe!"""
        print("Buenas tardes Moe!")
    
    #Consultas Triviales
    def obtenerNombre(self) -> str:
        """Devuelve el nombre del cliente"""
        return self._nombre
    
    def obtenerEdad(self) -> int:
        """Devuelve la edad del cliente"""
        return self._edad
    
    def obtenerDinero(self) -> float:
        """Devuelve el dinero del cliente"""
        return self.__dinero
    
    def obtenerBebidaFavorita(self) -> Bebida:
        """Devuelve la bebida favorita del cliente"""
        return self.__bebidaFavorita
    
    def clonacionProfunda(self) -> 'Cliente':
        """Retorna un objeto Cliente clonado en profundida"""
        clon = Cliente(self._nombre, self._edad, self.__dinero)
        
        if self.__bebidaFavorita != None:
            clon.establecerBebidaFavorita(self.__bebidaFavorita.clonar())
        
        return clon
    
    def __str__(self):
        return (
            f"{super().__str__()}"
            f"Dinero: {self.__dinero}\n"
            f"Bebida Favorita: {self.__bebidaFavorita.obtenerNombre()}"
        )