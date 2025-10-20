class Mascota:
    #Constructor
    def __init__(self, nombre: str = "-", especie: str = "-", edad: int = 0, descripcion: str = "-"):
        """
        Inicializa un nuevo objeto Mascota.
        Parametros:
        - nombre: nombre de la mascota
        - especie: especie de la mascota
        - edad: edad de la mascota
        - descripcion: descripcion de la mascota
        """
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre debe ser un texto y no puede quedar vacio!")
        if not isinstance(especie, str) or especie.strip() == "":
            raise ValueError("La especie debe ser un texto y no puede quedar vacio!")
        if not isinstance(edad, int) or edad < 0:
            raise ValueError("La edad debe ser un entero positivo")
        if not isinstance(descripcion, str) or descripcion.strip() == "":
            raise ValueError("La descripción debe ser un texto y no puede quedar vacía!")
        
        self.__nombre = nombre
        self.__especie = especie
        self.__edad = edad
        self.__descripcion = descripcion
    
    #Comandos
    def establecerNombre(self, nombre: str):
        """Establece el nombre recibido por parametro"""
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre debe ser un texto y no puede quedar vacio!")
        
        self.__nombre = nombre
    
    def establecerEspecie(self, especie: str):
        """Establece la especie recibida por parametro"""
        if not isinstance(especie, str) or especie.strip() == "":
            raise ValueError("La especie debe ser un texto y no puede quedar vacio!")
        
        self.__especie = especie
    
    def establecerEdad(self, edad: int):
        """Establece la edad recibida por parametro"""
        if not isinstance(edad, int) or edad < 0:
            raise ValueError("La edad debe ser un entero positivo")
        
        self.__edad = edad
    
    def establecerDescripcion(self, descripcion: str):
        """Establece la descripcion recibida por parametro"""
        if not isinstance(descripcion, str) or descripcion.strip() == "":
            raise ValueError("La descripción debe ser un texto y no puede quedar vacía!")
        
        self.__descripcion = descripcion
    
    def copiarValores(self, otraMascota: 'Mascota'):
        """copia los valores del estado interna de otraMascota a self."""
        self.__nombre = otraMascota.obtenerNombre()
        self.__especie = otraMascota.obtenerEspecie()
        self.__edad = otraMascota.obtenerEdad()
        self.__descripcion = otraMascota.obtenerDescripcion()
    
    #Consultas
    def obtenerNombre(self) -> str:
        """Devuelve el nombre de la mascota"""
        return self.__nombre
    
    def obtenerEspecie(self) -> str:
        """Devuelve la especie de la mascota"""
        return self.__especie
    
    def obtenerEdad(self) -> int:
        """Devuelve la edad de la mascota"""
        return self.__edad
    
    def obtenerDescripcion(self) -> str:
        """Devuelve la descripcion de la mascota"""
        return self.__descripcion
    
    def esIgualQue(self, otraMascota: 'Mascota') -> bool:
        """Retorna True si el estado interno de self y otraMascota son iguales."""
        mismoNombre = self.__nombre == otraMascota.obtenerNombre()
        mismaEspecie = self.__especie == otraMascota.obtenerEspecie()
        mismaEdad = self.__edad == otraMascota.obtenerEdad()
        mismaDescripcion = self.__descripcion == otraMascota.obtenerDescripcion()
        return mismoNombre and mismaEspecie and mismaEdad and mismaDescripcion
    
    def clonar(self) -> 'Mascota':
        """Devuelve un clon de la Mascota"""
        return Mascota(self.__nombre, self.__especie, self.__edad, self.__descripcion)
    
    def __str__(self) -> str:
        return f"- Nombre: {self.__nombre}\n - Especie: {self.__especie}\n - Edad: {self.__edad}\n - Descripcion: {self.__descripcion}"
    
    def __repr__(self) -> str:
        return f"Mascota('{self.__nombre}', '{self.__especie}', '{self.__edad}', '{self.__descripcion}')"
