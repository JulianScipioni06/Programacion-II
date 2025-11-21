import json
from contacto import Contacto

class TesterContacto:
    @staticmethod
    def test():
        # Crea objetos de la clase Contacto y almacenarlos en una lista
        contacto1 = Contacto("Juan","Perez","1234","juanperez@gmail.com","zelarrayan 646")
        contacto2 = Contacto("Martin","Sanchez","9999","martinsanchez@gmail.com","salta 365")
        contacto3 = Contacto("Pedro","Rodriguez","7474","pedrorodriguez@gmail.com","castelli 326")
        
        # Guarda esa lista completa en un archivo JSON “contactos.json”.
        lista_contactos = []
        lista_contactos.append(contacto1)
        lista_contactos.append(contacto2)
        lista_contactos.append(contacto3)
        
        for c in lista_contactos:
            print(c)
        
        with open("contactos.json","w") as archivo:
            diccionarios_contactos = [contacto.to_diccionario() for contacto in lista_contactos]
            json.dump(diccionarios_contactos, archivo, ensure_ascii=False, indent=4)
            
            print("Archivo cargado!!!")
        
        # En una nueva lista vacía almacena los objetos reconstruidos a partir del archivo JSON
        print("---------------------------------------------------------------")
        print("JSON a Objetos")
        print("---------------------------------------------------------------")
        
        contactos_objetos = []
        
        with open("contactos.json","r") as archivo:
            data = json.load(archivo) #data es una lista de diccioanarios
            
            for dicc_contacto in data:
                contacto = Contacto.from_diccionario(dicc_contacto)
                contactos_objetos.append(contacto)
        
        for obj in contactos_objetos:
            print(obj)

if __name__ == "__main__":
    TesterContacto.test()