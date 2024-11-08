class Animal:
    def __init__(self,nom):
        self._nom = nom
        self.info()
        
    def se_deplacer(self):
        print(f"{self._nom} se déplace.")
    def info(self):
        print(f"je suis un Animal : Nom : {self._nom}")
    
class Chien(Animal):
    def __init__(self,nom,race):
        super().__init__(nom)   # appel __init__ de Animal
        self._race = race
    
    def aboyer(self):
        print(f"{self._nom}, un{self._race} aboie : WOUF")
    
# exemple d'utilisation
ch_1 = Chien("Rex", "Berger Allemand")
ch_1.se_deplacer()
ch_1.aboyer()
