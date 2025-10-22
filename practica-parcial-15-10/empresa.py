from empleado import Empleado
from empleado_a_comision import EmpleadoAComision

class Empresa():
    def __init__(self, nombre:str):
        if not isinstance(nombre,str) or nombre.split() == "":
            raise TypeError("El nombre de la empresa debe ser una cadena valida")
        
        self.__nombre = nombre
        self.__empleados = []
    
    def agregarEmpleado(self,empleado: Empleado):
        if not isinstance(empleado,Empleado):
            raise TypeError("El empleado debe ser un objeto de tipo Empleado")
        
        if not empleado in self.__empleados:
            self.__empleados.append(empleado)
    
    def mostrarEmpleados(self) -> str:
        for emp in self.__empleados:
            print(emp)
    
    def empleadoConMasClientes(self) -> 'Empleado':
        empConMasClientes = None
        maxClientes = -1
        for emp in self.__empleados:
            if isinstance(emp, EmpleadoAComision):
                if emp.obtenerCantClientesCaptados() > maxClientes:
                    empConMasClientes = emp
                    maxClientes = emp.obtenerCantClientesCaptados()
        
        return empConMasClientes
    
    def obtenerNombre(self):
        return self.__nombre
    
    def obtenerEmpleados(self):
        return self.__empleados
    
    def esIgualSup(self, otraEmpresa: 'Empresa') -> bool:
        return self == otraEmpresa #Compara referencia de objetos empresa
    
    def esIgualSemiProf(self, otraEmpresa:'Empresa') -> bool:
        return self.__nombre == otraEmpresa.obtenerNombre() and self.__empleados == otraEmpresa.obtenerEmpleados()