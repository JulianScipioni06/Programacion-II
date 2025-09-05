def NombresLargos(lista,longitud):
    lista = [nombre for nombre in lista if len(nombre) >= longitud]
    return lista

nombres = ["Matias", "Manuel", "Bautista", "Franco", "Julian", "mia", "mario"]
longitud = int(input("Ingrese longitud minima de nombre: "))

nombres_filtrados = NombresLargos(nombres, longitud)
print(nombres_filtrados)