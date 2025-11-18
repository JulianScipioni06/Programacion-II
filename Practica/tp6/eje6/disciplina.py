# from participante import Participante

class Disciplina:
    #participantes:list[Participante] = None
    def __init__(self, nombre:str = "", descripcion:str = ""):
        """
        Inicializa un nuevo objeto Disciplina.
        Parametros:
        - nombre: nombre de la disciplina
        - descripcion: descripcion de la disciplina
        - participantes: participantes que compiten en esta disciplina
        """
        if not isinstance(nombre,str) or nombre.strip() == "":
            raise ValueError("Nombre debe ser un string y no puede estar vacio!")
        if not isinstance(descripcion,str) or descripcion.strip() == "":
            raise ValueError("descripcion debe ser un string y no puede estar vacio!")
        self.__nombre = nombre
        self.__descripcion = descripcion
        # self.__participantes = []
        
        # if participantes != None:
        #     if isinstance(participantes,Disciplina):
        #         self.__participantes.append(participantes)
        #     elif isinstance(participantes, list):
        #         for dis in participantes:
        #             if isinstance(dis, Disciplina):
        #                 self.__participantes.append(dis)
    
    def establecerNombre(self, nombre: str):
        """Establece como nombre el string recibido por parametro."""
        if not isinstance(nombre,str) or nombre.strip() == "":
            raise ValueError("Nombre debe ser un string y no puede estar vacio!")
        
        self.__nombre = nombre
    
    def establecerDescripcion(self, descripcion: str):
        """Establece como descripcion el string recibido por parametro."""
        if not isinstance(descripcion,str) or descripcion.strip() == "":
            raise ValueError("Nombre debe ser un string y no puede estar vacio!")
        
        self.__descripcion = descripcion
    
    # def establecerParticipante(self, participante: Participante):
    #     """Establece una disciplina en la cual compite el partcipante"""
    #     if participante not in self.__participantes:
    #         if isinstance(participante, Disciplina):
    #             self.__participantes.append(participante)
    
    def obtenerNombre(self) -> str:
        """Devuelve el nombre de la disciplina"""
        return self.__nombre
    
    def obtenerDescripcion(self) -> str:
        """Devuelve la descripcion de la disciplina"""
        return self.__descripcion
    
    # def obtenerParticipantes(self) -> list[Participante]:
    #     """Devuelve los participantes que practican esa disciplina"""
    #     return self.__participantes
    
    def __str__(self):
        # - Participantes: {self.__participantes}\n
        return f"- Nombre: {self.__nombre}\n - Descripcion: {self.__descripcion}\n"
        
    def __repr__(self):
        return f"Disciplina('{self.__nombre}', '{self.__descripcion}')"
