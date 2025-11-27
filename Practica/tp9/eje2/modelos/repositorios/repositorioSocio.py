from modelos.entidades.socio import Socio
from datetime import date
import json

class RepositorioSocio:
    FILE_PATH = r"C:\Users\July\Documents\Universidad\Segundo Cuatrimestre\Programacion-II\Practica\tp9\eje2\datos\socios.json"
    
    def __init__(self):
        self.__socios = self.__cargarTodos()
    
    def __cargarTodos(self):
        lista_socios = []
        
        try:
            with open(RepositorioSocio.FILE_PATH, "r") as file:
                datos = json.load(file)
                for l in datos:
                    lista_socios.append(Socio.fromDiccionario(l))
        except FileNotFoundError:
            print("No se encontro el archivo")
            
        return lista_socios
    
    def __guardarTodos(self):
        try:
            lista = []
            
            for socio in self.__socios:
                if isinstance(socio, Socio):
                    lista.append(socio.toDiccionario())
            
            with open(RepositorioSocio.FILE_PATH, "w")as file:
                json.dump(lista, file, indent=4)
            
        except FileNotFoundError:
            print("No se encontro el archivo")
    
    def obtenerTodos(self) -> list:
        return self.__socios
    
    def obtenerPorDNI(self, dni:int):
        for s in self.__socios:
            if isinstance(s, Socio):
                if s.obtenerDni() == dni:
                    return s
        return None
    
    def existe(self, socio: Socio) -> bool:
        return socio in self.__socios
    
    def existeDNI(self, dni:int) -> bool:
        for s in self.__socios:
            if isinstance(s, Socio):
                if s.obtenerDni() == dni:
                    return True
        return False
    
    def agregar(self, nuevoSocio:Socio):
        if not isinstance(nuevoSocio, Socio):
            raise TypeError("Se esperaba una instancia de Socio")
        
        if not self.existe(nuevoSocio):
            self.__socios.append(nuevoSocio)
            self.__guardarTodos()
    
    def modificarPorDNI(self, dni:int, nombre:str, apellido:str, mail:str, fecha_nacimiento: date) -> bool:
        if self.existeDNI(dni):
            socio = self.obtenerPorDNI(dni)
            socio.establecerNombre(nombre)
            socio.establecerApellido(apellido)
            socio.establecerMail(mail)
            socio.establecerFecha(fecha_nacimiento)
            
            self.__guardarTodos()
            return True
        return False
    
    def eliminarPorDNI(self, dni:int):
        if self.existeDNI(dni):
            socio = self.obtenerPorDNI(dni)
            
            self.__socios.remove(socio)
            self.__guardarTodos()
            return True
        return False