numeros = [1,2,3,4,5,6,7,8,9,10]

pares = [i for i in numeros if i % 2 == 0]
impares = [i for i in numeros if i % 2 != 0]

print(f"Lista de Numeros: {numeros}")
print(f"Pares: {pares}")
print(f"Impares: {impares}")