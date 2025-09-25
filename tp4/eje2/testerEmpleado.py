from empleado import Empleado

class TesterEmpleado:
    @staticmethod
    def Test():
        separador = "-"*60
        empleado1 = Empleado(123,50,1500)
        empleado2 = Empleado(999,valorHora=1000)
        empleado3 = Empleado(550)
        
        print(empleado1)
        print(separador)
        print(empleado2)
        print(separador)
        print(empleado3)
        
        print(separador)
        print(f"Sueldo Empleado 1: {empleado1.ObtenerSueldo()}")
        
        print(separador)
        empleado2.EstablecerHorasTrabajadas(150)
        print(f"Horas trabajadas Empleado 2: {empleado2.ObtenerHorasTrabajadas()}")
        print(f"Sueldo Empleado 2: {empleado2.ObtenerSueldo()}")
        
        print(separador)
        empleado3.EstablecerHorasTrabajadas(15)
        empleado3.EstablecerValorHora(2000)
        print(f"Horas trabajadas Empleado 3: {empleado3.ObtenerHorasTrabajadas()}")
        print(f"Valor de Hora Empleado 3: {empleado3.ObtenerValorHora()}")
        print(f"Sueldo Empleado 3: {empleado3.ObtenerSueldo()}")
        
        print(separador)
        empleado1.EstablecerHorasTrabajadas(128)
        empleado1.EstablecerValorHora(6000)
        print(f"Horas trabajadas Empleado 1: {empleado1.ObtenerHorasTrabajadas()}")
        print(f"Valor de Hora Empleado 1: {empleado1.ObtenerValorHora()}")
        print(f"Sueldo Empleado 1: {empleado1.ObtenerSueldo()}")


if __name__ == "__main__":
    TesterEmpleado.Test()