class Empleado:
    def __init__(self, legajo:int, horasTrabajadasMes:int = 0, valorHora:float = 0.0):
        """
        Inicializa un nuevo Empleado.
        
        Parametros:
        - legajo: Legajo unico del Empleado.
        - horasTrabajadasMes: Cantidad de Horas que Trabajo un empleado en el mes.
        - valorHora: Preio de la Hora que cobra el Empleado.
        
        Requerimientos:
        - legajo > 0 y tipo int
        - horasTrabajadasMes >= 0 y tipo int (default = 0)
        - valorHora > 0 y tipo float (default = 0.0)
        """
        
        if not isinstance(legajo,int) or legajo <= 0:
            raise ValueError("El lejago debe ser un Numero Entero Positivo")
        if not isinstance(horasTrabajadasMes,int) or horasTrabajadasMes < 0:
            raise ValueError("Las Horas trabajadas debe ser un Numero Entero Positivo o 0")
        if not isinstance(valorHora,(int,float)) or valorHora < 0.0:
            raise ValueError("El valor de la Hora debe ser un Numero Positivo")
        
        self.__legajo = legajo
        self.__horasTrabajadasMes = horasTrabajadasMes
        self.__valorHora =valorHora
    
    #Comandos de Empleado
    def EstablecerHorasTrabajadas(self,cantHoras:int):
        """
        Establece las horas trabajadas en el mes. Requiere cantHoras >= 0 y tipo int.
        Parametros:
        - cantHoras: La cantidad de horas a Establecer.
        """
        if not isinstance(cantHoras,int) or cantHoras < 0:
            raise ValueError("La cantidad de Horas debe Ser un Numero Entero Positivo")
        
        self.__horasTrabajadasMes = cantHoras
    
    def EstablecerValorHora(self,valorHora:float):
        """
        Establece el precio de la Hora del Empleado. Requiere valorHora > 0 y tipo int o float.
        Parametros:
        - valorHora: El precio de la hora.
        """
        if not isinstance(valorHora,(int,float)) or valorHora <= 0:
            raise ValueError("El valor de la Hora debe ser un Numero Positivo > 0")
        
        self.__valorHora = valorHora
    
    #Consultas de Empleado
    def ObtenerLegajo(self) -> int:
        """Devuelve el Numero de Legajo del Empleado"""
        return self.__legajo
    
    def ObtenerHorasTrabajadas(self) -> int:
        """Devuelve La cantidad de Horas Trabajadas del Empleado"""
        return self.__horasTrabajadasMes
    
    def ObtenerValorHora(self) -> float:
        """Devuelve el precio de la hora del Empleado"""
        return self.__valorHora
    
    def ObtenerSueldo(self) -> float:
        """Devuelve el resultado de multiplicar la cantidad de horas trabajadas por el valor de cada hora"""
        return self.__horasTrabajadasMes * self.__valorHora
    
    def __str__(self)->str:
        return f"- Legajo: {self.__legajo} \n- Horas Trabajadas: {self.__horasTrabajadasMes} \n- Valor Hora: {self.__valorHora}"
