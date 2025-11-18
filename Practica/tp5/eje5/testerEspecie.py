from especie import Especie
import random

class TesterEspecie:
    @staticmethod
    def test():
        divisor = "-"*60
        #especie1 = Especie("Yaguareté", machos=20, hembras=30, ritmo=0.08)
        especie1 = Especie("Yaguarete")
        especie2 = Especie("Tigre", random.randint(0,100), random.randint(0,100), ritmo=0.05)
        especie3 = Especie("Puma", random.randint(0,100), random.randint(0,100), ritmo=0.02)
        
        print("ESPECIES CREADAS")
        print(divisor)
        print(especie1)
        print(divisor)
        print(especie2)
        print(divisor)
        print(especie3)
        print(divisor)
        
        print("-----PROBANDO ESTABLECER----- \n")
        especie1.establecerMachos(20)
        especie1.establecerHembras(30)
        especie1.establecerRitmo(0.08)
        print(especie1)
        
        print(divisor)
        print("-----PROBANDO ACTUALIZAR-----")
        print(divisor)
        print(f"ESPECIE 2 ACTUAL: \n {especie2}")
        especie2.actualizarMachos(50)
        especie2.actualizarHembras(-5)
        especie2.actualizarRitmo(0.09)
        print(divisor)
        print(f"ESPECIE 2 AHORA: \n {especie2}")
        
        print(divisor)
        print("PROBANDO CONSULTAS")
        print(divisor)
        print("POBLACION ACTUAL")
        print(f"ESPECIE: {especie3.obtenerNombre()} --> POBLACION ACTUAL: {especie3.poblacionActual()}")
        print(divisor)
        print("POBLACION ESTIMADA")
        print(f"ESPECIE: {especie3.obtenerNombre()} --> POBLACION EN 2 AÑOS: {especie3.poblacionEstimada(2)}")
        print(divisor)
        print("AÑOS PARA POBLACION")
        anios = especie3.aniosParaPoblacion(80)
        print(f"ESPECIE: {especie3.obtenerNombre()} --> AÑOS PARA QUE LA POBLACION SEA 80: {anios}")
        print(divisor)
        print("RIESGO DE ESPECIE")
        print(f"ESPECIE: {especie3.obtenerNombre()} --> RIESGO DE ESPECIE: {especie3.riesgo()}")
        print(divisor)
        print("MAS HEMBRAS")
        print(f"ESPECIE: {especie3.obtenerNombre()}")
        if(especie3.masHembras() == None):
            print(f"ESPECIE: {especie3.obtenerNombre()} TIENE LA MISMA CANTIDAD DE MACHOS Y HEMBRAS")
        elif(especie3.masHembras()):
            print(f"ESPECIE: {especie3.obtenerNombre()} TIENE MAS HEMBRAS")
        else:
            print(f"ESPECIE: {especie3.obtenerNombre()} TIENE MAS MACHOS")
        print(divisor)
        print("MAYOR RITMO")
        resultado = especie1.mayorRitmo(especie2)
        if resultado is None:
            print("Caso 1: Ritmos iguales.")
        else:
            print(f"RESULTADO 1: {resultado.obtenerNombre()} tiene mayor ritmo ({resultado.obtenerRitmo()})")
        
        print(divisor)
        print("CLONAR")
        print(divisor)
        print("ESPECIE CLONADA 1")
        print(especie1)
        especie4 = especie1.clonar()
        print("ESPECIE CLONADA 4")
        print(especie4)

if __name__ == "__main__":
    TesterEspecie.test()