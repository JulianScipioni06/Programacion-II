# Se desea realizar una aplicación que solicite al usuario un caracter y un número natural N, 
# y que la aplicación muestre en pantalla dicho carácter repetido N veces consecutivas. 
# Ej: Ingrese un caracter: + 
# Ingrese la cantidad de repeticiones: 15 
# +++++++++++++++

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

def PedirCaracter() -> str:
    caracter = input("Ingrese caracter a imprimir: ")
    return caracter

caracter = PedirCaracter()
repeticiones = PedirEntero("Ingrese la cantidad de repeticiones: ")

for i in range (0,repeticiones):
    print(caracter,end="")