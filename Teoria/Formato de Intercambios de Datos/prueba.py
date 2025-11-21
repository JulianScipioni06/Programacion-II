import json

class Persona:
    def __init__(self, dni:int, nombre:str, apellido:str):
        if not isinstance(dni, int):
            raise ValueError("El DNI debe ser un entero.")
        if not isinstance(nombre, str) :
            raise ValueError("El nombre debe ser un string.")
        if not isinstance(apellido, str):
            raise ValueError("El apellido debe ser un string.")
        self.__dni=dni
        self.__nombre=nombre
        self.__apellido=apellido
    
    def to_json(self):
        dicc_persona={"dni": self.__dni, "nombre": self.__nombre, "apellido": self.__apellido}
        return json.dumps(dicc_persona, ensure_ascii=False)
        
    @classmethod
    def from_json(cls, json_data):
        datos=json.loads(json_data)
        return cls(datos["dni"], datos["nombre"], datos["apellido"])