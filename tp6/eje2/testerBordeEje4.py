from borde import Borde
from color import Color

class TesterBorde:
    def test():
        C1 = Color(150, 150, 150) 
        C2 = Color(150, 150, 150) 
        B1 = Borde(1,C1) 
        B2 = Borde(1,C2) 
        B3 = B2.clonarProf() 
        B4 = Borde(B2.obtenerGrosor(), B2.obtenerColor()) 
        print(B2 == B3) 
        print(B2 == B4) 
        print(B2.esIgualQue(B1)) 
        print(B2.esIgualQue(B3)) 
        print(B2.obtenerGrosor() == B1.obtenerGrosor() and B2.obtenerColor() == B1.obtenerColor()) 
        print(B2.obtenerGrosor() == B3.obtenerGrosor() and B2.obtenerColor() == B3.obtenerColor()) 
        print(B2.obtenerGrosor() == B1.obtenerGrosor() and B2.obtenerColor().esIgualQue(B1.obtenerColor())) 
        print(B2.obtenerGrosor() == B4.obtenerGrosor() and B2.obtenerColor().esIgualQue(B4.obtenerColor()))
    
if __name__ == "__main__":
    TesterBorde.test()