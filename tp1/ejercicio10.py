# Escriba un programa que permita al usuario ingresar las medidas de 2 lados de un rectángulo, 
# y que luego mediante la impresión repetida de un caracter (ej: *) lo dibuje en la pantalla. 
# Para este ejercicio tomaremos un máximo de 40 para el lado más largo, 
# con el fin de evitar problemas de visualización en la consola. Verificar en los datos de entrada que se cumpla este requisito.

def PedirEntero(mensaje:str) -> int: 
    bandera = True
    while bandera:
        try:
            numero = int(input(mensaje))
            if numero > 0 and numero <= 40:
                bandera = False
            else:
                print("Error: El numero debe ser positivo.")
        except ValueError:
            print("ERROR! Ingrese un numero entero positivo: ")
    return numero

lado1 = PedirEntero("Ingrese medida del lado 1: ")
lado2 = PedirEntero("Ingrese medida del lado 2: ")

for fila in range(1, lado1 + 1):
    for columna in range(1, lado2 + 1):
        print("*", end="")
    print()