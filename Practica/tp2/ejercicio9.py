archivo_alumnos = open("tp2/archivos/alumnos.txt","r")
archivo_datosAlumnos = open("tp2/archivos/datosAlumnos.txt","r")
archivo_promocion = open("tp2/archivos/promocion.txt","w")

def OrdenarLegajo(notas):
    for i in range(len(notas) - 1):
        for j in range(len(notas) - 1 - i):
            if(notas[j]["legajo"] > notas[j + 1]["legajo"]):
                aux = notas[j]
                notas[j] = notas[j + 1]
                notas[j + 1] = aux
    return notas

def ExtraerNotas():
    notas = []
    
    for linea in archivo_alumnos:
        infoNotas = linea.strip().split(";")
        
        notasAlumnos = ({
            "legajo": int(infoNotas[0]),
            "oral": int(infoNotas[1]),
            "escrito": int(infoNotas[2]),
            "tps": int(infoNotas[3])
        })
        
        notas.append(notasAlumnos)
    
    OrdenarLegajo(notas)
    return notas

def ExtraerAlumnos():
    alumnos = []
    
    for linea in archivo_datosAlumnos:
        infoAlumnos = linea.strip().split(";")
        
        datosAlumno = ({
            "legajo": int(infoAlumnos[0]),
            "apellido": infoAlumnos[1],
            "nombre": infoAlumnos[2]
        })
        
        alumnos.append(datosAlumno)
    
    OrdenarLegajo(alumnos)
    return alumnos

def OrdenarPorApellido(promocionados):
    for i in range(len(promocionados) - 1):
        for j in range(len(promocionados) - 1 - i):
            if(promocionados[j]["apellido"] > promocionados[j + 1]["apellido"]):
                aux = promocionados[j]
                promocionados[j] = promocionados[j + 1]
                promocionados[j + 1] = aux
    return promocionados

notas = ExtraerNotas()
alumnos = ExtraerAlumnos()
alumnosPromocionados = []

for i in range(len(alumnos)):
    promedio = (notas[i]["oral"] + notas[i]["escrito"] + notas[i]["tps"]) / 3
    
    if(promedio >= 7):
        alumnosPromocionados.append(alumnos[i])

OrdenarPorApellido(alumnosPromocionados)

archivo_promocion.write("Alumnos Promocionados\n")
for i in range(len(alumnosPromocionados)):
    archivo_promocion.write(f"{alumnosPromocionados[i]["apellido"]}, {alumnosPromocionados[i]["nombre"]} ({alumnosPromocionados[i]["legajo"]})\n")