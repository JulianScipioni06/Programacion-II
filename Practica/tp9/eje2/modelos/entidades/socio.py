from datetime import date, datetime

class Socio:
    @classmethod
    def fromDiccionario(cls, dicc:dict):
        fecha_str = dicc["fecha_nacimiento"]
        fecha_obj = datetime.strptime(fecha_str, "%Y-%m-%d").date()
        return cls(dicc["dni"], dicc["nombre"], dicc["apellido"], dicc["mail"], fecha_obj)
    
    def __init__(self, dni:int, nombre:str, apellido:str, mail:str, fecha_nacimiento: date):
        if not isinstance(dni, int) or dni <= 0:
            raise ValueError("dni debe ser un entero > que 0")
        if not isinstance(nombre,str) or nombre.strip() == "":
            raise ValueError("nombre debe ser un string no vacio")
        if not isinstance(apellido,str) or apellido.strip() == "":
            raise ValueError("apellido debe ser un string no vacio")
        if not isinstance(mail,str) or mail.strip() == "":
            raise ValueError("mail debe ser un string no vacio")
        if not isinstance(fecha_nacimiento,date) or fecha_nacimiento > date.today():
            raise ValueError("fecha nacimiento debe ser de tipo fecha y no puede ser futura")
        
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__mail = mail
        self.__fecha_nacimiento = fecha_nacimiento
    
    def establecerDni(self, dni:int):
        if not isinstance(dni, int) or dni <= 0:
            raise ValueError("dni debe ser un entero > que 0")
        self.__dni = dni
    
    def establecerNombre(self, nombre:str):
        if not isinstance(nombre,str) or nombre.strip() == "":
            raise ValueError("nombre debe ser un string no vacio")
        self.__nombre = nombre
    
    def establecerApellido(self, apellido:str):
        if not isinstance(apellido,str) or apellido.strip() == "":
            raise ValueError("nombre debe ser un string no vacio")
        self.__apellido = apellido
    
    def establecerMail(self, mail:str):
        if not isinstance(mail,str) or mail.strip() == "":
            raise ValueError("mail debe ser un string no vacio")
        self.__mail = mail
    
    def establecerFecha(self, fecha_nacimiento:date):
        if not isinstance(fecha_nacimiento,date) or fecha_nacimiento > date.today():
            raise ValueError("fecha nacimiento debe ser de tipo fecha y no puede ser futura")
        self.__fecha_nacimiento = fecha_nacimiento
    
    def obtenerDni(self):
        return self.__dni
    
    def obtenerNombre(self):
        return self.__nombre
    
    def obtenerApellido(self):
        return self.__apellido
    
    def obtenerMail(self):
        return self.__mail
    
    def obtenerFecha(self):
        return self.__fecha_nacimiento
    
    def esIgual(self, otroSocio:'Socio'):
        if not isinstance(otroSocio, Socio):
            raise ValueError("otroSocio debe ser una instancia de Socio")
        mismoDni = self.__dni == otroSocio.obtenerDni()
        mismoNombre = self.__nombre == otroSocio.obtenerNombre()
        mismoApellido = self.__apellido == otroSocio.obtenerApellido()
        mismoMail = self.__mail == otroSocio.obtenerMail()
        mismaFecha = self.__fecha_nacimiento == otroSocio.obtenerFecha()
        
        return mismoDni and mismoNombre and mismoApellido and mismoMail and mismaFecha
    
    def toDiccionario(self):
        return {
            "dni": self.__dni,
            "nombre": self.__nombre,
            "apellido": self.__apellido,
            "mail": self.__mail,
            "fecha_nacimiento": self.__fecha_nacimiento.strftime("%Y-%m-%d")
        }
    
    def __str__(self):
        return(
            f"DNI: {self.__dni}\n"
            f"Nombre: {self.__nombre}\n"
            f"Apellido: {self.__apellido}\n"
            f"Mail: {self.__mail}\n"
            f"Fecha Nacimiento: {self.__fecha_nacimiento}\n"
        )