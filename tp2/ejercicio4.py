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


numero = PedirEntero("numero: ")
print(f"Numero Ingresado: {numero}")
digitos = []

while numero != 0:
    digito = numero % 10
    digitos.append(digito)
    numero = numero // 10

digitoGrande = digitos[0]
posicion = 0
for i in range(0,len(digitos)):
    if digitos[i] > digitoGrande:
        digitoGrande = digitos[i]
        posicion = i

print(f"Digitos que lo Componen: {digitos}")
print(f"El digito mas grande es {digitoGrande} esta en la posicion {posicion} de la lista.")