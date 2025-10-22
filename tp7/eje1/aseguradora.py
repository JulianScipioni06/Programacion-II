from polizaInmueble import PolizaInmueble

class Aseguradora:
    def __init__(self, seguros: list[PolizaInmueble] = None):
        self.__seguros = []
        
        if seguros != None:
            if isinstance(seguros,PolizaInmueble):
                self.__seguros.append(seguros)
            elif isinstance(seguros, list):
                for seguro in seguros:
                    if isinstance(seguro, PolizaInmueble):
                        self.__seguros.append(seguro)
        
        self.__ordenarSeguros()
    
    def __ordenarSeguros(self):
        """Ordena las polizas por numero."""
        for i in range(len(self.__seguros) - 1):
            for j in range(len(self.__seguros) - 1 - i):
                if self.__seguros[j].obtenerNumero() > self.__seguros[j + 1].obtenerNumero():
                    aux = self.__seguros[j]
                    self.__seguros[j] = self.__seguros[j + 1]
                    self.__seguros[j + 1] = aux
            
    def insertar(self, poliza:PolizaInmueble):
        """Agrega una poliza a la lista de seguros."""
        if isinstance(poliza, PolizaInmueble):
            self.__seguros.append(poliza)
            self.__ordenarSeguros()
        else:
            raise TypeError("Poliza debe ser una instancia de tipo PolizaInmueble")
    
    def eliminar(self, poliza:PolizaInmueble):
        """Agrega una poliza a la lista de seguros."""
        if not isinstance(poliza, PolizaInmueble):
            raise TypeError("Poliza debe ser una instancia de tipo PolizaInmueble")
        
        self.__seguros.remove(poliza)
    
    def copiarValores(self, otraAseguradora: 'Aseguradora'):
        self.__seguros = []
        for seguro in otraAseguradora.obtenerSeguros():
            copiaSeguro = seguro.clonar()
            self.__seguros.append(copiaSeguro)
    
    #Consultas
    def obtenerSeguros(self) -> list[PolizaInmueble]:
        return self.__seguros
    
    def existePoliza(self, poliza: PolizaInmueble) -> bool:
        """Verficia si la poliza pasada por parametro existe en la lista de seguros"""
        return poliza in self.__seguros
    
    def hayPolizas(self) -> bool:
        """Retorna True si la lista tiene seguros y no esta vacia"""
        return len(self.__seguros) > 0
    
    def costoTotal(self) -> float:
        total = 0.0
        
        for poliza in self.__seguros:
            total += poliza.costoPoliza()
        
        return total
    
    def esIgualQue(self, otraAseguradora: 'Aseguradora') -> bool:
        if not isinstance(otraAseguradora, Aseguradora):
            raise TypeError("otraAseguradora debe ser una instancia de tipo Aseguradora")
        
        if self.__seguros is None and otraAseguradora.obtenerSeguros() is None:
            mismosSeguros = True
        elif (self.__seguros is None) != (otraAseguradora.obtenerSeguros() is None):
            mismosSeguros = False
        elif len(self.__seguros) != len(otraAseguradora.obtenerSeguros()):
            mismosSeguros = False
        else:
            mismosSeguros = True
            for i in range(len(self.__seguros)):
                m1 = self.__seguros[i]
                m2 = otraAseguradora.obtenerSeguros()[i]
                if not m1.esIgualQue(m2):
                    mismosSeguros = False
        
        return mismosSeguros
    
    def clonar(self) -> 'Aseguradora':
        clon = Aseguradora()
        
        if self.__seguros is not None:
            clon.__seguros = []
            for seguro in self.__seguros:
                clon.__seguros.append(seguro.clonar()) 
        else:
            clon.__seguros = None
        
        return clon
    
    def __str__(self):
        return f"Seguros: \n - {self.__seguros}"