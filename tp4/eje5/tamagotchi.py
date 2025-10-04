class Tamagotchi:
    #Atributos de Clase
    __MAX_VALOR = 100
    __MIN_VALOR = 0
    
    #Constructor
    def __init__(self, nombre:str, energia:int = __MAX_VALOR, diversion:int = __MAX_VALOR, higiene:int = __MAX_VALOR, dormido: bool = False, cantActividadesDesgaste: int = 0):
        self.__nombre = nombre
        self.__energia = energia
        self.__diversion = diversion
        self.__higiene = higiene
        self.__dormido = dormido
        self.__cantActividadesDesgaste = cantActividadesDesgaste
    
    #Consultas
    def ObtenerNombre(self) -> int:
        return self.__nombre
    
    def ObtenerEnergia(self) -> int:
        return self.__energia
    
    def ObtenerDiversion(self) -> int:
        return self.__diversion
    
    def ObtenerHigiene(self) -> int:
        return self.__higiene
    
    def EstaDormido(self) -> bool:
        return self.__dormido
    
    def ObtenerHumor(self) -> str:
        estados = [self.__energia, self.__diversion, self.__higiene]
        
        esFeliz = len([estado for estado in estados if estado > 70])
        esAlegre = len([estado for estado in estados if estado > 50 and estado <= 70])
        esNeutral = len([estado for estado in estados if estado > 30 and estado <= 50])
        esTriste = len([estado for estado in estados if estado >= 10 and estado <= 30])
        esMuyTriste = len([estado for estado in estados if estado < 10])
        
        if esFeliz == 3:
            return "Feliz"
        elif esAlegre >= 2:
            return "Alegre"
        elif esNeutral >= 2:
            return "Neutral"
        elif esTriste >= 2:
            return "Triste"
        elif esMuyTriste >= 2:
            return "Muy Triste"
        else:
            return "Indefenido"
    
    def EstaVivo(self) -> bool:
        if self.__energia > 0:
            return True
        else:
            return False
    
        
    def __str__(self) -> str:
        return (f"Mascota: {self.__nombre}\n"
            f"Energía: {self.__energia}\n"
            f"Diversión: {self.__diversion}\n"
            f"Higiene: {self.__higiene}\n"
            f"Dormido: {self.__dormido}\n"
            f"Humor: {self.ObtenerHumor()}")
    
    #Comandos
    def Comer(self):
        if not self.EstaVivo():
            print("La Mascota ha muerto! No puede realizar acciones!")
        if self.EstaDormido():
            print("La mascota esta Durmiendo!")
            despertarlo = int(input("Quieres despertarlo? (0 - NO, 1 - SI): "))
            if despertarlo == 1:
                self.Despertar()
                if self.__energia + 20 > Tamagotchi.__MAX_VALOR:
                    self.__energia = Tamagotchi.__MAX_VALOR
                else:
                    self.__energia += 20
            else:
                print("La mascota sigue durmiendo placidamente!")
        else:
            if self.__energia + 20 > Tamagotchi.__MAX_VALOR:
                self.__energia = Tamagotchi.__MAX_VALOR
            else:
                self.__energia += 20
    
    def Beber(self):
        if not self.EstaVivo():
            print("La Mascota ha muerto! No puede realizar acciones!")
        if self.EstaDormido():
            print("La mascota esta Durmiendo!")
            despertarlo = int(input("Quieres despertarlo? (0 - NO, 1 - SI): "))
            if despertarlo == 1:
                self.Despertar()
                if self.__energia + 10 > Tamagotchi.__MAX_VALOR:
                    self.__energia = Tamagotchi.__MAX_VALOR
                else:
                    self.__energia += 10
            else:
                print("La mascota sigue durmiendo placidamente!")
        else:
            if self.__energia + 10 > Tamagotchi.__MAX_VALOR:
                self.__energia = Tamagotchi.__MAX_VALOR
            else:
                self.__energia += 10
    
    def Jugar(self):
        if not self.EstaVivo():
            print("La Mascota ha muerto! No puede realizar acciones!")
        
        if self.__cantActividadesDesgaste >= 3:
            print("Ya hizo 3 actividades seguidas de desgaste. Ahora se duerme...")
            self.Dormir()
        
        if self.EstaDormido():
            print("La mascota esta Durmiendo!")
            despertarlo = int(input("Quieres despertarlo? (0 - NO, 1 - SI): "))
            if despertarlo == 1:
                self.Despertar()
                if self.__diversion + 40 > Tamagotchi.__MAX_VALOR:
                    self.__diversion = Tamagotchi.__MAX_VALOR
                else:
                    self.__diversion += 40
                if self.__energia - 20 < Tamagotchi.__MIN_VALOR:
                    self.__energia = Tamagotchi.__MIN_VALOR
                else:
                    self.__energia -= 20
                if self.__higiene - 15 < Tamagotchi.__MIN_VALOR:
                    self.__higiene = Tamagotchi.__MIN_VALOR
                else:
                    self.__higiene -= 15
            else:
                print("La mascota sigue durmiendo placidamente!")
        else:
            if self.__diversion + 40 > Tamagotchi.__MAX_VALOR:
                self.__diversion = Tamagotchi.__MAX_VALOR
            else:
                self.__diversion += 40
            if self.__energia - 20 < Tamagotchi.__MIN_VALOR:
                self.__energia = Tamagotchi.__MIN_VALOR
            else:
                self.__energia -= 20
            if self.__higiene - 15 < Tamagotchi.__MIN_VALOR:
                self.__higiene = Tamagotchi.__MIN_VALOR
            else:
                self.__higiene -= 15
        
        self.__cantActividadesDesgaste += 1
    
    def Caminar(self):
        if not self.EstaVivo():
            print("La Mascota ha muerto! No puede realizar acciones!")
        
        if self.__cantActividadesDesgaste >= 3:
            print("Ya hizo 3 actividades seguidas de desgaste. Ahora se duerme...")
            self.Dormir()
        
        if self.EstaDormido():
            print("La mascota esta Durmiendo!")
            despertarlo = int(input("Quieres despertarlo? (0 - NO, 1 - SI): "))
            if despertarlo == 1:
                self.Despertar()
                if self.__diversion + 20 > Tamagotchi.__MAX_VALOR:
                    self.__diversion = Tamagotchi.__MAX_VALOR
                else:
                    self.__diversion += 20
                if self.__energia - 10 < Tamagotchi.__MIN_VALOR:
                    self.__energia = Tamagotchi.__MIN_VALOR
                else:
                    self.__energia -= 10
                if self.__higiene - 8 < Tamagotchi.__MIN_VALOR:
                    self.__higiene = Tamagotchi.__MIN_VALOR
                else:
                    self.__higiene -= 8
            else:
                print("La mascota sigue durmiendo placidamente!")
        else:
            if self.__diversion + 20 > Tamagotchi.__MAX_VALOR:
                self.__diversion = Tamagotchi.__MAX_VALOR
            else:
                self.__diversion += 20
            if self.__energia - 10 < Tamagotchi.__MIN_VALOR:
                self.__energia = Tamagotchi.__MIN_VALOR
            else:
                self.__energia -= 10
            if self.__higiene - 8 < Tamagotchi.__MIN_VALOR:
                self.__higiene = Tamagotchi.__MIN_VALOR
            else:
                self.__higiene -= 8
        
        self.__cantActividadesDesgaste += 1
    
    def Saltar(self):
        if not self.EstaVivo():
            print("La Mascota ha muerto! No puede realizar acciones!")
        
        if self.__cantActividadesDesgaste >= 3:
            print("Ya hizo 3 actividades seguidas de desgaste. Ahora se duerme...")
            self.Dormir()
        
        if self.EstaDormido():
            print("La mascota esta Durmiendo!")
            despertarlo = int(input("Quieres despertarlo? (0 - NO, 1 - SI): "))
            if despertarlo == 1:
                self.Despertar()
                if self.__diversion + 10 > Tamagotchi.__MAX_VALOR:
                    self.__diversion = Tamagotchi.__MAX_VALOR
                else:
                    self.__diversion += 10
                if self.__energia - 15 < Tamagotchi.__MIN_VALOR:
                    self.__energia = Tamagotchi.__MIN_VALOR
                else:
                    self.__energia -= 15
                if self.__higiene - 10 < Tamagotchi.__MIN_VALOR:
                    self.__higiene = Tamagotchi.__MIN_VALOR
                else:
                    self.__higiene -= 10
            else:
                print("La mascota sigue durmiendo placidamente!")
        else:
            if self.__diversion + 10 > Tamagotchi.__MAX_VALOR:
                self.__diversion = Tamagotchi.__MAX_VALOR
            else:
                self.__diversion += 10
            if self.__energia - 15 < Tamagotchi.__MIN_VALOR:
                self.__energia = Tamagotchi.__MIN_VALOR
            else:
                self.__energia -= 15
            if self.__higiene - 10 < Tamagotchi.__MIN_VALOR:
                self.__higiene = Tamagotchi.__MIN_VALOR
            else:
                self.__higiene -= 10
        
        self.__cantActividadesDesgaste += 1
    
    def Dormir(self):
        if not self.EstaVivo():
            print("La Mascota ha muerto! No puede realizar acciones!")
        if self.EstaDormido():
            print("La mascota ya esta Durmiendo!")
            despertarlo = int(input("Quieres despertarlo? (0 - NO, 1 - SI): "))
            if despertarlo == 1:
                self.Despertar()
                self.__cantActividadesDesgaste = 0
            else:
                print("La mascota sigue durmiendo placidamente!")
        else:
            if self.__energia + 20 > Tamagotchi.__MAX_VALOR:
                self.__energia = Tamagotchi.__MAX_VALOR
            else:
                self.__energia += 20
            if self.__diversion - 10 < Tamagotchi.__MIN_VALOR:
                self.__diversion = Tamagotchi.__MIN_VALOR
            else:
                self.__diversion -= 10
            self.__dormido = True
            self.__cantActividadesDesgaste = 0
    
    def Banar(self):
        if not self.EstaVivo():
            print("La Mascota ha muerto! No puede realizar acciones!")
        if self.EstaDormido():
            print("La mascota esta Durmiendo!")
            despertarlo = int(input("Quieres despertarlo? (0 - NO, 1 - SI): "))
            if despertarlo == 1:
                self.Despertar()
                if self.__higiene + 40 > Tamagotchi.__MAX_VALOR:
                    self.__higiene = Tamagotchi.__MAX_VALOR
                else:
                    self.__higiene += 40
                if self.__diversion - 10 < Tamagotchi.__MIN_VALOR:
                    self.__diversion = Tamagotchi.__MIN_VALOR
                else:
                    self.__diversion -= 10 
            else:
                print("La mascota sigue durmiendo placidamente!")
        else:
            if self.__higiene + 40 > Tamagotchi.__MAX_VALOR:
                self.__higiene = Tamagotchi.__MAX_VALOR
            else:
                self.__higiene += 40
            if self.__diversion - 10 < Tamagotchi.__MIN_VALOR:
                self.__diversion = Tamagotchi.__MIN_VALOR
            else:
                self.__diversion -= 10 
    
    def Despertar(self):
        self.__dormido = False
