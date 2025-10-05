from fecha import Fecha  # Asegurate de que el archivo de la clase se llame fecha.py
import random as rand

class TesterFecha:
    @staticmethod
    def test():
        divisor = "-" * 60
        print(divisor)
        print("🔹 TESTER DE LA CLASE FECHA 🔹")
        print(divisor)

        # Creación de fechas
        print("Creación de fechas con distintos valores")
        f1 = Fecha()  # 1/1/1
        f2 = Fecha(15, 3, 2024)
        f3 = Fecha(28, 2, 2024)  # Año bisiesto
        f4 = Fecha(31, 12, 2023)
        
        print("Fecha 1:", f1)
        print("Fecha 2:", f2)
        print("Fecha 3:", f3)
        print("Fecha 4:", f4)
        print(divisor)

        # Prueba de diaSiguiente
        print("Prueba de diaSiguiente()")
        print("Día siguiente a", f3, "→", f3.diaSiguiente())
        print("Día siguiente a", f4, "→", f4.diaSiguiente())
        print(divisor)

        # Prueba de sumaDias
        print("Prueba de sumaDias()")
        suma1 = f3.sumaDias(5)
        suma2 = f4.sumaDias(60)
        print(f"Sumando 5 días a {f3} → {suma1}")
        print(f"Sumando 60 días a {f4} → {suma2}")
        print(divisor)

        # Prueba de esIgualQue
        print("4️⃣ Prueba de esIgualQue()")
        f5 = Fecha(15, 3, 2024)
        print(f"{f2} es igual que {f5}? →", f2.esIgualQue(f5))
        print(f"{f1} es igual que {f2}? →", f1.esIgualQue(f2))
        print(divisor)

        # Prueba de esAnterior
        print("5️⃣ Prueba de esAnterior()")
        print(f"{f1} es anterior a {f2}? →", f1.esAnterior(f2))
        print(f"{f4} es anterior a {f3}? →", f4.esAnterior(f3))
        print(f"{f3} es anterior a {f4}? →", f3.esAnterior(f4))
        print(divisor)

        # Prueba de comandos
        print("6️⃣ Prueba de setters (EstablecerDia, Mes, Anio)")
        f6 = Fecha()
        f6.EstablecerDia(20)
        f6.EstablecerMes(10)
        f6.EstablecerAnio(2025)
        print("Fecha modificada con setters:", f6)
        print(divisor)

        # Prueba de obtención
        print("7️⃣ Prueba de getters")
        print(f"Día: {f6.ObtenerDia()} | Mes: {f6.ObtenerMes()} | Año: {f6.ObtenerAnio()}")
        print(divisor)

        # Prueba combinada: cadena de operaciones
        print("8️⃣ Prueba combinada: sumar días y verificar igualdad")
        f7 = Fecha(25, 12, 2024)
        f8 = f7.sumaDias(7)
        print(f"Fecha base: {f7} | Fecha +7 días: {f8}")
        print(f"{f7} es anterior a {f8}? → {f7.esAnterior(f8)}")
        print(f"{f7} es igual a {f8}? → {f7.esIgualQue(f8)}")

        print(divisor)
        print("✅ Todas las pruebas finalizadas correctamente.")
        print(divisor)


if __name__ == "__main__":
    TesterFecha.test()
