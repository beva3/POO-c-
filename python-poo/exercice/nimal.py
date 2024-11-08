# Crée une classe Animal avec une méthode parler().
# Ensuite, crée deux classes enfants, Chien et Chat, 
# qui héritent de Animal et redéfinissent la méthode parler().
# Chaque classe doit afficher un son différent.

# Crée une fonction faire_parler() qui prend un objet Animal et 
# appelle sa méthode parler(). 
# Teste cette fonction avec différentes classes (par exemple, Chien et Chat).

# Ajoute une méthode deplacement() 
# dans les classes Chien et Chat qui affiche comment chaque animal se déplace. 
# Parcours une liste d'animaux et appelle à la fois parler() et 
# deplacement() pour chacun.

class Animal:
    def __init__(self):
        print("Creation animal...")

    def parler(self):
        # print("Animal parle...")
        pass

class Chien(Animal):
    def __init__(self):
        super().__init__()
        print("\tCreation chien...")
    
    def parler(self):
        print("Chien aboie : WOUF")

    def deplacement(self):
        print("le Chien court.")

class  Chat(Animal):
    def __init__(self):
        super().__init__()
        print("\tCreation chat...")
    
    def parler(self):
        print("Chat miaule : Miaou")

    def deplacement(self):
        print("le Chat saut.")

def faire_parler(Objet):
    Objet.parler()

# Test
animaux = [Chien(), Chat()]

print('-'*10,'methode parler()','-'*10)
for animal in animaux:
    animal.parler()

print('-'*10,'func faire_parler()','-'*10)
for animal in animaux:
    faire_parler(animal)

print('-'*10,'methode deplacement()','-'*10)
for animal in animaux:
    animal.deplacement()