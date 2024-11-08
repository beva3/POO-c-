class Chien :
    def __init__(self,nom, race):
        self.nom = nom
        self.race = race

    def info(self):
        print("-"*3,"Chien", "-"*3)
        print(f"Nom     : {self.nom}")
        print(f"Race    : {self.race}")
        print("-"*13)
    def deboyer(self):
        print(f"{self.nom} dit. WOUF !!")
        
chien_1 = Chien("Rex", "Berger Allemand")
chien_1.info()
chien_1.deboyer()