from vinoteca import Vinoteca

class TesterVinoteca:
    @staticmethod
    def test():
        divisor = 60*""
        sucursal = Vinoteca()
        print(sucursal)
        print(divisor)
        
        sucursal.VenderJugos(3000)
        sucursal.VenderVinosBlancos(1500)
        sucursal.VenderVinosTintosJovenes(500)
        sucursal.VenderVinosTintosAnejados(4000)
        print(sucursal)
        print(divisor)
        
        sucursal.ReponerJugos(1000)
        sucursal.ReponerVinosBlancos(250)
        sucursal.ReponerVinosTintosJovenes(500)
        sucursal.ReponerVinosTintosAnejados(500)
        print(sucursal)
        
        sucursal.VenderVinosBlancos(4000)
    
if __name__ == "__main__":
    TesterVinoteca.test()