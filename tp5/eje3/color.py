class Color:
    #Atributo de Clase
    __VALOR_MAX = 255
    __VALOR_MIN = 0
    
    def __init__(self):
        """
        Inicializa un Color con el Rojo, Azul y Verde en 255.
        """
        self.__rojo = Color.__VALOR_MAX
        self.__verde = Color.__VALOR_MAX
        self.__azul = Color.__VALOR_MAX
    
    #Comandos
    def Variar(self, valor:int):
        """
        Modifica cada componente de color sumándole si es posible, un valor dado.
        Si al Sumarle el Valor supera el Maximo o el Minimo, se ajusta a los valores correspondientes.
        """
        if not isinstance(valor,int):
            raise TypeError("El valor debe ser un numero entero")
        
        Color.VariarRojo(valor)
        Color.VariarVerde(valor)
        Color.VariarAzul(valor)
    
    def VariarRojo(self, valor:int):
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
    
    def VariarVerde(self, valor:int):
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
    
    def VariarAzul(self, valor:int):
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
    
    def EstablecerRojo(self, valor:int):
        """Establece el Color Rojo, en el valor recibido por parametro"""
        if not isinstance(valor,int) or valor < 0 or valor > 255:
            raise ValueError("Debe ser un numero entre 0 y 255")
        
        self.__rojo = valor
    
    def EstablecerVerde(self, valor:int):
        """Establece el Color Verde, en el valor recibido por parametro"""
        if not isinstance(valor,int) or valor < 0 or valor > 255:
            raise ValueError("Debe ser un numero entre 0 y 255")
        
        self.__verde = valor
    
    def EstablecerAzul(self, valor:int):
        """Establece el Color Azul, en el valor recibido por parametro"""
        if not isinstance(valor,int) or valor < 0 or valor > 255:
            raise ValueError("Debe ser un numero entre 0 y 255")
        
        self.__azul = valor
    
    def Copiar(self, otroColor:'Color') -> None:
        """Copia los valores de 'otroColor' en self."""
        self.__rojo = otroColor.ObtenerRojo()
        self.__verde = otroColor.ObtenerVerde()
        self.__azul = otroColor.ObtenerAzul()
    
    #Consultas
    def ObtenerRojo(self) -> int:
        """Devuelve el valor del color rojo"""
        return self.__rojo
    
    def ObtenerVerde(self) -> int:
        """Devuelve el valor del color verde"""
        return self.__verde
    
    def ObtenerAzul(self) -> int:
        """Devuelve el valor del color azul"""
        return self.__azul
    
    def esRojo(self) -> bool:
        """retorna el valor verdadero si el objeto que recibe el mensaje representa el color rojo."""
        return self.__rojo == 255 and self.__verde == 0 and self.__azul == 0
    
    def esGris(self) -> bool:
        """retorna el valor verdadero si el objeto que recibe el mensaje representa el color gris."""
        return self.__rojo == self.__verde and self.__rojo == self.__azul and self.__verde == self.__azul
    
    def esNegro(self) -> bool:
        """retorna el valor verdadero si el objeto que recibe el mensaje representa el color negro."""
        return self.__rojo == 0 and self.__verde == 0 and self.__azul == 0
    
    def Complemento(self) -> 'Color':
        