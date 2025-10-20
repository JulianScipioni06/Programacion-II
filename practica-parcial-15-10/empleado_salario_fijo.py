from empleado import Empleado

class EmpleadoSalarioFijo(Empleado):
    __PORC_2_A_5 = 0.05
    __PORC_MAS_DE_5 = 0.1
    __ANIO_LIMITE_INFERIOR = 2
    __ANIO_LIMITE_SUPERIOR = 5
    
    def __init__(self, nombre:str, apellido:str, dni:int, anioIngreso:int, sueldoBasico: float):
        super().__init__(nombre,apellido,dni,anioIngreso)
        if not isinstance(sueldoBasico, (int,float)) or sueldoBasico < 0:
            raise TypeError("El sueldo basico deber ser un numero positivo")
        
        self.__sueldoBasico = sueldoBasico
    
    def obtenerSalario(self) -> float:
        return self.__sueldoBasico * self.obtenerPorcentajeAdicional()       
        # if self.antiguedadEnAnios() < EmpleadoSalarioFijo.__ANIO_LIMITE_INFERIOR:
        #     return self.__sueldoBasico
        # elif self.antiguedadEnAnios() <= EmpleadoSalarioFijo.__ANIO_LIMITE_INFERIOR:
        #     return self.__sueldoBasico * (1 + EmpleadoSalarioFijo.__PORC_2_A_5)
        #     # return self.__sueldoBasico + self.__sueldoBasico * EmpleadoSalarioFijo.__PORC_2_A_5
        # else:
        #     return self.__sueldoBasico * (1 + EmpleadoSalarioFijo.__PORC_MAS_DE_5)
    
    def obtenerPorcentajeAdicional(self) -> int | float:
        if self.antiguedadEnAnios() < EmpleadoSalarioFijo.__ANIO_LIMITE_INFERIOR:
            return 0
        elif self.antiguedadEnAnios() <= EmpleadoSalarioFijo.__ANIO_LIMITE_INFERIOR:
            return EmpleadoSalarioFijo.__PORC_2_A_5 
            # return self.__sueldoBasico + self.__sueldoBasico * EmpleadoSalarioFijo.__PORC_2_A_5
        else:
            return EmpleadoSalarioFijo.__PORC_MAS_DE_5
    
    def __str__(self):
        return f"{super().__str__()}\n - Sueldo Basico: {self.__sueldoBasico}\n -Sueldo a Cobrar: {self.obtenerSalario()}"