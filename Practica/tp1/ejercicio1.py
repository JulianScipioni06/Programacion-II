# Realizar un programa que pida los tres lados de un triángulo e indique el tipo de triángulo que es según sus lados: 
#     Equilátero (tres lados iguales), 
#     Isósceles (dos lados iguales),
#     Escaleno (tres lados distintos).

lado1 = float(input("Ingrese lado 1 del triangulo: "));
lado2 = float(input("Ingrese lado 2 del triangulo: "));
lado3 = float(input("Ingrese lado 3 del triangulo: "));

if (lado1 == lado2 and lado1 == lado3 and lado2 == lado3):
    print("El triangulo tiene 3 lados iguales. Es Equilatero!")
elif((lado1 == lado2 and lado1 != lado3) or (lado2 == lado3 and lado2 != lado3) or (lado3 == lado1 and lado3 or lado1)):
    print("El triangulo tiene 2 lados iguales. Es Isosceles!")
else:
    print("El triangulo tiene 3 lados distintos. Es Escaleno!");