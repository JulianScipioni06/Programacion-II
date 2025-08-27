# Escriba un programa que dado un texto ingresado por el usuario cuente la cantidad total de vocales que aparecen y lo muestre por pantalla.

a = 0
e = 0
i = 0
o = 0
u = 0
vocales = [a,e,i,o,u]

texto = input("Ingrese un texto: ")

for letra in texto:
    if letra.lower() == "a":
        a += 1
    elif letra.lower() == "e":
        e += 1
    elif letra.lower() == "i":
        i += 1
    elif letra.lower() == "o":
        o += 1
    elif letra.lower() == "u":
        u += 1

print(f"a: {a} veces.")
print(f"e: {e} veces.")
print(f"i: {i} veces.")
print(f"o: {o} veces.")
print(f"u: {u} veces.")