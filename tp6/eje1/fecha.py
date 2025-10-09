class Fecha:
    def __init__(self,  dia:int = 1, mes:int = 1, anio:int = 1):
        if not isinstance(dia, int) or dia < 1 or dia > 31:
            raise ValueError("El dia Debe ser un Entero Positivo menor o igual que 31 (0 no cuenta)")
        if not isinstance(mes, int) or mes < 1 or mes > 12:
            raise ValueError("El mes Debe ser un Entero Positivo menor o igual que 12 (0 no cuenta)")
        if not isinstance(anio, int) or anio < 1:
            raise ValueError("El Año Debe ser un Entero Positivo (0 no cuenta)")
        
        self.__dia = dia
        self.__mes = mes
        self.__anio = anio
        
    #Metodos Auxiliares
    def __EsBisiesto(self, anio:int)->bool:
        """Retorna True si el Año es Bisiesto o Falso sino lo es."""
        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
            return True
        else:
            return False
    
    def __diasDelMes(self, mes:int, anio:int=None)->int:
        """Devuelve la Cantidad de Dias segun el mes pasado por parametro"""
        if anio is None:
            anio = self.__anio
        
        if mes in [1,3,5,7,8,10,12]:
            return 31
        elif mes in [4,6,9,11]:
            return 30
        elif mes == 2:
            if self.__EsBisiesto(anio): 
                return 29
            else:
                return 28
    
    #Comandos
    def EstablecerDia(self, dia:int):
        if not isinstance(dia, int) or dia < 1 or dia > 31:
            raise ValueError("El dia Debe ser un Entero Positivo menor o igual que 31 (0 no cuenta)")
        self.__dia = dia
    def EstablecerMes(self, mes:int):
        if not isinstance(mes, int) or mes < 1 or mes > 12:
            raise ValueError("El mes Debe ser un Entero Positivo menor o igual que 12 (0 no cuenta)")
        self.__mes = mes
    def EstablecerAnio(self, anio:int):
        if not isinstance(anio, int) or anio < 1:
            raise ValueError("El Año Debe ser un Entero Positivo (0 no cuenta)")
        self.__anio = anio
    
    #Consultas
    def ObtenerDia(self):
        return self.__dia
    def ObtenerMes(self):
        return self.__mes
    def ObtenerAnio(self):
        return self.__anio
    
    def esAnterior(self,otraFecha:'Fecha')->bool:
        if self.__anio == otraFecha.__anio:
            if self.__mes == otraFecha.__mes:
                if self.__dia < otraFecha.__dia:
                    return True
                else:
                    return False
            elif self.__mes < otraFecha.__mes:
                return True
            else:
                return False
        elif self.__anio < otraFecha.__anio:
            return True
        else:
            return False
    
    def sumaDias(self, cantDias: int) -> 'Fecha':
        """
        Retorna una nueva Fecha que resulta de sumar cantDias a la fecha actual.
        No modifica el objeto original.
        """
        if not isinstance(cantDias, int) or cantDias < 0:
            raise ValueError("La cantidad de días debe ser un entero positivo.")

        dia = self.__dia + cantDias
        mes = self.__mes
        anio = self.__anio

        
        while dia > self.__diasDelMes(mes, anio):
            dia -= self.__diasDelMes(mes, anio)
            mes += 1
            if mes > 12:
                mes = 1
                anio += 1

        
        return Fecha(dia, mes, anio)
    
    def diasHasta(self, otraFecha: 'Fecha') -> int:
        """
        Devuelve la cantidad de días entre la fecha actual (self)
        y otraFecha, sin usar datetime.
        """
        if not isinstance(otraFecha, Fecha):
            raise TypeError("El parámetro debe ser una instancia de 'Fecha'")

        # Si son iguales, no hay diferencia
        if self.esIgualQue(otraFecha):
            return 0

        contador = 0
        fecha_temp = Fecha(self.__dia, self.__mes, self.__anio)

        # Si self es anterior, sumo días hasta alcanzar la otra fecha
        if fecha_temp.esAnterior(otraFecha):
            while not fecha_temp.esIgualQue(otraFecha):
                fecha_temp = fecha_temp.sumaDias(1)
                contador += 1
        else:
            # Si self es posterior, resto días (resultado negativo)
            while not fecha_temp.esIgualQue(otraFecha):
                fecha_temp = fecha_temp.sumaDias(-1)
                contador -= 1
        return contador

    
    def diaSiguiente(self):
        """
        Retorna una nueva Fecha con el día siguiente a la fecha actual.
        No modifica la fecha original.
        """
        
        return self.sumaDias(1)
    
    def esIgualQue(self, otraFecha:'Fecha'):
        mismoDia = self.__dia == otraFecha.__dia
        mismoMes = self.__mes == otraFecha.__mes
        mismoAnio = self.__anio == otraFecha.__anio
        return mismoDia and mismoMes and mismoAnio
    
    def __str__(self):
        return f"{self.__dia}/{self.__mes}/{self.__anio}"
