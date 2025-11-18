class Atleta:
    #Atributos de Clase
    __MAX_VALOR = 100
    __MIN_VALOR = 0
    
    #Atributos de Instancia
    def __init__(self, nombre:str):
        """
        Inicializa un nuevo personaje.
        Parámetros:
        - nombre: El nombre del Atleta.
        """
        self.__nombre = nombre
        self.__energia = Atleta.__MAX_VALOR
        self.__destreza = Atleta.__MIN_VALOR
        self.__cantEntrenamientos = Atleta.__MIN_VALOR
    
    #Comandos
    def Entrenar(self):
        """
        Consume 5 unidades de energía.
        Si llega a 5 entrenamientos, suma un punto de destreza.
        """
        if self.__energia >= 5:
            self.__energia -= 5
            self.__cantEntrenamientos += 1
            
            if self.__cantEntrenamientos % 5 == 0:
                self.__destreza += 1
        else:
            print("El atleta debe Descansar!!!")
    
    def Descansar(self):
        """
        Recupera 20 puntos de Energia.
        """
        if self.__energia + 20 > Atleta.__MAX_VALOR:
            self.__energia = Atleta.__MAX_VALOR
        else:
            self.__energia += 20
    
    #Consultas
    def ObtenerNombre(self):
        """Devuelve el Nombre del Atleta"""
        return self.__nombre
    def ObtenerEnergia(self):
        """Devuelve la energia del Atleta"""
        return self.__energia
    def ObtenerDestreza(self):
        """Devuelve la destreza del Atleta"""
        return self.__destreza
    def ObtenerCantidadEntrenamientos(self):
        """Devuelve la cantidad de entrenamientos del Atleta"""
        return self.__cantEntrenamientos
    
    def mismaDestrezaQue(self, otro:'Atleta'):
        """
        Compara las Destrezas de los Atletas, y compara si son iguales!
        """
        return self.__destreza == otro.__destreza
    
    def esMejorQue(self, otro:'Atleta'):
        """
        Compara las Destrezas de los Atletas, y se fija si la de uno es mayor que el otro!
        """
        return self.__destreza > otro.__destreza
    
    def __str__(self):
        return f"Nombre del Atleta: {self.__nombre} \n Energia: {self.__energia} \n Destreza: {self.__destreza} \n Cantidad de Entrenamientos: {self.__cantEntrenamientos} \n"