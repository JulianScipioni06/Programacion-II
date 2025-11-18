class Participante:
    #Constructor
    def __init__(self, nombre: str, email: str,telefono: int):
        """
        Inicializa un nuevo objeto Participante.
        Parametros:
        - nombre: nombre del participante
        - email: email del participante
        - telefono: telefono del participante
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
        if not isinstance(telefono, int):
            raise TypeError("telefono debe ser de tipo int")
        if telefono <= 0:
            raise ValueError("telefono debe ser positivo")
        
        self.__nombre = nombre
        self.__email = email
        self.__telefono = telefono
    
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
    
    def establecerTelefono(self, telefono: int):
        if not isinstance(telefono, int):
            raise TypeError("telefono debe ser de tipo int")
        if telefono <= 0:
            raise ValueError("telefono debe ser positivo")
        
        self.__telefono = telefono
    
    def copiarValores(self, otroParticipante: 'Participante'):
        if not isinstance(otroParticipante, Participante):
            raise TypeError("otroParticipante debe ser una instancia de tipo Participante")
        self.__nombre = otroParticipante.obtenerNombre()
        self.__email = otroParticipante.obtenerEmail()
        self.__telefono = otroParticipante.obtenerTelefono()
    
    #Consultas
    def obtenerNombre(self) -> str:
        return self.__nombre
    
    def obtenerEmail(self) -> str:
        return self.__email
    
    def obtenerTelefono(self) -> int:
        return self.__telefono
    
    def esIgualQue(self, otroParticipante: 'Participante') -> bool:
        mismoNombre = self.__nombre == otroParticipante.obtenerNombre()
        mismoEmail = self.__email == otroParticipante.obtenerEmail()
        mismoTelefono = self.__telefono == otroParticipante.obtenerTelefono()
        
        return mismoNombre and mismoEmail and mismoTelefono
    
    def clonar(self) -> 'Participante':
        return Participante(self.__nombre, self.__email, self.__telefono)