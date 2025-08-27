# Se desea realizar una aplicación que solicite al usuario tres números enteros positivos (A, B, y X), 
# y que muestre por pantalla todos los múltiplos de X que estén entre A y B inclusive.

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

numA = PedirEntero("Ingrese numero A: ")
numB = PedirEntero("Ingrese numero B: ")
numX = PedirEntero("Ingrese numero X: ")
multiplosX = []

for i in range(numA,numB + 1):
    if i % numX == 0:
        multiplosX.append(i)

print(f"Los numeros entre {numA} y {numB} multiplo de {numX} son:")
print(multiplosX)
