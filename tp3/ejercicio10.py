estudiantes = [
    {"nombre_apellido": "Ana Pérez", "legajo": 1001, "nota_parcial1": 70, "nota_parcial2": 80, "nota_final": 90},
    {"nombre_apellido": "Luis Gómez", "legajo": 1002, "nota_parcial1": 50, "nota_parcial2": 60, "nota_final": 40},
    {"nombre_apellido": "María López", "legajo": 1003, "nota_parcial1": 90, "nota_parcial2": 80, "nota_final": 100},
]

nombres = [estudiante["nombre_apellido"] for estudiante in estudiantes]

mayor_70 = [estudiante["nombre_apellido"] for estudiante in estudiantes if estudiante["nota_parcial1"] >= 70 and estudiante["nota_parcial2"] >= 70 and estudiante["nota_final"] >= 70]

menor_60 = [estudiante["nombre_apellido"] for estudiante in estudiantes if estudiante["nota_parcial1"] <= 60 or estudiante["nota_parcial2"] <= 60 or estudiante["nota_final"] <= 60]

print(nombres)
print(mayor_70)
print(menor_60)