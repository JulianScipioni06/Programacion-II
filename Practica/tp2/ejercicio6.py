archivo = open("tp2/archivos/distancias.txt", 'r')

distanciaTotal = 0
cantViajes = 0
for linea in archivo:
    distancia = float(linea)
    distanciaTotal += distancia
    cantViajes += 1

archivo.seek(0)
promedio = distanciaTotal / cantViajes
distanciasMayores = []

for linea in archivo:
    distancia = float(linea)
    if distancia >= promedio:
        distanciasMayores.append(distancia)

archivo.close()

print(f"La distancia promedio de los viajes es {promedio} y los viajes con distancia mayor son: {distanciasMayores}")