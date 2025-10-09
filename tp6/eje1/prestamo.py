from fecha import Fecha
from socio import Socio
from libro import Libro

class Prestamo:
    #Constructor
    
    def __init__(self, libro:Libro, fechaPrestamo:Fecha, dias:int, socio:Socio, fechaDevolucion:Fecha = None):
        """
        Inicializa un nuevo Objeto Prestamo.
        Parametros:
        - libro = libro sacado a prestamo
        - fechaPrestamo = Fecha en la que se realizo el prestamo
        - dias = Cantidad de Dias que se presta el libro
        - socio = Socio el cual retiro el libro
        - fechaDevolucion = Fecha en la que se devolvio el libro
        """
        if not isinstance(libro, Libro):
            raise TypeError("Tipo de Dato Invalido. Tipo Requerido: Libro")
        if not isinstance(fechaPrestamo, Fecha):
            raise TypeError("Tipo de Dato Invalido. Tipo Requerido: Fecha")
        if not isinstance(dias,int) or dias <= 0:
            raise ValueError("cantDias debe ser un Entero mayor que 0")
        if not isinstance(socio, Socio):
            raise TypeError("Tipo de Dato Invalido. Tipo Requerido: Socio")
        
        self.__libro = libro
        self.__fechaPrestamo = fechaPrestamo
        self.__dias = dias
        self.__socio = socio
        self.__fechaDevolucion = fechaDevolucion
    
    #Comandos
    def establecerFechaDevolucion(self, fechaDev:Fecha):
        """Establece la fecha de devolución y aplica penalización si corresponde."""
        if not isinstance(fechaDev, Fecha):
            raise TypeError("La fecha de devolución debe ser de tipo 'Fecha'")

        self.__fechaDevolucion = fechaDev
        
        # Calcular fecha límite de devolución
        fechaLimite = self.__fechaPrestamo.sumaDias(self.__dias)
        
        if fechaLimite.esAnterior(self.__fechaDevolucion):
            fechaPenalHasta = self.penalizacion()
            self.__socio.establecerFechaPenalizacion(fechaPenalHasta)
    
    #Consultas
    def obtenerLibro(self) -> Libro:
        """Devuelve el Libro por el cual se hace el prestamo."""
        return self.__libro
    
    def obtenerFechaPrestamo(self) -> Fecha:
        """Devuelve la fecha del prestamo."""
        return self.__fechaPrestamo
    
    def obtenerFechaDevolucion(self) -> Fecha:
        """Devuelve la fecha del prestamo."""
        return self.__fechaDevolucion
    
    def estaAtrasado(self, fecha:Fecha) -> bool:
        """recibe como parámetro la fecha actual y retorna verdadero si el libro no se devolvió y ya debería haberse devuelto de acuerdo a la fecha de préstamo y la cantidad de días."""
        if self.__fechaDevolucion is not None:
            return False
        
        fechaLimite = self.__fechaPrestamo.sumaDias(self.__dias)
        
        return fechaLimite.esAnterior(fecha)
    
    def penalizacion(self) -> Fecha:
        """Calcula y devuelve la fecha hasta la que el socio estará penalizado."""
        # Calcular días de atraso
        diasAtraso = self.__fechaPrestamo.diasHasta(self.__fechaDevolucion) - self.__dias

        if diasAtraso < 7:
            diasPenal = 3
        elif diasAtraso < 21:
            diasPenal = 5
        else:
            diasPenal = 10

        # Si el libro es categoría A, se duplican los días
        if self.__libro.obtenerCategoria() == 'A':
            diasPenal *= 2

        # Fecha final = fecha de devolución + días de penalización
        return self.__fechaDevolucion.sumaDias(diasPenal)
    
    def __str__(self):
        return f"DATOS DEL PRESTAMO: \n Libro: {self.__libro.obtenerNombre()} \n Fecha de Prestamo: {self.__fechaPrestamo} \n Dias de Prestamo: {self.__dias} \n Socio: {self.__socio.obtenerNombre()} \n Fecha de Devolucion: {self.__fechaDevolucion}"
