from tamagotchi import Tamagotchi

class TesterTamagotchi:
    @staticmethod
    def test():
        divisor = "-" * 60
        mascota = Tamagotchi("Firulais")
        
        # Estado inicial
        print("Estado inicial de la mascota:")
        print(mascota)
        print(divisor)
        
        print("Probando Comer()")
        mascota.Comer()
        print(mascota)
        print(divisor)

        print("Probando Beber()")
        mascota.Beber()
        print(mascota)
        print(divisor)

        print("Probando Jugar()")
        mascota.Jugar()
        print(mascota)
        print(divisor)

        print("Probando Caminar()")
        mascota.Caminar()
        print(mascota)
        print(divisor)

        print("Probando Saltar()")
        mascota.Saltar()
        print(mascota)
        print(divisor)

        print("Probando Bañar()")
        mascota.Banar()
        print(mascota)
        print(divisor)

        print("Probando Dormir()")
        mascota.Dormir()
        print(mascota)
        print(divisor)

        print("Probando Despertar()")
        mascota.Despertar()
        print(mascota)
        print(divisor)

        # Forzar 3 actividades de desgaste consecutivas
        print("Probando límite de 3 desgastes consecutivos")
        mascota.Jugar()
        mascota.Caminar()
        mascota.Saltar()
        print(mascota)
        print(divisor)

        # Cuarta acción de desgaste → debería dormir
        print("Cuarta acción de desgaste (debería dormirse)")
        mascota.Jugar()
        print(mascota)
        print(divisor)

        # Forzar muerte reduciendo energía
        print("Forzando muerte (restando energía con Saltar)")
        while mascota.EstaVivo():
            mascota.Saltar()
        print(mascota)
        print("⚠️ La mascota ha muerto, ya no puede hacer más acciones.")
        print(divisor)

if __name__ == "__main__":
    TesterTamagotchi.test()

