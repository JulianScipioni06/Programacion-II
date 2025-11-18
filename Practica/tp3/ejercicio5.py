numeros = [1,2,3,4,5,6,7,8,9,10,11,15,17,20]

def esPrimo(numero):
    divisores = [divisor for divisor in range(2,numero) if numero % divisor == 0]
    
    if not divisores:
        return True
    else:
        return False

for num in numeros:
    if esPrimo(num):
        print(f"{num} Es primo.")
    else:
        print(f"{num} NO Es primo.")