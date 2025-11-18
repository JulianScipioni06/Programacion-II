archivosProductos = open("tp2/archivos/productos.txt","r")

def PedirEntero(mensaje:str) -> int: 
    bandera = True
    while bandera:
        try:
            numero = int(input(mensaje))
            if numero > 0:
                bandera = False
            else:
                print("Error: El numero debe ser positivo.")
        except ValueError:
            print("ERROR! Ingrese un numero entero positivo: ")
    return numero

def OrdenarProductos(productos):
    for i in range(len(productos) - 1):
        for j in range(len(productos) - 1 - i):
            if(productos[j]["codigo"] > productos[j + 1]["codigo"]):
                aux = productos[j]
                productos[j] = productos[j + 1]
                productos[j + 1] = aux
    return productos

def BusquedaProducto(productos,codigoBuscado):
    indiceEncontrado = -1
    inicio = 0
    final = len(productos) - 1
    
    while(inicio <= final and indiceEncontrado == -1):
        medio = (inicio + final) // 2
        if(codigoBuscado == productos[medio]["codigo"]):
            indiceEncontrado = medio
        elif (codigoBuscado > productos[medio]["codigo"]):
            inicio = medio + 1
        else:
            final = medio - 1
    
    return indiceEncontrado

def BuscarProductos(productos):
    OrdenarProductos(productos)
    codigoBuscado = PedirEntero("Ingrese Codigo del Producto: ")
    
    indice = BusquedaProducto(productos,codigoBuscado)
    
    if(indice == -1):
        print("Codigo NO encontrado!")
    else:
        print("Producto Encontrado!")
        print(f"Nombre: {productos[indice]['nombre']}")
        print(f"Precio: {productos[indice]['precio']}")


productos = []
for linea in archivosProductos:
    infoProducto = linea.split(";")

    producto = ({
        "codigo": int(infoProducto[0]),
        "nombre": infoProducto[1],
        "precio": float(infoProducto[2])
    })
    
    productos.append(producto)

BuscarProductos(productos)
archivosProductos.close()