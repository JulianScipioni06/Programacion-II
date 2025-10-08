from color import Color  # Asegurate de que tu clase esté en color.py
import random as rand

class TesterColor:
    @staticmethod
    def test():
        divisor = "-"*60
        color_1 = Color() 
        color_2 = Color(70, 70, 70) 
        color_3 = Color(255, 255, 255) 
        igualdad1 = color_1.esIgualQue(color_2) 
        igualdad2 = color_2.esIgualQue(color_3) 
        color_4 = color_1 
        color_5 = color_2.clonar()
        
        print(divisor)
        print(color_1)
        print(divisor)
        print(color_2)
        print(divisor)
        print(color_3)
        print(divisor)
        print(color_4)
        print(divisor)
        print(color_5)
        print(divisor)
        print(divisor)
        print(f"Rsultado Igualdad 1: {igualdad1}")
        print(f"Rsultado Igualdad 2: {igualdad2}")


if __name__ == "__main__":
    TesterColor.test()
