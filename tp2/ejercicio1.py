def InvertirCadena(cadena:str):
    invertida = ""
    for letra in cadena:
        invertida = letra + invertida
    return invertida

def determinarPalindromo(cadena:str, invertida:str):
    if cadena.lower() == invertida.lower():
        print(f"Palabra Invertida: {invertida}")
        print("La palabra es Palindromo!")
    else:
        print(f"Palabra Invertida: {invertida}")
        print("La palabra NO es palindromo!")

cadena = input("Ingrese una palabra: ")

cadenaInvertida = InvertirCadena(cadena)

determinarPalindromo(cadena,cadenaInvertida)

