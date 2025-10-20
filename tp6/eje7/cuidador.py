from mascota import Mascota

class Cuidador:
    def __init__(self, nombre: str = "-", direccion: str = "-", telefono: int = 0, mascotas: list[Mascota] = None):
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
        if not isinstance(direccion, str) or direccion.strip() == "":
            raise ValueError("La direccionj debe ser un texto y no puede quedar vacio!")
        if not isinstance(telefono, int) or telefono < 0:
            raise ValueError("El telefono debe ser un entero positivo")
        
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__mascotas = []
        
        if mascotas != None:
            if isinstance(mascotas,Mascota):
                self.__mascotas.append(mascotas)
            elif isinstance(mascotas, list):
                for mascota in mascotas:
                    if isinstance(mascota, Mascota):
                        self.__mascotas.append(mascota)
    
    #Comandos
    def establecerNombre(self, nombre:str):
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre debe ser un texto y no puede quedar vacio!")
        
        self.__nombre = nombre
    
    def establecerDireccion(self, direccion:str):
        if not isinstance(direccion, str) or direccion.strip() == "":
            raise ValueError("La direccion debe ser un texto y no puede quedar vacio!")
        
        self.__direccion = direccion
    
    def establecerTelefono(self, telefono:int):
        if not isinstance(telefono, int) or telefono < 0:
            raise ValueError("El telefono debe ser un entero positivo")
        
        self.__telefono = telefono
    
    def asignarMascota(self, mascota:Mascota):
        if not isinstance(mascota, Mascota):
            raise ValueError("mascota de ber de tipo Mascota")
        
        self.__mascotas.append(mascota)
    
    def copiarValores(self, otroCuidador: 'Cuidador'):
        if not isinstance(otroCuidador, Cuidador):
            raise ValueError("Debe recibir un objeto de tipo Cuidador")
        
        self.__nombre = otroCuidador.obtenerNombre()
        self.__direccion = otroCuidador.obtenerDireccion()
        self.__telefono = otroCuidador.obtenerTelefono()
        
        self.__mascotas = []
        for mascota in otroCuidador.obtenerMascotas():
            copiaMascota = mascota.clonar()
            self.__mascotas.append(copiaMascota)
    
    #Consultas
    def obtenerNombre(self) -> str:
        return self.__nombre
    
    def obtenerDireccion(self) -> str:
        return self.__direccion
    
    def obtenerTelefono(self) -> int:
        return self.__telefono
    
    def obtenerMascotas(self) -> list[Mascota]:
        return self.__mascotas
    
    def tieneMascota(self, mascota: Mascota):
        if not isinstance(mascota, Mascota):
            raise TypeError("mascota debe ser una instancia de tipo MASCOTA")
        
        return mascota in self.__mascotas
    
    def esIgualQue(self, otroCuidador):
        if not isinstance(otroCuidador, Cuidador):
            raise ValueError("Debe recibir un objeto de tipo Cuidador")
        
        mismoNombre = self.__nombre == otroCuidador.obtenerNombre()
        mismaDireccion = self.__direccion == otroCuidador.obtenerDireccion()
        mismoTelefono = self.__telefono == otroCuidador.obtenerTelefono()
        
        if self.__mascotas is None and otroCuidador.obtenerMascotas() is None:
            mismasMascotas = True
        elif (self.__mascotas is None) != (otroCuidador.obtenerMascotas() is None):
            mismasMascotas = False
        elif len(self.__mascotas) != len(otroCuidador.obtenerMascotas()):
            mismasMascotas = False
        else:
            mismasMascotas = True
            for i in range(len(self.__mascotas)):
                m1 = self.__mascotas[i]
                m2 = otroCuidador.obtenerMascotas()[i]
                if not m1.esIgualQue(m2):
                    mismasMascotas = False
        
        return mismoNombre and mismaDireccion and mismoTelefono and mismasMascotas
    
    def clonar(self) -> 'Cuidador':
        copia = Cuidador(self.__nombre, self.__direccion, self.__telefono)
        
        if self.__mascotas is not None:
            copia.__mascotas = []
            for mascota in self.__mascotas:
                copia.__mascotas.append(mascota.clonar()) 
        else:
            copia.__mascotas = None
    
    def __str__(self):
        return f"Nombre: {self.__nombre}\n Direccion: {self.__direccion}\n Telefono: {self.__telefono}\n MASCOTAS: {self.__mascotas}\n"