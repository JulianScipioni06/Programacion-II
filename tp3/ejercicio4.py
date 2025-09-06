diccionario = {
    "abaco": "Instrumento para realizar cálculos.",
    "arbol": "Planta de tronco leñoso.",
    "calido": "Que produce calor.",
    "amistad": "Afecto personal puro y desinteresado.",
    "casa": "Edificio para habitar.",
    "bello": "Que tiene belleza.",
    "azul": "Color del cielo sin nubes.",
    "barco": "Construcción flotante que se desplaza en el agua."
}

dict_A = [palabra for palabra in diccionario if palabra[0].lower() == "c"]

for palabra in dict_A:
    print(f"{palabra}: {diccionario[palabra]}")
