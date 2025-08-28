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

def PedirNota(mensaje:str) -> int: 
    bandera = True
    while bandera:
        try:
            numero = int(input(mensaje))
            if numero > 0 and numero <= 100:
                bandera = False
            else:
                print("Error: El numero debe ser positivo.")
        except ValueError:
            print("ERROR! Ingrese un numero entero positivo: ")
    return numero

alumnos = []

cantAlumnos = PedirEntero("Cantidad de Alumnos a Ingresar: ")

for i in range(cantAlumnos):
    print("Datos del Alumno")
    nombre = input("Ingrese nombre: ")
    nota = PedirNota(f"Nota de {nombre}: ")
    print()
    
    alumnos.append({
        "nombre": nombre,
        "nota": nota
    })

print("Resultados del Parcial")
for alumno in alumnos:
    print(f"Alumno: {alumno["nombre"]} / Nota: {alumno["nota"]} /Resultado: {"Aprobado" if alumno["nota"] >= 40 else "Desaprobado"}")
