from modelos.entidades.alumno import Alumno
import json

class RepositorioAlumnos:
    __RUTA_ARCHIVO = "datos/alumnos.json"

    def __init__(self):
        self.__alumnos = []
        self.__cargarDesdeArchivo()

    def __cargarDesdeArchivo(self):
        try:
            with open(self.__RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
                datos_cargados = json.load(archivo)
                if "ultimo_id" in datos_cargados:
                    ultimo_id = datos_cargados["ultimo_id"]
                    Alumno.establecerUltimoID(ultimo_id)
                if "alumnos" in datos_cargados:
                    lista_alumnos = datos_cargados["alumnos"]
                    for alumno_diccionario in lista_alumnos:
                        alumno = Alumno.fromDiccionario(alumno_diccionario)
                        self.__alumnos.append(alumno)
        except Exception as e:
            print(f"Error al cargar los datos desde el archivo: {e}")

    def __guardarEnArchivo(self):
        # primero generamos la lista de diccionarios de alumnos
        lista_alumnos_diccionarios = []
        for alumno in self.__alumnos:
            lista_alumnos_diccionarios.append(alumno.toDiccionario())
        # luego obtenemos el último ID utilizado por la clase
        ultimo_id_utilizado = Alumno.obtenerUltimoID()
        # preparamos el diccionario completo para guardar
        datos_a_guardar = {"ultimo_id": ultimo_id_utilizado, "alumnos": lista_alumnos_diccionarios}
        try:            
            with open(self.__RUTA_ARCHIVO, "w", encoding="utf-8") as archivo:
                json.dump(datos_a_guardar, archivo, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Error al guardar los datos en el archivo: {e}")

    #metodo para la peticion POST
    def agregarAlumno(self, alumno:Alumno)->bool:
        if not isinstance(alumno, Alumno):
            raise ValueError("El argumento debe ser una instancia de Alumno.")
        if not self.existe_alumno(alumno.obtenerLegajo()):
            self.__alumnos.append(alumno)
            self.__guardarEnArchivo()
            return True
        return False

    def existe_alumno(self, legajo:int) -> bool:
        for alumno in self.__alumnos:
            if alumno.obtenerLegajo() == legajo:
                return True
        return False
    
    #metodo para la peticion GET de un alumno por legajo
    def obtener_alumno_por_legajo(self, legajo:int) -> Alumno|None:
        for alumno in self.__alumnos:
            if alumno.obtenerLegajo() == legajo:
                return alumno
        return None
    
    #metodo para la peticion GET de TODOS los alumnos
    def obtener_todos_los_alumnos(self) -> list[Alumno]:
        return self.__alumnos
    
    #metodo para la peticion DELETE
    def eliminar_alumno_por_legajo(self, legajo:int) -> bool:
        for alumno in self.__alumnos:
            if alumno.obtenerLegajo() == legajo:
                self.__alumnos.remove(alumno)
                self.__guardarEnArchivo()
                return True
        return False
    
    #metodo para la peticion PUT
    def actualizar_alumno(self, legajo:int, datos:dict) -> bool:
        alumno = self.obtener_alumno_por_legajo(legajo)
        if alumno is not None:
            # datos es el diccionario con los nuevos datos, que pueden ser parciales
            if "nombre" in datos:
                nuevo_nombre = datos["nombre"]
                if isinstance(nuevo_nombre, str) and nuevo_nombre.strip() != "":
                    alumno.establecerNombre(nuevo_nombre)
            if "apellido" in datos:
                nuevo_apellido = datos["apellido"]
                if isinstance(nuevo_apellido, str) and nuevo_apellido.strip() != "":
                    alumno.establecerApellido(nuevo_apellido)
            self.__guardarEnArchivo()
            return True
        return False