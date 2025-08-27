# Implemente un programa que a partir del ancho, alto y largo de una habitación rectangular calcule cuántos litros de pintura se necesitan para pintarla. 
# Suponiendo que 1 litro de pintura sirve para 10m cuadrados y que la habitación tiene sólo una puerta de 0,80 de ancho por 2 mts de alto.
ancho = float(input("Ingrese ancho de la Habitacion: "));
alto = float(input("Ingrese alto de la Habitacion: "));
largo = float(input("Ingrese largo de la Habitacion: "));

puerta = 0.80 * 2;

superficiePintar = 2* (ancho * alto) + 2 * (largo * alto);
superficieTotal = superficiePintar - puerta

litros = superficieTotal / 10;
litrosEnteros = superficieTotal // 10;

if(litros >= litrosEnteros):
    litrosTotales = litrosEnteros + 1;
else:
    litrosTotales = litrosEnteros;

print(f"Superficie a Pintar: {superficieTotal} m2");
print(f"Litros Necesarios: {litrosTotales} litros");



