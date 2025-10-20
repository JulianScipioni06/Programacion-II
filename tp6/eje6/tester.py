from disciplina import Disciplina
from participante import Participante

class tester:
    def test():
        # Crear disciplinas
        disciplina1 = Disciplina("Carrera 100m", "Prueba de velocidad corta.")
        disciplina2 = Disciplina("Salto en largo", "Competencia de salto horizontal.")

        # Crear participantes
        p1 = Participante("Juan Pérez", 22, "Argentina",[disciplina1, disciplina2])
        p2 = Participante("María Gómez", 25, "Uruguay",[disciplina1])
        p3 = Participante("Carlos López", 20, "Chile")
        p4 = Participante()
        
        print(p1)
        print(p2)
        print(p3)
        
        print("-"*60)
        p2.competir(disciplina2)
        print(p2)
        
        print("-"*60)
        p4.establecerNombre("Lautaro")
        p4.establecerEdad(19)
        p4.establecerNacionalidad("Brasil")
        p4.competir(disciplina1)
        
        print(p4)

if __name__ == "__main__":
    tester.test()