from disciplina import Disciplina

class Participante:
    def __init__(self, nombre:str = "-", edad:int = 1, nacionalidad:str = "-", disciplinas:list[Disciplina] = None):
        """
        Inicializa un nuevo objeto Participante.
        Parametros:
        - nombre: nombre del participante
        - edad: edad del participante
        - nacionalidad: nacionalidad del participante
        - disciplinas: disciplinas en las que participa el participante
        """
        if not isinstance(nombre,str) or nombre.strip() == "":
            raise ValueError("Nombre debe ser un string y no puede estar vacio!")
        if not isinstance(edad,int) or edad <= 0:
            raise ValueError("Edad debe ser un numero entero mayor que 0!")
        if not isinstance(nacionalidad,str) or nacionalidad.strip() == "":
            raise ValueError("Nacionalidad debe ser un string y no puede estar vacio!")
        self.__nombre = nombre
        self.__edad = edad
        self.__nacionalidad = nacionalidad
        self.__disciplinas = []
        
        if disciplinas != None:
            if isinstance(disciplinas,Disciplina):
                self.__disciplinas.append(disciplinas)
            elif isinstance(disciplinas, list):
                for dis in disciplinas:
                    if isinstance(dis, Disciplina):
                        self.__disciplinas.append(dis)
    
    def establecerNombre(self, nombre: str):
        """Establece como nombre el string recibido por parametro."""
        if not isinstance(nombre,str) or nombre.strip() == "":
            raise ValueError("Nombre debe ser un string y no puede estar vacio!")
        
        self.__nombre = nombre
    
    def establecerEdad(self, edad: int):
        """Establece como edad el int recibido por parametro."""
        if not isinstance(edad,int) or edad <= 0:
            raise ValueError("Edad debe ser un numero entero mayor que 0!")
        
        self.__edad = edad
    
    def establecerNacionalidad(self, nacionalidad: str):
        """Establece como nacionalidad el string recibido por parametro."""
        if not isinstance(nacionalidad,str) or nacionalidad.strip() == "":
            raise ValueError("Nombre debe ser un string y no puede estar vacio!")
        
        self.__nacionalidad = nacionalidad
    
    def competir(self, disciplina: Disciplina):
        """Establece una disciplina en la cual compite el partcipante"""
        if disciplina not in self.__disciplinas:
            if isinstance(disciplina, Disciplina):
                self.__disciplinas.append(disciplina)
    
    def obtenerNombre(self) -> str:
        """Devuelve el nombre del Participante"""
        return self.__nombre
    
    def obtenerEdad(self) -> int:
        """Devuelve la edad del Participante"""
        return self.__edad
    
    def obtenerNacionalidad(self) -> str:
        """Devuelve la nacionalidad del Participante"""
        return self.__nacionalidad
    
    def obtenerDisciplinas(self) -> list[Disciplina]:
        """Devuelve las disciplinas en las que compite el Participante"""
        return self.__disciplinas
    
    def __str__(self):
        return f"- Nombre: {self.__nombre}\n - Edad: {self.__edad}\n - Nacionalidad: {self.__nacionalidad}\n - Disciplinas: {self.__disciplinas}\n"
    
