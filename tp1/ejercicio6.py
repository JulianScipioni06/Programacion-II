# Realizar un programa que solicite al usuario un número entero positivo, y luego en pantalla muestre la secuencia de números desde el 1 hasta el número ingresado. 
# Ej: usuario ingresa 10, en pantalla se mostrará 1 2 3 4 5 6 7 8 9 10


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

tope = PedirEntero("Ingrese un Numero: ")
for i in range(1, tope + 1):
    print(i, end=" ")