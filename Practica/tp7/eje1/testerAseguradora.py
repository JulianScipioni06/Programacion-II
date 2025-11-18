from polizaInmueble import PolizaInmueble
from polizaInmuebleEscolar import PolizaInmuebleEscolar
from aseguradora import Aseguradora

class TesterAseguradora:
    def test():
        print("========== TESTER DE CLASES ==========\n")

        # 1️⃣ CREACIÓN DE OBJETOS
        print("Creando pólizas...")

        p1 = PolizaInmueble(1, incendio=1000, explosion=500, robo=300)
        p2 = PolizaInmueble(2, incendio=1500, explosion=700, robo=400)
        p3 = PolizaInmuebleEscolar(3, incendio=2000, explosion=1000, robo=800,cantPersonas=8, montoEquipamiento=50000,montoMobiliario=30000, montoPersona=1000)

        print("Pólizas creadas correctamente.\n")

        # 2️⃣ TESTEO DE MÉTODOS INDIVIDUALES
        print("---- Test de métodos de PolizaInmueble ----")
        print(p1)
        print(f"Costo total p1: {p1.costoPoliza()}\n")

        print("---- Test de métodos de PolizaInmuebleEscolar ----")
        print(p3)
        print(f"Costo total p3 (con >5 personas): {p3.costoPoliza()}\n")

        print("---- Test de clonar() y esIgualQue() ----")
        clon_p1 = p1.clonar()
        print(f"¿El clon es igual al original?: {clon_p1.esIgualQue(p1)}")
        print(f"¿Son el mismo objeto?: {clon_p1 is p1}\n")

        # 3️⃣ TEST DE ASEGURADORA
        print("========== TEST DE ASEGURADORA ==========")
        aseg = Aseguradora()
        aseg.insertar(p2)
        aseg.insertar(p3)
        aseg.insertar(p1)

        print("\n-- Pólizas ordenadas por número --")
        for poliza in aseg.obtenerSeguros():
            print(f"N°{poliza.obtenerNumero()} -> Costo: {poliza.costoPoliza()}")

        print(f"\nHay pólizas?: {aseg.hayPolizas()}")
        print(f"Costo total de la aseguradora: {aseg.costoTotal()}\n")

        # Eliminación de una póliza
        print("-- Eliminando la póliza número 2 --")
        aseg.eliminar(p2)
        for poliza in aseg.obtenerSeguros():
            print(f"N°{poliza.obtenerNumero()} -> Costo: {poliza.costoPoliza()}")

        # Copia y clonación
        print("\n-- Copiando valores a otra aseguradora --")
        otra = Aseguradora()
        otra.copiarValores(aseg)
        print("¿Son iguales?:", aseg.esIgualQue(otra))

        print("\n-- Clonando aseguradora --")
        clon = aseg.clonar()
        print("¿El clon es igual?:", aseg.esIgualQue(clon))
        print("¿Es el mismo objeto?:", clon is aseg)

        # 4️⃣ RESUMEN FINAL
        print("\n========== TEST FINALIZADO ==========")
        print(f"Pólizas en aseguradora original: {len(aseg.obtenerSeguros())}")
        print(f"Pólizas en clon: {len(clon.obtenerSeguros())}")
        print(f"Costo total final: {aseg.costoTotal()}")

if __name__ == "__main__":
    TesterAseguradora.test()
