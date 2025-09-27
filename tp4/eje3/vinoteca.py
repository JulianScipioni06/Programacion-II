class Vinoteca:
    #Atributos de Clase
    __CAPACIDAD_SECCION = 5000
    
    #Constructor
    def __init__(self, cantJugos:int = 5000, cantBlancos: int = 5000, cantTintosJovenes: int = 5000, cantTintosAnejados: int = 5000):
        if not isinstance(cantJugos,int) or cantJugos > Vinoteca.__CAPACIDAD_SECCION or cantJugos < 0:
            raise ValueError("Cantidad de Jugos debe ser un Entero Positivo Menor que 5000.")
        if not isinstance(cantBlancos,int) or cantBlancos > Vinoteca.__CAPACIDAD_SECCION or cantBlancos < 0:
            raise ValueError("Cantidad de Vinos Blancos debe ser un Entero Positivo Menor que 5000.")
        if not isinstance(cantTintosJovenes,int) or cantTintosJovenes > Vinoteca.__CAPACIDAD_SECCION or cantTintosJovenes < 0:
            raise ValueError("Cantidad de Vinos Tintos Jovenes debe ser un Entero Positivo Menor que 5000.")
        if not isinstance(cantTintosAnejados,int) or cantTintosAnejados > Vinoteca.__CAPACIDAD_SECCION or cantTintosAnejados < 0:
            raise ValueError("Cantidad de Vinos Tintos Añejados debe ser un Entero Positivo Menor que 5000.")
        
        self.__cantJugos = cantJugos
        self.__cantBlancos = cantBlancos
        self.__cantTintosJovenes = cantTintosJovenes
        self.__cantTintosAnejados = cantTintosAnejados
    
    #Comandos
    def ReponerJugos(self,cantidad:int):
        """Repone la cantidad de jugos disponibles. Requiere que cantJugos < 5000"""
        if not isinstance(cantidad,int) or cantidad < 0:
            raise ValueError("Cantidad debe ser Un Entero Positivo")
        if self.__cantJugos + cantidad > Vinoteca.__CAPACIDAD_SECCION:
            raise ValueError("No se puede reponer porque supera la Capacidad Maxima(5000).")
        if self.__cantJugos + cantidad <= Vinoteca.__CAPACIDAD_SECCION:
            self.__cantJugos += cantidad
    
    def ReponerVinosBlancos(self,cantidad:int):
        """Repone la cantidad de Vinos Blancos disponibles. Requiere que cantBlancos < 5000"""
        if not isinstance(cantidad,int) or cantidad < 0:
            raise ValueError("Cantidad debe ser Un Entero Positivo")
        if self.__cantBlancos + cantidad > Vinoteca.__CAPACIDAD_SECCION:
            raise ValueError("No se puede reponer porque supera la Capacidad Maxima(5000).")
        if self.__cantBlancos + cantidad <= Vinoteca.__CAPACIDAD_SECCION:
            self.__cantBlancos += cantidad 
    
    def ReponerVinosTintosJovenes(self,cantidad:int):
        """Repone la cantidad de Tintos Jovenes disponibles. Requiere que CantJugos < 5000"""
        if not isinstance(cantidad,int) or cantidad < 0:
            raise ValueError("Cantidad debe ser Un Entero Positivo")
        if self.__cantTintosJovenes + cantidad > Vinoteca.__CAPACIDAD_SECCION:
            raise ValueError("No se puede reponer porque supera la Capacidad Maxima(5000).")
        if self.__cantTintosJovenes + cantidad <= Vinoteca.__CAPACIDAD_SECCION:
            self.__cantTintosJovenes += cantidad  
    
    def ReponerVinosTintosAnejados(self,cantidad:int):
        """Repone la cantidad de Tintos Anejados disponibles. Requiere que CantJugos < 5000"""
        if not isinstance(cantidad,int) or cantidad < 0:
            raise ValueError("Cantidad debe ser Un Entero Positivo")
        if self.__cantTintosAnejados + cantidad > Vinoteca.__CAPACIDAD_SECCION:
            raise ValueError("No se puede reponer porque supera la Capacidad Maxima(5000).")
        if self.__cantTintosAnejados + cantidad <= Vinoteca.__CAPACIDAD_SECCION:
            self.__cantTintosAnejados += cantidad
    
    def VenderJugos(self,unidades:int):
        """
        Resta la cantidad vendida de Jugos solicitada. 
        Si la cantidad del deposito no es suficiente, se vende lo que se puede.
        """
        if not isinstance(unidades,int) or unidades < 0:
            raise ValueError("Unidades debe ser Un Entero Positivo")
        if unidades > self.__cantJugos:
            print(f"Solo podemos vender {self.__cantJugos} Jugos. No tenemos Suficientes Unidades.")
            self.__cantJugos = 0
        else:
            self.__cantJugos -= unidades
    
    def VenderVinosBlancos(self,unidades:int):
        """
        Resta la cantidad vendida de Vinos Blancos solicitada. 
        Si la cantidad del deposito no es suficiente, se vende lo que se puede.
        """
        if not isinstance(unidades,int) or unidades < 0:
            raise ValueError("Unidades debe ser Un Entero Positivo")
        if unidades > self.__cantBlancos:
            print(f"Solo podemos vender {self.__cantBlancos} Vinos Blancos. No tenemos Suficientes Unidades.")
            self.__cantBlancos = 0
        else:
            self.__cantBlancos -= unidades
    
    def VenderVinosTintosJovenes(self,unidades:int):
        """
        Resta la cantidad vendida de Vinos Tintos Jovenes solicitada. 
        Si la cantidad del deposito no es suficiente, se vende lo que se puede.
        """
        if not isinstance(unidades,int) or unidades < 0:
            raise ValueError("Unidades debe ser Un Entero Positivo")
        if unidades > self.__cantTintosJovenes:
            print(f"Solo podemos vender {self.__cantTintosJovenes} Vinos Tintos Jovenes. No tenemos Suficientes Unidades.")
            self.__cantTintosJovenes = 0
        else:
            self.__cantTintosJovenes -= unidades
    
    def VenderVinosTintosAnejados(self,unidades:int):
        """
        Resta la cantidad vendida de Vinos Tintos Añejados solicitada. 
        Si la cantidad del deposito no es suficiente, se vende lo que se puede.
        """
        if not isinstance(unidades,int) or unidades < 0:
            raise ValueError("Unidades debe ser Un Entero Positivo")
        if unidades > self.__cantTintosAnejados:
            print(f"Solo podemos vender {self.__cantTintosAnejados} Vinos Tintos Añejados. No tenemos Suficientes Unidades.")
            self.__cantTintosAnejados = 0
        else:
            self.__cantTintosAnejados -= unidades
    
    #Consultas
    def ObtenerCantidadJugos(self) -> int:
        return self.__cantJugos
    def ObtenerCantidadVinosBlancos(self) -> int:
        return self.__cantBlancos
    def ObtenerCantidadVinosTintosJovenes(self) -> int:
        return self.__cantTintosJovenes
    def ObtenerCantidadVinosTintosAnejados(self) -> int:
        return self.__cantTintosAnejados
    
    def __str__(self)->str:
        return f"Cantidad en Stock: \n - Jugos Sin alcohol: {self.__cantJugos} \n - Vinos Blancos: {self.__cantBlancos} \n - Vinos Tintos Jovenes: {self.__cantTintosJovenes} \n - Vinos Tintos Anejados: {self.__cantTintosAnejados} \n"
