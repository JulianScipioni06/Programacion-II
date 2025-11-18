from borde import Borde
from color import Color

class TesterBorde:
    def test():
        C1 = Color(150, 150, 150) 
        C2 = Color(150, 150, 150) 
        B1 = Borde(1,C1) 
        B2 = Borde(1,C2) 
        print(C1 == C2) 
        print(B1 == B2) 
        print(C1.esIgualQue(C2)) 
        print(B1.esIgualQue(B2))
    
if __name__ == "__main__":
    TesterBorde.test()