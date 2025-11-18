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

# def OrdenarNotas(notas):
#     for i in range(len(notas) + 1): #Recorre Toda la lista
#         for j in range(0,len(notas) - 1 - i):
#             if notas[j] > notas[j + 1]:
#                 aux = notas[j]
#                 notas[j] = notas[j + 1]
#                 notas[j + 1] = aux

cantidad = PedirEntero("Cuantas notas queres ingresar: ")
notas = []

for i in range(0, cantidad):
    nota = PedirEntero("Ingrese nota: ")
    notas.append(nota)

mejorNota = notas[0]
for i in notas:
    if notas[i] >= mejorNota:
        mejorNota = notas[i]
        posicion = i

print(f"Mejor Nota: {mejorNota} - Posicion del Arreglo: {posicion}")