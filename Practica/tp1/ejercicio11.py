# Escriba un programa que permita el ingreso de números enteros positivos para calcular su promedio, 
# el ingreso finaliza cuando el usuario ingresa un número negativo. 
# Luego mostrar el promedio y la cantidad de valores que se ingresaron. 
# Ej: “El promedio es ….. con un total de …. ingresos.”

def PedirNumero(mensaje:str) -> float:
    bandera = True
    while bandera:
        try:
            numero = int(input(mensaje))
            bandera = False
        except ValueError:
            print("Error! Debe ingresar un numero valido: ")
    return numero

numero = 0
suma = 0
cantNumeros = 0

while numero >= 0:
    numero = PedirNumero("Ingrese un numero: ")
    if numero >= 0:
        suma += numero
        cantNumeros += 1

print()
print(f"Promedio Calculado = {suma / cantNumeros}")
print(f"Cantidad de Numeros Sumados = {cantNumeros}")