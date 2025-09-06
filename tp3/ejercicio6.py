personas = {
    "Ana": 25,
    "Juan": 32,
    "Maria": 19,
    "Pedro": 45,
    "Sofia": 28,
    "Luis": 36,
    "Elena": 22
}

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

def generar_lista(personas:dict,edadMinima:int):
    nueva_lista = [nombre for nombre,edad in personas.items() if edad >= edadMinima]
    
    return nueva_lista

edadMinima = PedirEntero("Ingrese edad minima requerida: ")
personas_mayores = generar_lista(personas,edadMinima)
print(personas_mayores)