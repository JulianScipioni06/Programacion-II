def ExponerLista(lista):
    lista = [numero ** 2 for numero in numeros]
    return lista

numeros = [2,7,5,9,10]

nums_cuadrados = ExponerLista(numeros)
print(nums_cuadrados)
