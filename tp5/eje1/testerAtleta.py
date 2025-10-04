from atleta import Atleta
import random as rand

class TesterAtleta:
    @staticmethod
    def test():
        divisor = "-"*60
        pepe = Atleta("Pepe Argento")
        julio = Atleta("Julio Leiva")
        
        print(pepe)
        print(divisor)
        print(julio)
        
        print(divisor)
        print("Pruebas del Tester")
        print(divisor)
        
        for i in range(rand.randint(1,15)):
            pepe.Entrenar()
        
        for i in range(rand.randint(1,15)):
            julio.Entrenar()
        
        print(f"Energia de Pepe: {pepe.ObtenerEnergia()}")
        print(f"Destreza de Pepe: {pepe.ObtenerDestreza()}")
        print(f"Entrenamientos de Pepe: {pepe.ObtenerCantidadEntrenamientos()}")
        print(divisor)
        print(f"Energia de Julio: {julio.ObtenerEnergia()}")
        print(f"Destreza de Julio: {julio.ObtenerDestreza()}")
        print(f"Entrenamientos de Julio: {julio.ObtenerCantidadEntrenamientos()}")
        
        print(divisor)
        print("Prueba de Funciones mismaDestreza y esMejor")
        print(divisor)
        
        pepe.Descansar()
        julio.Descansar()
        
        if(pepe.mismaDestrezaQue(julio)):
            print(f"{pepe.ObtenerNombre()} Tiene la Misma Destreza que {julio.ObtenerNombre()}")
        else:
            print(f"{pepe.ObtenerNombre()} NO Tiene la Misma Destreza que {julio.ObtenerNombre()}")
        
        if(pepe.esMejorQue(julio)):
            print(f"{pepe.ObtenerNombre()} Tiene Mejor Destreza que {julio.ObtenerNombre()}")
        else:
            print(f"{pepe.ObtenerNombre()} NO Tiene Mejor Destreza que {julio.ObtenerNombre()}")
if __name__ == "__main__":
    TesterAtleta.test()