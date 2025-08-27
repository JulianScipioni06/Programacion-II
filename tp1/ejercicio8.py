# Desarrollar un programa que permita al usuario indicar cuantos valores quiere ingresar, 
# luego que permita la carga de los valores por teclado y nos muestre posteriormente la suma de los valores ingresados y su promedio.

def PedirEntero(mensaje:str) -> int: 
    bandera = True
    while bandera:
        try:
            numero = int(input(mensaje))
            if numero > 0:
                bandera = False
            else:
                print("Error: El numero debe ser positivo.")
        except ValueError:
            print("ERROR! Ingrese un numero entero positivo: ")
    return numero

def PedirNumero(mensaje:str) -> float:
    bandera = True
    while bandera:
        try:
            numero = float(input(mensaje))
            bandera = False
        except ValueError:
            print("Error! Debe ingresar un numero valido: ")
    return numero

cantValores = PedirEntero("Cuantos valores queres sumar: ")
suma = 0
promedio = 0

for i in range(0, cantValores):
    suma += PedirNumero(f"Valor {i + 1}: ")

print(f"Suma Total de Valores = {suma}")
print(f"Promedio Valores Sumados = {suma/cantValores}")