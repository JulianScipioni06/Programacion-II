from participante import Participante
from organizador import Organizador

class Evento: 
    #Constructor
    def __init__(self, nombre: str = "-", fecha: str = "-", descripcion: str = "-", organizador: Organizador = None, participantes: list[Participante] = None):
        """
        Inicializa un nuevo objeto Evento.
        Parametros:
        - nombre: nombre del evento
        - fecha: fecha del evento
        - descripcion: descripcion del evento
        - organizador: organizador del evento
        - participantes: participantes del evento
        """
        
        if not isinstance(nombre,str):
            raise TypeError("nombre debe ser de tipo string")
        if nombre == "" or nombre.isspace():
            raise ValueError("nombre no debe estar vacio")
        if not isinstance(fecha,str):
            raise TypeError("fecha debe ser de tipo string")
        if fecha == "" or fecha.isspace():
            raise ValueError("fecha no debe estar vacio")
        if not isinstance(descripcion,str):
            raise TypeError("descripcion debe ser de tipo string")
        if descripcion == "" or descripcion.isspace():
            raise ValueError("descripcion no debe estar vacio")
        if not isinstance(organizador,Organizador) and organizador is not None:
            raise TypeError("organizador debe ser una instancia de tipo Organizador")
        
        self.__nombre = nombre
        self.__fecha = fecha
        self.__descripcion = descripcion
        self.__organizador = organizador
        self.__participantes = []
        
        if participantes != None:
            if isinstance(participantes,Participante):
                self.__participantes.append(participantes)
            elif isinstance(participantes, list):
                for participante in participantes:
                    if isinstance(participante, Participante):
                        self.__participantes.append(participante)
    
    #Comandos
    def establecerNombre(self, nombre: str):
        if not isinstance(nombre,str):
            raise TypeError("nombre debe ser de tipo string")
        if nombre == "" or nombre.isspace():
            raise ValueError("nombre no debe estar vacio")
        
        self.__nombre = nombre
    
    def establecerFecha(self, fecha: str):
        if not isinstance(fecha,str):
            raise TypeError("fecha debe ser de tipo string")
        if fecha == "" or fecha.isspace():
            raise ValueError("fecha no debe estar vacio")
        
        self.__fecha = fecha
    
    def establecerDescripcion(self, descripcion: str):
        if not isinstance(descripcion,str):
            raise TypeError("descripcion debe ser de tipo string")
        if descripcion == "" or descripcion.isspace():
            raise ValueError("descripcion no debe estar vacio")
        
        self.__descripcion = descripcion
    
    def asignarOrganizador(self, organizador: Organizador):
        if not isinstance(organizador,Organizador):
            raise TypeError("organizador debe ser una instancia de tipo Organizador")
        
        self.__organizador = organizador
    
    def registrarParticipantes(self, participante: Participante):
        if not isinstance(participante,Participante):
            raise TypeError("participante debe ser una instancia de tipo Participante")
        
        self.__participantes.append(participante)
    
    def copiarValores(self, otroEvento:'Evento'):
        if isinstance(otroEvento, Evento):
            self.__nombre = otroEvento.obtenerNombre()
            self.__fecha = otroEvento.obtenerFecha()
            self.__descripcion = otroEvento.obtenerDescripcion()
            if otroEvento.obtenerOrganizador() != None:
                if self.__organizador != None:
                    self.__organizador.copiarValores(otroEvento.obtenerOrganizador())
                else:
                    self.__organizador = otroEvento.obtenerOrganizador().clonar()
            else:
                self.__organizador = None
            
            self.__participantes = []
            for participante in otroEvento.obtenerParticipantes():
                copiaParticipante = participante.clonar()
                self.__participantes.append(copiaParticipante)
        else:
            raise ValueError("El organizador a copiar debe ser un objeto de la clase Organizador.")
    
    #Consultas
    def obtenerNombre(self) -> str:
        return self.__nombre
    
    def obtenerFecha(self) -> str:
        return self.__fecha
    
    def obtenerDescripcion(self) -> str:
        return self.__descripcion
    
    def obtenerOrganizador(self) -> Organizador:
        return self.__organizador
    
    def obtenerParticipantes(self) -> list[Participante]:
        return self.__participantes
    
    def tieneParticipante(self, participante: Participante) -> bool:
        if not isinstance(participante,Participante):
            raise TypeError("participante debe ser una instancia de tipo Participante")
        return participante in self.__participantes
    
    def esIgualQue(self, otroEvento: 'Evento') -> bool:
        mismoNombre = self.__nombre == otroEvento.obtenerNombre()
        mismaFecha = self.__fecha == otroEvento.obtenerFecha()
        mismaDescripcion = self.__descripcion == otroEvento.obtenerDescripcion()
        mismoOrganizador = self.__organizador.esIgualQue(otroEvento.obtenerOrganizador())
        
        if self.__participantes is None and otroEvento.obtenerParticipantes() is None:
            mismosParticipantes = True
        elif (self.__participantes is None) != (otroEvento.obtenerParticipantes() is None):
            mismosParticipantes = False
        elif len(self.__participantes) != len(otroEvento.obtenerParticipantes()):
            mismosParticipantes = False
        else:
            mismosParticipantes = True
            for i in range(len(self.__participantes)):
                m1 = self.__participantes[i]
                m2 = otroEvento.obtenerParticipantes()[i]
                if not m1.esIgualQue(m2):
                    mismosParticipantes = False
        
        return mismoNombre and mismaFecha and mismaDescripcion and mismoOrganizador and mismosParticipantes
    
    def clonar(self) -> 'Evento':
        clon = Evento(self.__nombre, self.__fecha, self.__descripcion)
        clon.asignarOrganizador(self.__organizador)
        
        if self.__participantes != None:
            clon.__participantes = []
            for participante in self.__participantes:
                clon.__participantes.append(participante.clonar()) 
        else:
            clon.__participantes = None
        
        return clon