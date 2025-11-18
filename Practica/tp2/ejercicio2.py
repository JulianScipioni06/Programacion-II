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

def EsBisiesto(anio:int):
    if (anio % 4 == 0) and not(anio % 100 == 0):
        print(f"El año {anio} es Bisiesto!")
    else:
        print(f"El año {anio} NO es Bisiesto!")

def ValidarFecha(dia:int, mes:int, anio:int):
    if (anio % 4 == 0) and not(anio % 100 == 0):
        if mes == 2 and dia >= 1 and dia <= 29:
            print(f"Fecha Ingresada VALIDA: {dia}/{mes}/{anio}")
        else:
            print(f"Fecha Ingresada INVALIDA: {dia}/{mes}/{anio}")
    elif (dia >= 1 and dia <= 31) and (mes >= 1 and mes <= 1):
        print(f"Fecha Ingresada VALIDA: {dia}/{mes}/{anio}")
    else:
        print(f"Fecha Ingresada INVALIDA: {dia}/{mes}/{anio}")


print("Ingrese una fecha")
dia = PedirEntero("Ingrese el dia: ")
mes = PedirEntero("Ingrese el mes: ")
anio = PedirEntero("Ingrese el Año: ")

EsBisiesto(anio)
ValidarFecha(dia,mes,anio)