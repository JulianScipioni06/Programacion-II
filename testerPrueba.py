from prueba import CuentaCorriente

class TestCuentaCorriente:
    # validamos el funcionamiento simulando el uso de la clase CuentaCorriente
    @staticmethod
    def test():
        cuenta_1 = CuentaCorriente(1, 1000)
        cuenta_2 = CuentaCorriente(2)
        cuenta_1.depositar(100)
        cuenta_2.depositar(100)
        print(f"Saldo cuenta 1: {cuenta_1.obtenerSaldo()}") # 1100
        print(f"Saldo cuenta 2: {cuenta_2.obtenerSaldo()}") # 100
        if cuenta_1.extraer(500):
            print(f"Extracción exitosa. Saldo cuenta 1: {cuenta_1.obtenerSaldo()}")
        else:
            print(f"No se pudo extraer 500 de cuenta_1. Saldo cuenta 1: {cuenta_1.obtenerSaldo()}")
        if cuenta_2.extraer(900):
            print(f"Extracción exitosa. Saldo cuenta 2: {cuenta_2.obtenerSaldo()}")
        else:
            print(f"No se pudo extraer 900 de cuenta_2. Saldo cuenta 2: {cuenta_2.obtenerSaldo()}")
        if cuenta_1.extraer(300):
            print(f"Extracción exitosa. Saldo cuenta 1: {cuenta_1.obtenerSaldo()}")
        else:
            print(f"No se pudo extraer 300 de cuenta_1. Saldo cuenta 1: {cuenta_1.obtenerSaldo()}")
        if cuenta_2.extraer(300):
            print(f"Extracción exitosa. Saldo cuenta 2: {cuenta_2.obtenerSaldo()}")
        else:
            print(f"No se pudo extraer 300 de cuenta_2. Saldo cuenta 2: {cuenta_2.obtenerSaldo()}")
        
        cuenta_1.depositar(500)
        cuenta_2.depositar(500)
        print(f"Saldo cuenta 1: {cuenta_1.obtenerSaldo()}") # 800
        print(f"Saldo cuenta 2: {cuenta_2.obtenerSaldo()}") # -300

if __name__ == "__main__":
    TestCuentaCorriente.test()


def procedimiento(param1, param2=[]): # Mala práctica
    pass

def procedimiento(param1, param2=None): # Mejor práctica
    if param2 is None:
        param2=[]
        pass