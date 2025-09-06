duplicados = [1, 2, 2, 3, 4, 4, 5, 5, 5]

unicos = []
[unicos.append(valor) for valor in duplicados if valor not in unicos]
print(unicos)