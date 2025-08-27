# Escriba un programa que, dada una oración ingresada muestre por pantalla:
# a.El número total de caracteres en la oración
# b.La cantidad total de letras (consonantes y vocales, sin signos de puntuación)
# c.La cantidad de palabras separadas por uno o más espacios
# En este ejercicio, para simplificar, asumiremos que los posibles caracteres de entrada son letras, espacios, dígitos, signos de puntuación, signos de interrogación y de exclamación.
# Investigar si hay funciones de strings que nos faciliten la resolución [len(), .isalpha(), .split() , etc.]

def ContarLetras(oracion:str):
    caracteresEspeciales = 0
    for letra in oracion:
        if letra == " ":
            caracteresEspeciales += 1
        elif letra == "!" or letra == "¡":
            caracteresEspeciales += 1
        elif letra == "?" or letra == "¿":
            caracteresEspeciales += 1
        elif letra == "." or letra == ",":
            caracteresEspeciales += 1
    cantLetras = cantCaracteres - caracteresEspeciales
    return cantLetras

def ContarPalabras(oracion:str):
    palabras = oracion.split(" ")
    cantPalabras = len(palabras)
    return cantPalabras

oracion = input("Ingrese una oracion: ")

cantCaracteres = len(oracion)
letrasTotales = ContarLetras(oracion)
palabrasTotales = ContarPalabras(oracion)

print(f"La oracion tiene: {cantCaracteres} caracteres.")
print(f"De los cuales {letrasTotales} son letras.")
print(f"La oracion se compone de {palabrasTotales} palabras")




