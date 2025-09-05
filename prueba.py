class Repartidor:
    valorKm = 500
    valorKmExtra = 100
    
    def __init__(self, nombre:str, edad:int, cobros:list, pedidosEmpleados:int):
        self.__nombre = nombre
        self.__edad = edad
        self.__cobros = cobros
        self.__pedidosEmpleados = pedidosEmpleados
    
    def CalcularViaje(self, km:float, propina:float = 0):
        valorViaje = km * Repartidor.__valorKm
