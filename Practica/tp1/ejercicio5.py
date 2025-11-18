#Dada una cadena de texto ingresada por consola, decir cuántos “espacios” contiene.

cadena = input("Ingrese una de cadena texto: ")

cantEspacios = 0

# for letra in cadena:
#     if(letra == " "):
#         cantEspacios += 1

for i in range(0,len(cadena)):
    if(cadena[i] == " "):
        cantEspacios += 1

print(f"El texto tiene {cantEspacios} espacios.")