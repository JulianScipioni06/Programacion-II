from libro import Libro
import json

class TesterLibro:
    @staticmethod
    def test():
        with open("libros.json","r",encoding="utf-8") as archivo_json:
            datos = json.load(archivo_json)
        
        libros_objetos = []
        
        for dicc_libro in datos:
            # Convertimos cada diccionario en un string JSON
            json_libro = Libro.from_diccionario(json.dumps(dicc_libro))
            
            # Llamamos a tu método de deserialización
            libro = Libro.from_diccionario(json_libro)
            libros_objetos.append(libro)
        
        print("\n=== LISTA COMPLETA DE LIBROS ===")
        for libro in libros_objetos:
            print(libro)
        
        anio = int(input("Ingrese un anio para ver los libros: "))
        print(f"\n=== LIBROS PUBLICADOS EN {anio} ===")
        encontrados = [libro for libro in libros_objetos if libro.obtenerAnio() == anio]

        if not encontrados:
            print("No se encontraron libros para ese año.")
        else:
            for libro in encontrados:
                print(libro)

if __name__ == "__main__":
    TesterLibro.test()