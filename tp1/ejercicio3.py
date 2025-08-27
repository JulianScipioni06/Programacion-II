# Extienda el programa anterior para permitir múltiple cantidad de “manos” de pintura.
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

