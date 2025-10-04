from automovil import Automovil
import random as rand

class TesterAutomovil:
    @staticmethod
    def test():
        divisor = "-"*60
        auto1 = Automovil()
        
        auto1.EstablecerMarca(input("Ingrese la Marca del Vehiculo: "))
        auto1.EstablecerModelo(input("Ingrese el Modelo del Vehiculo: "))
        auto1.EstablecerAnio(int(rand.randint(1920,2025)))
        auto1.EstablecerVelocidadMaxima(float(rand.randint(80,240)))
        auto1.EstablecerVelocidadActual(float(rand.randint(0,240)))
        
        print(divisor)
        print(auto1)
        print(divisor)
        iteraciones = int(input("Cuantas Iteraciones quiere realizar? "))
        
        for i in range(iteraciones):
            iteracion = rand.randint(0,3)
            
            print(divisor)
            print(f"Iteracion Numero {i+1}({iteracion}):")
            
            if iteracion == 0:
                incremento = rand.randint(5, 30)
                print(f"Velocidad actual = {auto1.ObtenerVelocidadActual()} km/h")
                auto1.Acelerar(incremento)
                print(f"Acción: Acelerar(20) → Velocidad actual = {auto1.ObtenerVelocidadActual()} km/h")

            elif iteracion == 1:
                decremento = rand.randint(5, 30)
                print(f"Velocidad actual = {auto1.ObtenerVelocidadActual()} km/h")
                auto1.Desacelerar(decremento)
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