alumnos = []

cantAlumnos = int(input("Cuantos alumnos vas a cargar? "))

for i in range(cantAlumnos):
    nombre = input("Ingrese nombre del alumno: ")
    nota = float(input(f"Ingrese nota de {nombre}: "))
    print()
    
    alumnos.append([nombre,nota])

resultados = []

# for i in range(0,len(alumnos)):
#     if alumnos[0,i] >= 40:
#         resultados[i] = "Aprobado"
#     else:
#         resultados[i] = "Desaprobado"

print(alumnos[0])
print(alumnos[nombre])

