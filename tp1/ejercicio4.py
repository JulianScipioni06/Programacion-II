#Pedir 3 números enteros e implementar un algoritmo para determinar cuál es el mayor de los 3 y mostrar un mensaje por pantalla.
num1 = int(input("Ingrese numero 1(Entero): "));
num2 = int(input("Ingrese numero 2(Entero): "));
num3 = int(input("Ingrese numero 3(Entero): "));

if(num1 > num2 and num1 > num3):
    if(num1 == num2):
        print(f"Numero 1({num1}) y Numero 2({num2}) son iguales. Ambos son mayores que Numero 3({num3})");
    elif(num1 == num3):
        print(f"Numero 1({num1}) y Numero 3({num3}) son iguales. Ambos son mayores que Numero 2({num2})");
    else:
        print(f"Numero 1({num1}) es el mayor de los 3.");
elif(num2 > num3):
    if(num2 == num3):
        print(f"Numero 2({num2}) y Numero 3({num3}) son iguales. Ambos son mayores que Numero 1({num1})");
    else:
        print(f"Numero 2({num2}) es el mayor de los 3.");
else:
    print(f"Numero 3({num3}) es el mayor de los 3.");