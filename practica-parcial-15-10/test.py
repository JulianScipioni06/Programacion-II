from empleado_a_comision import EmpleadoAComision
from empleado_salario_fijo import EmpleadoSalarioFijo
from empresa import Empresa

class Tester:
    @staticmethod
    def run():
        empresa = Empresa("Empresa A")
        e1 = EmpleadoAComision("Pedro", "Perez",123, 2023,500000,100, 2000)
        e2 = EmpleadoAComision("Ana", "González",234, 2020,500000,400, 1500)
        e3 = EmpleadoSalarioFijo( "Maria", "Alvarez",345,2020,800000)
        e4 = EmpleadoSalarioFijo( "Matias", "Perez",456,2020,800000)
        empresa.agregarEmpleado(e1)
        empresa.agregarEmpleado(e2)
        empresa.agregarEmpleado(e3)
        empresa.agregarEmpleado(e4)
        empresa.mostrarEmpleados()
        print("="*60)
        print("Empleado con mas clientes en A:")
        print(empresa.empleadoConMasClientes())
        print("="*60)
        empresa2 = Empresa("Empresa A")
        empresa2.agregarEmpleado(e1)
        empresa2.agregarEmpleado(e2)
        empresa2.agregarEmpleado(e3)
        empresa2.agregarEmpleado(e4)
        print(f"esIgualSup: {empresa.esIgualSup(empresa2)}")
        print(f"esIgualsemiProf: {empresa.esIgualSemiProf(empresa2)}")
        e2 = e1
        print(e1 == e2)

if __name__ == "__main__":
    Tester.run()