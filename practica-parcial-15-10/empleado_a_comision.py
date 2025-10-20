from empleado import Empleado

class EmpleadoAComision(Empleado):
    def __init__(self, nombre:str, apellido:str, dni:int, anioIngreso:int, salarioMinimo: float, cantClientes: int, montoPorCliente:float):
        super().__init__(nombre,apellido,dni,anioIngreso)
        if not isinstance(salarioMinimo,(int,float)) or salarioMinimo <= 0:
            raise ValueError("Ingrese un Numero valido para el Salario.")
        if not isinstance(montoPorCliente,(int,float)) or montoPorCliente < 0:
            raise ValueError("Ingrese un Numero valido para el monto por cliente.")
        if not isinstance(cantClientes,int) or cantClientes < 0:
            raise ValueError("Ingrese un Numero valido para el cantidad de Clientes.")
        
        self.__salarioMinimo = salarioMinimo
        self.__cantClientes = cantClientes
        self.__montoPorCliente = montoPorCliente
    
    def obtenerSalario(self) -> float:
        if self.__montoPorCliente * self.__cantClientes > self.__salarioMinimo:
            return self.__montoPorCliente * self.__cantClientes
        else:
            return self.__salarioMinimo
    
    def obtenerCantClientesCaptados(self):
        return self.__cantClientes
    
    def __str__(self):
        return f"EMPLEADO A COMISION \n {super.__str__()}\n - Cant Clientes Captados: {self.__cantClientes}\n - Monto Por CLiente: {self.__montoPorCliente}\n - Salario Minimo: {self.__salarioMinimo}\n - Salario a Cobrar: {self.obtenerSalario()}"