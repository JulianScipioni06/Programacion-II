# Escriba un programa que para un texto ingresado nos muestre cual es la palabra más larga dentro de ese texto y cuántas letras tiene.

texto = input("Ingrese un texto: ")

palabras = texto.split(" ")

masLarga = palabras[0]
for palabra in palabras:
    if len(palabra) >= len(masLarga):
        masLarga = palabra

print(f"La palabra mas larga es '{masLarga}'.")
print(f"Tiene {len(masLarga)} letras")