archivo = open("tp3/archivos/datos.txt","r")

lineas_archivo = [linea for linea in archivo]
print(lineas_archivo)

archivo.close()