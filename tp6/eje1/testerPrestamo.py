from fecha import Fecha
from socio import Socio
from libro import Libro
from prestamo import Prestamo

class TesterPrestamo:
    @staticmethod
    def test():
        divisor = "-" * 70
        print(divisor)
        print("📚 TESTER DE LA CLASE PRÉSTAMO 📚")
        print(divisor)

        # 🔹 Casos fijos
        print("1️⃣ Creación de objetos fijos (Libro, Socio y Préstamo)")
        libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", "Sudamericana", "A")
        socio1 = Socio("Lucas Goodman", Fecha(10, 5, 2002))
        fecha_prestamo = Fecha(1, 10, 2025)
        prestamo1 = Prestamo(libro1, fecha_prestamo, 7, socio1)
        print("Libro:", libro1)
        print("Socio:", socio1)
        print("Préstamo:", prestamo1)
        print(divisor)

        # 🔹 Probar devolución dentro del plazo
        print("2️⃣ Devolución a tiempo (no debe penalizar)")
        fechaDev = Fecha(6, 10, 2025)
        prestamo1.establecerFechaDevolucion(fechaDev)
        print("Fecha de devolución establecida:", prestamo1.obtenerFechaDevolucion())
        print("Fecha de penalización del socio:", socio1.obtenerFechaPenalizacion())
        print("¿Socio habilitado al 10/10/2025? →", socio1.estaHabilitado(Fecha(10, 10, 2025)))
        print(divisor)

        # 🔹 Probar devolución fuera de plazo
        print("3️⃣ Devolución atrasada (debe generar penalización)")
        libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "Sudamericana", "B")
        socio2 = Socio("María Pérez", Fecha(12, 8, 1995))
        prestamo2 = Prestamo(libro2, Fecha(1, 10, 2025), 7, socio2)
        prestamo2.establecerFechaDevolucion(Fecha(15, 10, 2025))  # 7 días tarde
        print("Libro:", libro2.obtenerNombre())
        print("Fecha de devolución:", prestamo2.obtenerFechaDevolucion())
        print("Fecha de penalización asignada:", socio2.obtenerFechaPenalizacion())
        print("¿Socio habilitado al 20/10/2025? →", socio2.estaHabilitado(Fecha(20, 10, 2025)))
        print(divisor)

        # 🔹 Probar penalización con libro categoría A (se duplica)
        print("4️⃣ Devolución atrasada con libro categoría A (penalización doble)")
        libro3 = Libro("Python Avanzado", "Guido Van Rossum", "O'Reilly", "A")
        socio3 = Socio("Juan López", Fecha(1, 1, 1990))
        prestamo3 = Prestamo(libro3, Fecha(1, 10, 2025), 7, socio3)
        prestamo3.establecerFechaDevolucion(Fecha(25, 10, 2025))  # 17 días tarde
        print("Libro:", libro3.obtenerNombre())
        print("Fecha de devolución:", prestamo3.obtenerFechaDevolucion())
        print("Fecha de penalización asignada:", socio3.obtenerFechaPenalizacion())
        print("¿Socio habilitado al 10/11/2025? →", socio3.estaHabilitado(Fecha(10, 11, 2025)))
        print(divisor)

        # 🔹 Caso con datos ingresados por el usuario
        print("5️⃣ Caso con ingreso de datos manual:")
        nombre_libro = input("Ingrese el nombre del libro: ")
        autor_libro = input("Ingrese el autor: ")
        editorial_libro = input("Ingrese la editorial: ")
        categoria_libro = input("Ingrese la categoría (A/B/C): ").upper()
        libro_usr = Libro(nombre_libro, autor_libro, editorial_libro, categoria_libro)

        nombre_socio = input("Ingrese el nombre del socio: ")
        socio_usr = Socio(nombre_socio, Fecha(15, 6, 2000))
        fecha_prest_usr = Fecha(1, 10, 2025)

        dias_prest_usr = int(input("Ingrese la cantidad de días autorizados: "))
        prestamo_usr = Prestamo(libro_usr, fecha_prest_usr, dias_prest_usr, socio_usr)

        print("\nIngrese la fecha de devolución:")
        dia_dev = int(input("Día: "))
        mes_dev = int(input("Mes: "))
        anio_dev = int(input("Año: "))
        fecha_dev_usr = Fecha(dia_dev, mes_dev, anio_dev)
        prestamo_usr.establecerFechaDevolucion(fecha_dev_usr)

        print("\n📘 Resultados del préstamo ingresado por el usuario:")
        print(prestamo_usr)
        print("Fecha de penalización del socio:", socio_usr.obtenerFechaPenalizacion())
        print(divisor)

        print("✅ Todas las pruebas finalizadas correctamente.")
        print(divisor)


if __name__ == "__main__":
    TesterPrestamo.test()
