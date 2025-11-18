class Automovil:
    __VELOCIDAD_MINIMA = 0

    def __init__(self, marca: str = "", modelo: str = "", anio: int = 0, velocidadMaxima: float = 0.0, velocidadActual: float = 0.0):
        # Año puede ser 0 al crear el objeto vacío, pero no negativo
        if not isinstance(anio, int) or anio < 0:
            raise ValueError("El año debe ser un Entero Positivo o Cero.")

        # Velocidad máxima puede ser 0 al inicio, pero no negativa
        if not isinstance(velocidadMaxima, float) or velocidadMaxima < 0:
            raise ValueError("La Velocidad Máxima debe ser un Número Positivo o Cero.")

        # Velocidad actual puede ser 0, pero no negativa
        if not isinstance(velocidadActual, float) or velocidadActual < 0:
            raise ValueError("La Velocidad Actual debe ser un Número Positivo o Cero.")

        self.__marca = marca
        self.__modelo = modelo
        self.__anio = anio
        self.__velocidadMaxima = velocidadMaxima
        self.__velocidadActual = velocidadActual

    # --- Comandos ---
    def EstablecerMarca(self, marca: str):
        self.__marca = marca

    def EstablecerModelo(self, modelo: str):
        self.__modelo = modelo

    def EstablecerAnio(self, anio: int):
        if not isinstance(anio, int) or anio <= 0:
            raise ValueError("El Año debe ser un Entero Positivo")
        self.__anio = anio

    def EstablecerVelocidadMaxima(self, velMaxima: float):
        if not isinstance(velMaxima, float) or velMaxima <= 0:
            raise ValueError("La Velocidad Máxima debe ser Positiva")
        self.__velocidadMaxima = velMaxima

    def EstablecerVelocidadActual(self, velActual: float):
        if not isinstance(velActual, float) or velActual < 0:
            raise ValueError("La Velocidad Actual debe ser Positiva o Cero")
        self.__velocidadActual = velActual

    def Acelerar(self, incrementoVelocidad: int):
        if not isinstance(incrementoVelocidad, int) or incrementoVelocidad <= 0:
            raise ValueError("El Incremento de Velocidad debe ser un Entero Positivo.")

        if self.__velocidadActual + incrementoVelocidad > self.__velocidadMaxima:
            self.__velocidadActual = self.__velocidadMaxima
            print(f"No se Puede Acelerar más Que {self.__velocidadMaxima} KM/H")
        else:
            self.__velocidadActual += incrementoVelocidad

    def Desacelerar(self, decrementoVelocidad: int):
        if not isinstance(decrementoVelocidad, int) or decrementoVelocidad <= 0:
            raise ValueError("El Decremento de Velocidad debe ser un Entero Positivo.")

        if self.__velocidadActual - decrementoVelocidad < Automovil.__VELOCIDAD_MINIMA:
            self.FrenarPorCompleto()
        else:
            self.__velocidadActual -= decrementoVelocidad

    def FrenarPorCompleto(self):
        self.__velocidadActual = 0

    # --- Consultas ---
    def ObtenerMarca(self) -> str:
        return self.__marca

    def ObtenerModelo(self) -> str:
        return self.__modelo

    def ObtenerAnio(self) -> int:
        return self.__anio

    def ObtenerVelocidadMaxima(self) -> float:
        return self.__velocidadMaxima

    def ObtenerVelocidadActual(self) -> float:
        return self.__velocidadActual

    def CalcularMinutosLlegada(self, distancia: float):
        if self.__velocidadActual == Automovil.__VELOCIDAD_MINIMA:
            print("El auto está detenido y no se puede calcular el tiempo para llegar!")
            return None
        else:
            tiempoLlegadaHoras = distancia / self.__velocidadActual
            return tiempoLlegadaHoras * 60
    
    def __str__(self)->str:
        return f"Datos del Auto: \n - Marca: {self.__marca} {self.__modelo}  {self.__anio} \n - Velocidad Maxima: {self.__velocidadMaxima} \n - Velocidad Actual: {self.__velocidadActual} \n"
