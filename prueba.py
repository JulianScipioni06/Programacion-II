
class CuentaCorriente:
    def __init__(self, numero_cuenta, saldo_inicial=0):
        #Validar el Numero de Cuenta
        if not isinstance(numero_cuenta, int):
            raise("El Nro de Cuenta debe ser un entero.")
        if numero_cuenta <= 0:
            raise("El Nro de Cuenta debe ser 0 o positivo")
        
        #Validar el Saldo Inicial
        if not isinstance(saldo_inicial, (int, float)):
            raise TypeError("El saldo debe ser numérico")
        if saldo_inicial < 0:
            raise ValueError("El saldo inicial no puede ser negativo")
        
        #Si paso todas las validaciones:
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo_inicial

c1 = CuentaCorriente(111, 7500)
c2 = CuentaCorriente(112, 5000)
c3 = c1.cuentaMayorSaldo(c2)
c4 = c1
c5 = CuentaCorriente(111, 7500)

print(c1 == c3)  # False → distintas referencias
print(c1 == c4)  # True  → misma referencia
print(c1 == c5)  # False → mismo estado pero distintas referencias

if c1.obtenerCodigo() == c3.obtenerCodigo() and c1.obtenerSaldo() == c3.obtenerSaldo():
    print("El estado interno es igual")