from modelos.entidades.pizza import Pizza
import json

class RepositorioPizza:
    FILE_PATH = r"C:\Users\July\Documents\Universidad\Segundo Cuatrimestre\Programacion-II\Practica\practica-13-11\datos\pizzas.json"
    
    def __init__(self):
        self.__pizzas = self.__cargarTodas()
    
    def __cargarTodas(self):
        lista_pizzas = []
        try:
            with open(RepositorioPizza.FILE_PATH, "r") as file:
                datos = json.load(file)

                for p in datos:
                    lista_pizzas.append(Pizza.fromDiccionario(p))
        except FileNotFoundError:
            print("No se encontro el archivo")
            
        return lista_pizzas
    
    def __guardarTodas(self):
        try:
            lista = []
            
            for pizza in self.__pizzas:
                if isinstance(pizza, Pizza):
                    lista.append(pizza.toDiccionario())
            
            with open(RepositorioPizza.FILE_PATH, "w")as file:
                json.dump(lista, file, indent=4)
        except FileNotFoundError:
            print("No se encontro el archivo")
    
    def obtenerTodas(self):
        return self.__pizzas
    
    def obtenerPorId(self, id:int) -> 'Pizza' | None:
        for p in self.__pizzas:
            if isinstance(p,Pizza):
                if p.obtenerId() == id:
                    return p
        return None
    
    def agregarPizza(self, pizza:Pizza):
        if not isinstance(pizza,Pizza):
            raise ValueError("Se esperaba un dato de tipo Pizza")
        
        if not self.existe(pizza):
            self.__pizzas.append(pizza)
            self.__guardarTodas()
    
    def existe(self, pizza:Pizza):
        return pizza in self.__pizzas
    
    def existeId(self, id:int) -> bool:
        for p in self.__pizzas:
            if isinstance(p,Pizza):
                if p.obtenerId() == id:
                    return True
        return False
    
    def modificarPorId(self, id:int, nombre:str, precio:float, puntuacion:int, horneada:bool) -> bool:
        if self.existeId(id):
            p = self.obtenerPorId(id)
            p.establecerNombre(nombre)
            p.establecerPrecio(precio)
            p.establecerPuntuacion(puntuacion)
            p.establecerHorneada(horneada)
            
            self.__guardarTodas
            return True
        
        return False
    
    def eliminarPorId(self, id:int) ->bool:
        if self.existeId(id):
            p = self.obtenerPorId(id)
            self.__pizzas.remove(p)
            self.__guardarTodas()
            return True
        return False
    
    #SEGUIR EN MIN 49 DE CLASE