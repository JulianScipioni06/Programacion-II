class Especie:
    #Constructor
    def __init__(self, nombre:str, machos:int = 0, hembras:int = 0, ritmo:float = 0.0):
        """
        Inicializa una nueva Especie:
        Parametros:
        - nombre: Nombre de La Especie
        - machos: Cantidad de Machos Registrados
        - hembras: Cantidad de Hembras Registradas
        - ritmo: Crecimiento anual de la poblacion a lo largo de 10 años
        """
        self.__nombre = nombre
        self.__machos = machos
        self.__hembras = hembras
        self.__ritmo = ritmo
    
    #Comandos
    def establecerHembras(self, cantHembras:int):
        """Establece la Cantidad de Hembras"""
        if not isinstance(cantHembras,int) or cantHembras < 0:
            raise ValueError("Cantidad de Hembras debe ser un Entero Positivo o 0")
        
        self.__hembras = cantHembras
    
    def establecerMachos(self, cantMachos:int):
        """Establece la Cantidad de Machos"""
        if not isinstance(cantMachos,int) or cantMachos < 0:
            raise ValueError("Cantidad de Machos debe ser un Entero Positivo o 0")
        
        self.__machos = cantMachos
    
    def establecerRitmo(self, ritmo:float):
        """Establece el Ritmo de crecimiento"""
        if not isinstance(ritmo,(int,float)):
            raise ValueError("Ritmo debe ser un numero Positivo o 0")
        
        self.__ritmo = ritmo
    
    def actualizarHembras(self, cantHembras:int):
        """Actualiza la Cantidad de Hembras"""
        if not isinstance(cantHembras,int):
            raise TypeError("Cantidad de Hembras debe ser un Entero")
        
        if self.__hembras + cantHembras < 0:
            self.__hembras = 0
        else:
            self.__hembras += cantHembras
    
    def actualizarMachos(self, cantMachos:int):
        """Actualiza la Cantidad de Machos"""
        if not isinstance(cantMachos,int):
            raise TypeError("Cantidad de Machos debe ser un Entero")
        
        if self.__machos + cantMachos < 0:
            self.__machos = 0
        else:
            self.__machos += cantMachos
    
    def actualizarRitmo(self, ritmo:float):
        """Actualiza el Ritmo de crecimiento"""
        if not isinstance(ritmo,(int,float)):
            raise TypeError("Ritmo debe ser un numero")
        
        self.__ritmo += ritmo
    
    #Consultas
    def obtenerNombre(self) -> str:
        """Devuelve el Nombre de la Especie"""
        return self.__nombre
    
    def obtenerCantHembras(self) -> int:
        """Devuelve la cantidad de hembras de la especie"""
        return self.__hembras
    
    def obtenerCantMachos(self) -> int:
        """Devuelve la cantidad de machos de la especie"""
        return self.__machos
    
    def obtenerRitmo(self) -> float:
        """Devuelve el Ritmo de crecimiento"""
        return self.__ritmo
    
    def poblacionActual(self) -> int:
        """Devuelve el total de la suma de hembras y machos"""
        return self.__hembras + self.__machos
    
    def poblacionEstimada(self, anios:int) -> int:
        """Devuelve la población estimada dentro de 'anios' años, según el ritmo anual (porcentual)."""
        if not isinstance(anios, int) or anios < 0:
            raise ValueError("anios debe ser un entero mayor o igual que 0")
        
        return int(self.poblacionActual() * ((1 + self.__ritmo) ** anios))
    
    def aniosParaPoblacion(self, poblacion_objetivo:int) -> int:
        """Devuelve cuántos años serán necesarios estimativamente para que la población alcance un valor dado."""
        actual = self.poblacionActual()
        if poblacion_objetivo <= actual:
            return 0
        if self.__ritmo <= 0:
            return None

    # Bucle controlado: va multiplicando hasta pasar el objetivo
        crecimiento = 1 + self.__ritmo
        poblacion = actual
        anios = 0

        while poblacion < poblacion_objetivo:
            poblacion *= crecimiento
            anios += 1
            if anios > 10000:   # seguridad
                return None

        return anios
    
    def riesgo(self) -> str: 
        """Devuelve el nivel de riesgo de extinción (“verde” si el ritmo de crecimiento es positivo, “amarillo” si es nulo y “rojo” si es negativo)"""
        
        if self.__ritmo > 0.00:
            return "Verde"
        elif self.__ritmo == 0.00:
            return "Amarillo"
        else:
            return "Rojo"
    
    def masHembras(self) -> bool:
        """Devuelve TRUE si en una especie dada es mayor el número de hembras que de machos"""
        
        if self.__hembras > self.__machos:
            return True
        elif self.__hembras < self.__machos:
            return False
        else:
            return None
    
    def mayorRitmo(self, otraEspecie:'Especie') -> 'Especie':
        """Devuelve la especie que tiene el mayor ritmo de crecimiento"""
        
        if self.__ritmo > otraEspecie.__ritmo:
            return self
        elif self.__ritmo < otraEspecie.__ritmo:
            return otraEspecie
        else:
            return None
    
    def clonar(self) -> 'Especie': 
        """Devuelve un nuevo objeto Especie con el mismo estado interno el objeto qeu recibe el mensaje"""
        
        return Especie(self.__nombre, self.__machos, self.__hembras, self.__ritmo)
    
    def __str__(self):
        return (f"Especie: {self.__nombre} \n"
                f"Machos: {self.__machos} \n"
                f"Hembras: {self.__hembras} \n"
                f"Ritmo: {self.__ritmo}")