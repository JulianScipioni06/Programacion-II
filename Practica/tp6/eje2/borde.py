from color import Color

class Borde:
    def __init__(self, grosor:int, color:'Color'):
        if not isinstance(grosor,int):
            raise TypeError("Grosor debe ser un entero")
        if grosor <= 0:
            raise ValueError("Grosor no puede ser negativo o 0")
        if not isinstance(color,Color):
            raise TypeError("Color debe ser una instancia de Color")
        
        self.__grosor = grosor
        self.__color = color
    
    #Comandos
    def establecerBorde(self, grosor:int):
        if not isinstance(grosor,int):
            raise TypeError("Grosor debe ser un entero")
        if grosor <= 0:
            raise ValueError("Grosor no puede ser negativo o 0")
        
        self.__grosor = grosor
    
    def establecerColor(self, color:'Color'):
        if not isinstance(color,Color):
            raise TypeError("Color debe ser una instancia de Color")
        
        self.__color = color
    
    def copiarValores(self, otroBorde:'Borde'):
        self.__grosor = otroBorde.obtenerGrosor()
        self.__color = otroBorde.obtenerColor()
    
    #consultas
    def obtenerGrosor(self) -> int:
        return self.__grosor
    
    def obtenerColor(self) -> Color:
        return self.__color
    
    def clonarSup(self) -> 'Borde':
        return Borde(self.__grosor, self.__color)
    
    def clonarProf(self) -> 'Borde':
        clon_borde = Borde(self.__grosor)
        clon_borde.establecerColor(self.__color.obtenerRojo(), self.__color.obtenerVerde(),self.__color.obtenerAzul())
        
        return clon_borde
    
    def esIgualQueSup(self, otroBorde:'Borde') -> bool:
        mismoGrosor = self.__grosor == otroBorde.obtenerGrosor()
        mismoColor = self.__color == otroBorde.obtenerColor()
        
        return mismoGrosor and mismoColor
    
    def esIgualQueProf(self, otroBorde:'Borde') -> bool:
        mismoGrosor = self.__grosor == otroBorde.obtenerGrosor()
        mismoColor = self.__color.esIgualQue(otroBorde.obtenerColor())
        
        return mismoGrosor and mismoColor