class Person:
    def __init__(self,nom):
        self.nom = nom
    
    def dire_bonjout(self):
        print(f"Bonjour, je m'appelle {self.nom}!")