from cliente import Cliente
from empleado import Empleado
from bebida import Bebida

class Tester():
    @staticmethod
    def test():
        daiquiri = Bebida("daiquiri", 2000, "trago", 500)
        gaseosa = Bebida("sprite", 1500, "refresco", 300)
        c1 = Cliente("María", 35, 20000, daiquiri)
        c2 = Cliente("Paula", 34, 25000, gaseosa)
        c3 = c1.clonacionProfunda()
        c4 = c3
        moe = Empleado("Moe", 60, "20/05/1990")
        barney = Empleado("Moe", 60, "20/05/1990")
        print("------------------------PERSONAS CARGADAS Y BEBIDAS--------------------------------")
        print(c1)
        print(c2)
        print(c3)
        print(c4)
        print(moe)
        print(barney)
        
        print("¿c1 y c3 son el mismo objeto?:", c1 is c3)
        print("¿Moe y Barney son iguales?:", moe == barney)

        print("--------------------PROBANDO METODOS------------------------")
        moe.saludar()
        c1.saludar()
        moe.hablar()
        c1.hablar()
        c1.beber()
        moe.beber()
        
        print("--------------------PROBANDO METODOS Y CONSULTAS TRIVIALES------------------------")
        vino = Bebida("Vino", 3000, "bebidas con alcohol", 30)
        print(vino)
        print("-"*60)
        vino.aumentarStock(80)
        print(f"Cantidad de Vino disponible: {vino.consultarStock()}")
        print("-"*60)
        vino.reducirStock(100)
        print(f"Cantidad de Vino disponible: {vino.consultarStock()}")
        print("-"*60)
        
        
        c4.establecerNombre("Ramon")
        c4.establecerEdad(40)
        c4.establecerDinero(30000)
        c4.establecerBebidaFavorita(vino)
        print("-"*60)
        print(f"Nombre Cliente: {c4.obtenerNombre()}")
        print(f"Edad Cliente: {c4.obtenerEdad()}")
        print(f"Dinero de Cliente: {c4.obtenerDinero()}")
        print(f"Bebida Favorita del Cliente: {c4.obtenerBebidaFavorita()}")
        
        
        barney.establecerNombre("Barney")
        barney.establecerEdad(25)
        barney.establecerFechaIngreso("23/10/2025")
        
        print("-"*60)
        print(f"Nombre Empleado: {barney.obtenerNombre()}")
        print(f"edad Empleado: {barney.obtenerEdad()}")
        print(f"fecha de Ingreso: {barney.obtenerFechaIngreso()}")
        
        
if __name__ == "__main__":
    Tester.test()