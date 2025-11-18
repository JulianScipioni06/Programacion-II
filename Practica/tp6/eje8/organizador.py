class Organizador:
    #Constructor
    def __init__(self, nombre: str, email: str, especialidad: str):
        """
        Inicializa un nuevo objeto Organizador.
        Parametros:
        - nombre: nombre del organizador
        - email: email del organizador
        - especialidad: especialidad del organizador
        """
        
        if not isinstance(nombre,str):
            raise TypeError("nombre debe ser de tipo string")
        if nombre == "" or nombre.isspace():
            raise ValueError("nombre no debe estar vacio")
        if not isinstance(email,str):
            raise TypeError("email debe ser de tipo string")
        if email == "" or email.isspace():
            raise ValueError("email no debe estar vacio")
        if not "@" in email:
            raise ValueError("email no valido")
        if not isinstance(especialidad,str):
            raise TypeError("especialidad debe ser de tipo string")
        if especialidad == "" or especialidad.isspace():
            raise ValueError("especialidad no debe estar vacio")
        
        self.__nombre = nombre
        self.__email = email
        self.__especialidad = especialidad
    
    #Comandos
    def establecerNombre(self, nombre: str):
        if not isinstance(nombre,str):
            raise TypeError("nombre debe ser de tipo string")
        if nombre == "" or nombre.isspace():
            raise ValueError("nombre no debe estar vacio")
        
        self.__nombre = nombre
    
    def establecerEmail(self, email: str):
        if not isinstance(email,str):
            raise TypeError("email debe ser de tipo string")
        if email == "" or email.isspace():
            raise ValueError("email no debe estar vacio")
        if not "@" in email:
            raise ValueError("email no valido")
        
        self.__email = email
    
    def establecerEspecialidad(self, especialidad: str):
        if not isinstance(especialidad,str):
            raise TypeError("especialidad debe ser de tipo string")
        if especialidad == "" or especialidad.isspace():
            raise ValueError("especialidad no debe estar vacio")
        
        self.__especialidad = especialidad
    
    def copiarValores(self, otroOrganizador: 'Organizador'):
        if not isinstance(otroOrganizador, Organizador):
            raise TypeError("otroParticipante debe ser una instancia de tipo Participante")
        self.__nombre = otroOrganizador.obtenerNombre()
        self.__email = otroOrganizador.obtenerEmail()
        self.__especialidad = otroOrganizador.obtenerEspecialidad()
    
    #Consultas
    def obtenerNombre(self) -> str:
        return self.__nombre
    
    def obtenerEmail(self) -> str:
        return self.__email
    
    def obtenerEspecialidad(self) -> str:
        return self.__especialidad
    
    def esIgualQue(self, otroOrganizador: 'Organizador') -> bool:
        mismoNombre = self.__nombre == otroOrganizador.obtenerNombre()
        mismoEmail = self.__email == otroOrganizador.obtenerEmail()
        mismaEspecialidad = self.__especialidad == otroOrganizador.obtenerEspecialidad()
        
        return mismoNombre and mismoEmail and mismaEspecialidad
    
    def clonar(self) -> 'Organizador':
        return Organizador(self.__nombre, self.__email, self.__especialidad)