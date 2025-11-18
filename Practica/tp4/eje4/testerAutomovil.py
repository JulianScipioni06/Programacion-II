from automovil import Automovil
import random as rand

class TesterAutomovil:
    @staticmethod
    def test():
        divisor = "-"*60
        auto1 = Automovil("Corolla","Toyota", 2020, 180.0, 0.0)
        auto2 = Automovil("Mustang","Ford", 2022, 250.0, 50.0)
        print(f"Datos Auto 1: \n {auto1.ObtenerModelo()} {auto1.ObtenerMarca()} {auto1.ObtenerAnio()} \n Velocidad Maxima: {auto1.ObtenerVelocidadMaxima()} \n Velocidad Actual: {auto1.ObtenerVelocidadActual()}")
        print(divisor)
        print(f"Datos Auto 2: \n {auto2.ObtenerModelo()} {auto2.ObtenerMarca()} {auto2.ObtenerAnio()} \n Velocidad Maxima: {auto2.ObtenerVelocidadMaxima()} \n Velocidad Actual: {auto2.ObtenerVelocidadActual()}")
        iteraciones = int(input("Cuantas Iteraciones quiere realizar? "))
        
        for i in range(iteraciones):
            iteracion = rand.randint(0,3)
            
            print(divisor)
            print(f"Iteracion Numero {i+1}({iteracion}):")
            
            if iteracion == 0:
                print(f"Velocidad actual = {auto1.ObtenerVelocidadActual()} km/h")
                auto1.Acelerar(20)
                print(f"Acción: Acelerar(20) → Velocidad actual = {auto1.ObtenerVelocidadActual()} km/h")

            elif iteracion == 1:
                print(f"Velocidad actual = {auto1.ObtenerVelocidadActual()} km/h")
                auto1.Desacelerar(15)
                print(f"Acción: Desacelerar(15) → Velocidad actual = {auto1.ObtenerVelocidadActual()} km/h")

            elif iteracion == 2:
                print(f"Velocidad actual = {auto1.ObtenerVelocidadActual()} km/h")
                auto1.FrenarPorCompleto()
                print(f"Acción: FrenarPorCompleto() → Velocidad actual = {auto1.ObtenerVelocidadActual()} km/h")

            elif iteracion == 3:
                print(f"Velocidad actual = {auto1.ObtenerVelocidadActual()} km/h")
                tiempo = auto1.CalcularMinutosLlegada(50)
                if tiempo is not None:
                    print(f"Acción: CalcularMinutosLlegada(50) → Tiempo = {tiempo:.2f} minutos")

if __name__ == "__main__":
    TesterAutomovil.test()