class Color:
    #Atributo de Clase
    __VALOR_MAX = 255
    __VALOR_MIN = 0
    
    def __init__(self, rojo=255, verde=255, azul=255):
        """
        Inicializa un Color con el Rojo, Azul y Verde en 255.
        """
        self.__rojo = rojo
        self.__verde = verde
        self.__azul = azul
    
    #Comandos
    def variar(self, valor:int):
        """
        Modifica cada componente de color sumándole si es posible, un valor dado.
        Si al Sumarle el Valor supera el Maximo o el Minimo, se ajusta a los valores correspondientes.
        """
        if not isinstance(valor,int):
            raise TypeError("El valor debe ser un numero entero")
        
        self.variarRojo(valor)
        self.variarVerde(valor)
        self.variarAzul(valor)
    
    def variarRojo(self, valor:int):
        """
        Modifica la componente de rojo sumándole un valor dado.
        Si al Sumarle el Valor supera el Maximo o el Minimo, se ajusta a los valores correspondientes.
        """
        if not isinstance(valor,int):
            raise TypeError("El valor debe ser un numero entero")
        
        if self.__rojo + valor > 255:
            self.__rojo = Color.__VALOR_MAX
        elif self.__rojo + valor < 0:
            self.__rojo = Color.__VALOR_MIN
        else:
            self.__rojo += valor
    
    def variarVerde(self, valor:int):
        """
        Modifica la componente de verde sumándole un valor dado.
        Si al Sumarle el Valor supera el Maximo o el Minimo, se ajusta a los valores correspondientes.
        """
        if not isinstance(valor,int):
            raise TypeError("El valor debe ser un numero entero")
        
        if self.__verde + valor > 255:
            self.__verde = Color.__VALOR_MAX
        elif self.__verde + valor < 0:
            self.__verde = Color.__VALOR_MIN
        else:
            self.__verde += valor
    
    def variarAzul(self, valor:int):
        """
        Modifica la componente de azul sumándole un valor dado.
        Si al Sumarle el Valor supera el Maximo o el Minimo, se ajusta a los valores correspondientes.
        """
        if not isinstance(valor,int):
            raise TypeError("El valor debe ser un numero entero")
        
        if self.__azul + valor > 255:
            self.__azul = Color.__VALOR_MAX
        elif self.__azul + valor < 0:
            self.__azul = Color.__VALOR_MIN
        else:
            self.__azul += valor
    
    def establecerRojo(self, valor:int):
        """Establece el Color Rojo, en el valor recibido por parametro"""
        if not isinstance(valor,int) or valor < 0 or valor > 255:
            raise ValueError("Debe ser un numero entre 0 y 255")
        
        self.__rojo = valor
    
    def establecerVerde(self, valor:int):
        """Establece el Color Verde, en el valor recibido por parametro"""
        if not isinstance(valor,int) or valor < 0 or valor > 255:
            raise ValueError("Debe ser un numero entre 0 y 255")
        
        self.__verde = valor
    
    def establecerAzul(self, valor:int):
        """Establece el Color Azul, en el valor recibido por parametro"""
        if not isinstance(valor,int) or valor < 0 or valor > 255:
            raise ValueError("Debe ser un numero entre 0 y 255")
        
        self.__azul = valor
    
    def copiar(self, otroColor:'Color') -> None:
        """Copia los valores de 'otroColor' en self."""
        self.__rojo = otroColor.obtenerRojo()
        self.__verde = otroColor.obtenerVerde()
        self.__azul = otroColor.obtenerAzul()
    
    #Consultas
    def obtenerRojo(self) -> int:
        """Devuelve el valor del color rojo"""
        return self.__rojo
    
    def obtenerVerde(self) -> int:
        """Devuelve el valor del color verde"""
        return self.__verde
    
    def obtenerAzul(self) -> int:
        """Devuelve el valor del color azul"""
        return self.__azul
    
    def esRojo(self) -> bool:
        """retorna el valor verdadero si el objeto que recibe el mensaje representa el color rojo."""
        return self.__rojo == 255 and self.__verde == 0 and self.__azul == 0
    
    def esGris(self) -> bool:
        """retorna el valor verdadero si el objeto que recibe el mensaje representa el color gris."""
        return self.__rojo == self.__verde == self.__azul
    
    def esNegro(self) -> bool:
        """retorna el valor verdadero si el objeto que recibe el mensaje representa el color negro."""
        return self.__rojo == 0 and self.__verde == 0 and self.__azul == 0
    
    def complemento(self) -> 'Color':
        """
        Retorna un nuevo objeto con el color complemento del color del objeto que recibe el mensaje para alcanzar el color blanco.
        """
        complementoRojo = Color.__VALOR_MAX - self.__rojo
        complementoVerde = Color.__VALOR_MAX - self.__verde
        complementoAzul = Color.__VALOR_MAX - self.__azul
        
        return Color(complementoRojo,complementoVerde,complementoAzul)
    
    def esIgualQue(self, otroColor:'Color') -> bool:
        """
        etorna el valor verdadero si ambos objetos son equivalentes.
        """
        mismoRojo = self.obtenerRojo() == otroColor.obtenerRojo()
        mismoVerde = self.obtenerVerde() == otroColor.obtenerVerde()
        mismoAzul = self.obtenerAzul() == otroColor.obtenerAzul()
        
        return mismoRojo and mismoVerde and mismoAzul
    
    def clonar(self) -> 'Color':
        """
        Devuelve un nuevo color con el mismo estado interno que el color que recibe el mensaje.
        """
        return Color(self.__rojo, self.__verde, self.__azul)
    
    def __str__(self):
        return f"Intensidad de Colores: \n Rojo: {self.__rojo} \n Verde: {self.__verde} \n Azul: {self.__azul} \n"