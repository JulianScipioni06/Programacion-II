from persona import Persona

class Empleado(Persona):
    def __init__(self, nombre: str, edad: int, fechaIngreso: str):
        super().__init__(nombre, edad)
        """
        Inicializa un nuevo objeto Empleado.
        Parametros:
        - nombre: Nombre del empleado
        - edad: Edad del empleado
        - fechaIngreso: Fecha de ingreso del empleado
        """
        if not isinstance(fechaIngreso, str):
            raise TypeError("fechaIngreso debe ser un string")
        if fechaIngreso.strip() == "":
            raise ValueError("fechaIngreso no puede ser nulo")
        
        self.__fechaIngreso = fechaIngreso
    
    #Comandos Triviales
    def establecerNombre(self, nombre:str):
        """Establece el nombre del empleado con lo recibido por parametro"""
        if not isinstance(nombre, str):
            raise TypeError("nombre debe ser de tipo string")
        if nombre.strip() == "":
            raise ValueError("nombre no puede estar vacio")
        
        self._nombre = nombre
    
    def establecerEdad(self, edad:int):
        """Establece la edad del empleado con lo recibido por parametro"""
        if not isinstance(edad, int):
            raise TypeError("edad debe ser un numero entero")
        if edad < 0:
            raise ValueError("edad debe ser positivo")
        
        self._edad = edad
    
    def establecerFechaIngreso(self, fechaIngreso:str):
        """Establece la fecha de Ingreso del empleado con lo recibido por parametro"""
        if not isinstance(fechaIngreso, str):
            raise TypeError("fechaIngreso debe ser un string")
        if fechaIngreso.strip() == "":
            raise ValueError("fechaIngreso no puede ser nulo")
        
        self.__fechaIngreso = fechaIngreso
    
    #Comandos
    def beber(self):
        """imprime por pantalla 'Tomando agua en horario de trabajo...'"""
        print(f"Tomando agua en horario de trabajo...")
    
    def hablar(self):
        """imprime por pantalla '¿Qué le puedo ofrecer para tomar?'"""
        print(f"¿Qué le puedo ofrecer para tomar?")
    
    def saludar(self):
        """imprime por pantalla 'Bienvenido a la taberna de Moe!'"""
        print("Bienvenido a la taberna de Moe!")
    
    #Consultas Triviales
    def obtenerNombre(self) -> str:
        """Devuelve el nombre del cliente"""
        return self._nombre
    
    def obtenerEdad(self) -> int:
        """Devuelve la edad del cliente"""
        return self._edad
    
    def obtenerFechaIngreso(self) -> str:
        """Devuelve la Fecha de Ingreso del cliente"""
        return self.__fechaIngreso
    
    def __str__(self):
        return (
            f"{super().__str__()}"
            f"Fecha Ingreso: {self.__fechaIngreso}\n"
        )