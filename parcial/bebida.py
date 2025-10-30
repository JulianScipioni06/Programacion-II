class Bebida:
    def __init__(self, nombre:str, precio: float, tipo: str, stock: int):
        """
        Inicializa un nuevo objeto Bebida.
        Parametros:
        - nombre: Nombre de la bebida
        - precio: Precio de la bebida
        - tipo: Tipo de la bebida
        - stock: Stock disponible de la bebida
        """
        if not isinstance(nombre, str):
            raise TypeError("nombre debe ser de tipo string")
        if nombre.strip() == "":
            raise ValueError("nombre no puede estar vacio")
        if not isinstance(precio,(int,float)):
            raise TypeError("precio debe ser un numero")
        if precio < 0:
            raise ValueError("precio no puede ser negativo")
        if not isinstance(tipo, str):
            raise TypeError("tipo debe ser de tipo string")
        if tipo.strip() == "":
            raise ValueError("tipo no puede estar vacio")
        if not isinstance(stock, int):
            raise TypeError("stock debe ser un numero entero")
        if stock < 0:
            raise ValueError("stock debe ser positivo")
        
        self.__nombre = nombre
        self.__precio = precio
        self.__tipo = tipo
        self.__stock = stock
    
    #Comandos Triviales
    def establecerNombre(self, nombre:str):
        """Establece el nombre de la bebida con lo recibido por parametro"""
        if not isinstance(nombre, str):
            raise TypeError("nombre debe ser de tipo string")
        if nombre.strip() == "":
            raise ValueError("nombre no puede estar vacio")
        
        self.__nombre = nombre
    
    def establecerPrecio(self, precio:float):
        """Establece el precio de la bebida con lo recibido por parametro"""
        if not isinstance(precio,(int,float)):
            raise TypeError("precio debe ser un numero")
        if precio < 0:
            raise ValueError("precio no puede ser negativo")
        
        self.__precio = precio
    
    def establecerTipo(self, tipo:str):
        """Establece el tipo de la bebida con lo recibido por parametro"""
        if not isinstance(tipo, str):
            raise TypeError("tipo debe ser de tipo string")
        if tipo.strip() == "":
            raise ValueError("tipo no puede estar vacio")
        
        self.__tipo = tipo
    
    def establecerStock(self, stock:int):
        """Establece el stock de la bebida con lo recibido por parametro"""
        if not isinstance(stock, int):
            raise TypeError("stock debe ser un numero entero")
        if stock < 0:
            raise ValueError("stock debe ser positivo")
        
        self.__stock = stock
    
    #Comandos
    def reducirStock(self, cantidad:int):
        """Reduce el stock de la bebida con la cantidad recibida por parametro"""
        if not isinstance(cantidad, int):
            raise TypeError("cantidad debe ser un numero entero")
        if cantidad < 0:
            raise ValueError("cantidad debe ser positivo")
        
        if self.__stock - cantidad < 0:
            self.__stock = 0
        else:
            self.__stock -= cantidad
    
    def aumentarStock(self, cantidad:int):
        """Aumenta el stock de la bebida con la cantidad recibida por parametro"""
        if not isinstance(cantidad, int):
            raise TypeError("cantidad debe ser un numero entero")
        if cantidad < 0:
            raise ValueError("cantidad debe ser positivo")
        
        self.__stock += cantidad
    
    #Consultas Triviales
    def obtenerNombre(self) -> str:
        """Devuelve el nombre de la bebida"""
        return self.__nombre
    
    def obtenerPrecio(self) -> float:
        """Devuelve el precio de la bebida"""
        return self.__precio
    
    def obtenerTipo(self) -> str:
        """Devuelve el tipo de la bebida"""
        return self.__tipo
    
    def consultarStock(self) -> int:
        """Devuelve el stock actual de la bebida"""
        return self.__stock
    
    def clonar(self):
        """Devuelve un nuevo objeto bebida con el mismo estado interno que self"""
        return Bebida(self.__nombre, self.__precio, self.__tipo, self.__stock)
    
    def __str__(self):
        return f"DATOS DE BEBIDA:\n - Nombre: {self.__nombre}\n - Precio: ${self.__precio}\n - tipo: {self.__tipo}\n - stock: {self.__stock}"