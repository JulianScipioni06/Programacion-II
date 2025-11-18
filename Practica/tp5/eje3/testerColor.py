from color import Color  # Asegurate de que tu clase esté en color.py
import random as rand

class TesterColor:
    @staticmethod
    def test():
        divisor = "-" * 60
        print(divisor)
        print("🔹 TESTER DE LA CLASE COLOR 🔹")
        print(divisor)

        # 1️⃣ Creación de colores
        print("Creación de colores con distintos valores")
        c1 = Color()  # Blanco
        c2 = Color(255, 0, 0)  # Rojo puro
        c3 = Color(70, 70, 70)  # Gris
        c4 = Color(0, 0, 0)  # Negro
        print("Color 1:", c1)
        print("Color 2:", c2)
        print("Color 3:", c3)
        print("Color 4:", c4)
        print(divisor)

        # 2️⃣ Prueba de establecer colores
        print("Prueba de establecerRojo, establecerVerde y establecerAzul")
        c5 = Color()
        c5.establecerRojo(120)
        c5.establecerVerde(60)
        c5.establecerAzul(200)
        print("Color 5:", c5)
        print(divisor)

        # 3️⃣ Prueba de variar valores (positivo y negativo)
        print("Prueba de variar(valor)")
        c6 = Color(100, 50, 200)
        print("Color original:", c6)
        c6.variar(30)
        print("Después de variar(+30):", c6)
        c6.variar(-80)
        print("Después de variar(-80):", c6)
        print(divisor)

        # 4️⃣ Prueba de variarRojo, variarVerde, variarAzul
        print("Prueba individual de variaciones")
        c7 = Color(240, 5, 250)
        print("Color original:", c7)
        c7.variarRojo(20)   # debería quedar en 255
        c7.variarVerde(-10) # debería quedar en 0
        c7.variarAzul(10)   # debería quedar en 255
        print("Color modificado:", c7)
        print(divisor)

        # 5️⃣ Prueba de consultas esRojo, esGris, esNegro
        print("Prueba de esRojo(), esGris() y esNegro()")
        print(f"{c2} es rojo? → {c2.esRojo()}")
        print(f"{c3} es gris? → {c3.esGris()}")
        print(f"{c4} es negro? → {c4.esNegro()}")
        print(divisor)

        # 6️⃣ Prueba de complemento()
        print("Prueba de complemento()")
        c8 = Color(100, 150, 200)
        comp = c8.complemento()
        print(f"Color base: {c8} → Complemento: {comp}")
        print(divisor)

        # 7️⃣ Prueba de copiar()
        print("Prueba de copiar()")
        c9 = Color(50, 100, 150)
        c10 = Color()
        print("Antes de copiar:")
        print("  c9:", c9)
        print("  c10:", c10)
        c10.copiar(c9)
        print("Después de copiar:")
        print("  c10:", c10)
        print(divisor)

        # 8️⃣ Prueba de esIgualQue()
        print("Prueba de esIgualQue()")
        c11 = Color(10, 20, 30)
        c12 = Color(10, 20, 30)
        c13 = Color(0, 0, 0)
        print(f"{c11} es igual que {c12}? → {c11.esIgualQue(c12)}")
        print(f"{c11} es igual que {c13}? → {c11.esIgualQue(c13)}")
        print(divisor)

        # 9️⃣ Prueba de clonar()
        print("Prueba de clonar()")
        c14 = Color(5, 50, 100)
        c15 = c14.clonar()
        print("Color original:", c14)
        print("Clon:", c15)
        print(f"¿Mismo objeto en memoria? → {c14 is c15}")
        print(f"¿Mismo estado interno? → {c14.esIgualQue(c15)}")
        print(divisor)

        print("✅ Todas las pruebas finalizadas correctamente.")
        print(divisor)


if __name__ == "__main__":
    TesterColor.test()
