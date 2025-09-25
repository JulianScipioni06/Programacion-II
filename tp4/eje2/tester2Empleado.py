from empleado import Empleado

class TesterEmpleado2:
    @staticmethod
    def Test():
        separador = "-"*60
        legajo = int(input("Nro de Legajo del Empleado: "))
        cantHoras= int(input("Cantidad de Horas que Trabajo: "))
        costoHora = int(input("Cobro Por Hora del Empleado: "))
        empleado1 = Empleado(legajo,cantHoras,costoHora)
        
        print(empleado1)
        
        print(separador)
        print(f"Sueldo Empleado 1(Datos Usuario): {empleado1.ObtenerSueldo()}")
    
        print(separador)
        print("Probando Comandos")
        empleado1.EstablecerHorasTrabajadas(128)
        empleado1.EstablecerValorHora(6000)
        print(f"Horas trabajadas Empleado 1: {empleado1.ObtenerHorasTrabajadas()}")
        print(f"Valor de Hora Empleado 1: {empleado1.ObtenerValorHora()}")
        print(f"Sueldo Empleado 1: {empleado1.ObtenerSueldo()}")


if __name__ == "__main__":
    TesterEmpleado2.Test()