def pedir_palabras():
    palabra = input("Ingrese una palabra: ")
    palabras = []
    
    while palabra.lower() != "salir":
        palabras.append(palabra)
        print("Ingrese 'Salir' para frenar!")
        palabra = input("Ingrese una palabra: ")
    
    return palabras

def contar_vocales(palabras:list):
    vocales = ["a","e","i","o","u"]
    contVocales = 0
    for palabra in palabras:
        for letra in palabra:
            if letra in vocales:
                contVocales += 1
        print(f"La palabra '{palabra}' Tiene {contVocales} vocales.")


palabras = pedir_palabras()
print(contar_vocales(palabras))