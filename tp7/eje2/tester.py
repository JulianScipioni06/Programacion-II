from inmueble import Inmueble
from departamento import Departamento
from quinta import Quinta

class TesterInmueble:
    @staticmethod
    def test():
        depa1 = Departamento(101,"Av. Colón 1234","Lucía Gómez",80,1,15000.0,True)
        depa2 = Departamento(102,"Sarmiento 850","Carlos Pérez",60,0,12000.0,False)
        quinta1 = Quinta(201,"Ruta 33 km 10","María López",150,1,600)
        quinta2 = Quinta(202,"Camino Viejo 55","Juan Torres",120,2,200)
        
        print(depa1)
        print("-"*60)
        print(depa2)
        print("-"*60)
        print(quinta1)
        print("-"*60)
        print(quinta2)
        
        print("-"*60)
        depa3 = depa1.clonar()
        print(depa3)
        print("-"*60)
        quinta3 = quinta2.clonar()
        print(quinta3)
        print("-"*60)
        
        print("-----------------Probando Metodos--------------------")
        print(f"depa1 Es igual que depa2? {depa1.esIgualQue(depa2)}")
        print(f"depa1 Es igual que depa3? {depa1.esIgualQue(depa3)}")
        print(f"quinta1 Es igual que quinta2? {quinta1.esIgualQue(quinta2)}")
        print(f"quinta2 Es igual que quinta3? {quinta2.esIgualQue(quinta3)}")
        
        print("-"*60)
        depa2.copiarValores(depa1)
        print(depa2)
        print("-"*60)
        print(f"depa1 Es igual que depa2? {depa1.esIgualQue(depa2)}")

if __name__ == "__main__":
    TesterInmueble.test()