# Crée une classe Animal avec une méthode parler().
# Ensuite, crée deux classes enfants, Chien et Chat, 
# qui héritent de Animal et redéfinissent la méthode parler().
# Chaque classe doit afficher un son différent.

class Animal:
    def __init__(self):
        print("Creation animal...")

    def parler(self):
        # print("Animal parle...")
        pass

class Chien(Animal):
    def __init__(self):
        super().__init__()
        print("Creation chien...")
    
    def parler(self):
        print("Chien aboie : WOUF")

class  Chat(Animal):
    def __init__(self):
        super().__init__()
        print("Creation chat...")
    
    def parler(self):
        print("Chat miaule : Miaou")

# Test
animaux = [Chien(), Chat()]

for animal in animaux:
    animal.parler()