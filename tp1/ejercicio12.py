# Escriba un programa que permita el ingreso de números enteros positivos, 
# finalizando el ingreso con 0, y luego indique si la secuencia estaba ordenada de menor a mayor.

def PedirEntero(mensaje: str) -> int: 
    while True:
        try:
            numero = int(input(mensaje))
            if numero >= 0:
                return numero
            else:
                print("Error: El número debe ser positivo.")
        except ValueError:
            print("ERROR! Ingrese un número entero positivo.")

# Inicia la lógica del programa principal
primer_numero = PedirEntero("Ingrese un número (0 para finalizar): ")

# Caso especial: Si el primer número ingresado es 0
if primer_numero == 0:
    print("La secuencia está vacía.")
else:
    # La lógica para la secuencia ordenada
    anterior = primer_numero
    ordenada = True

    while True:
        numero = PedirEntero("Ingrese otro número (0 para finalizar): ")
        if numero == 0:  
            break
        elif numero < anterior:
            ordenada = False
        anterior = numero

    if ordenada:
        print("La secuencia cargada está ordenada de menor a mayor.")
    else:
        print("La secuencia cargada NO está ordenada de menor a mayor.")


