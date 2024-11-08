# Crée deux classes indépendantes Voiture et Bateau, 
# chacune ayant une méthode deplacer(). 
# Utilise une fonction pour appeler cette méthode sur n'importe quel objet 
# qui l'implémente.

class Voiture:
    def __init__(self,marque):
        self.marque = marque
    def deplacer(self):
        print(f"{self.marque} roule sur la route.")
    
class Bateau:
    def __init__(self,marque):
        self.marque = marque
    
    def deplacer(self):
        print(f"{self.marque} navigue dans l'océan.")

def voyager(Objet):
    Objet.deplacer()

# Test
vehicules = [Voiture("Toyota"), Bateau("Titanic")]

for v in vehicules:
    voyager(v)