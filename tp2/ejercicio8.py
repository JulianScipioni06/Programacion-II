archivoStock = open("tp2/archivos/stock.txt","r")
archivoProductos = open("tp2/archivos/productos.txt","r")
archivoCompras = open("tp2/archivos/compras.txt","w")

def OrdenarProductos(productos):
    for i in range(len(productos) - 1):
        for j in range(len(productos) - 1 - i):
            if(productos[j]["codigo"] > productos[j + 1]["codigo"]):
                aux = productos[j]
                productos[j] = productos[j + 1]
                productos[j + 1] = aux
    return productos

def ControlarStock(stocks,productos):
    for i in range(len(stocks)):
        if stocks[i]["stockMinimo"] > stocks[i]["stockReal"]:
            archivoCompras.write(f"{productos[i]["nombre"]}({stocks[i]["codigo"]})")
            archivoCompras.write(f"Stock Actual: {stocks[i]["stockReal"]}/{stocks[i]["stockMinimo"]}")
    print("Lista de Compras realizada con exito!!!")

productos = []

for linea in archivoProductos:
    infoProducto = linea.split(";")

    producto = ({
        "codigo": int(infoProducto[0]),
        "nombre": infoProducto[1],
        "precio": int(infoProducto[2])
    })
    
    productos.append(producto)

stocks = []

for linea in archivoStock:
    infoStock = linea.split(";")

    stock = ({
        "codigo": int(infoStock[0]),
        "stockMinimo": int(infoStock[1]),
        "stockReal": int(infoStock[2])
    })
    
    stocks.append(stock)

ControlarStock(stocks,productos)

archivoProductos.close()
archivoStock.close()