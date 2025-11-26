from modelos.entidades.tema import Tema
import json

class RepositorioTemas:
    __RUTA_ARCHIVO = "datos/temas.json"

    def __init__(self):
        self.__temas = []
        self.__cargarDesdeArchivo()

    def __cargarDesdeArchivo(self):
        try:
            with open(self.__RUTA_ARCHIVO, 'r', encoding='utf-8') as archivo:
                datos = json.load(archivo)
                for tema_dict in datos:
                    tema = Tema.fromDiccionario(tema_dict)
                    self.__temas.append(tema)
        except Exception:
            print("No se pudo cargar el archivo de temas. Se iniciará con una lista vacía.")
    
    def __guardarEnArchivo(self):
        try:
            with open(self.__RUTA_ARCHIVO, 'w', encoding='utf-8') as archivo:
                datos = []
                for tema in self.__temas:
                    datos.append(tema.toDiccionario())
                json.dump(datos, archivo, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"No se pudo guardar el archivo de temas: {e}")

    #metodo para el GET de todos los temas
    def obtenerTodos(self):
        return self.__temas
    #metodo para el GET de un tema por id
    def obtenerPorNumero(self, numero:int):
        for tema in self.__temas:
            if tema.obtenerNumero() == numero:
                return tema
        return None
    
    #metodo para agregar un tema
    def agregar(self, tema:Tema)->bool:
        if not self.existe_tema(tema.obtenerNumero()):
            self.__temas.append(tema)
            self.__guardarEnArchivo()
            return True
        return False

    def existe_tema(self, numero:int):
        for tema in self.__temas:
            if tema.obtenerNumero() == numero:
                return True
        return False
    
    #metodo para eliminar un tema por id
    def eliminar(self, numero:int)->bool:
        for tema in self.__temas:
            if tema.obtenerNumero() == numero:
                self.__temas.remove(tema)
                self.__guardarEnArchivo()
                return True
        return False
    
    #metodo para actualizar un tema
    def actualizar(self, numero:int, dict_tema:dict)->bool:
        tema_existente = self.obtenerPorNumero(numero)
        if tema_existente:
            if "nombre" in dict_tema:
                tema_existente.establecerNombre(dict_tema["nombre"])
            if "enunciado" in dict_tema:
                tema_existente.establecerEnunciado(dict_tema["enunciado"])
            self.__guardarEnArchivo()
            return True
        return False