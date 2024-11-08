class Animal:
    def __init__(self,):
        print("Animal ....")
    
    def manger(self):
        print("Animal dit <<Je mange.>>")
 
class Chat(Animal):    # cet chat herite de l' Aniimal
    def miauler(self):
        print("Chien dit <<Miaou Miaou.>>")

c_1 = Chat()
c_1.manger()    # Animal dit <<Je mange.>>
c_1.miauler()   # Chien dit <<Miaou Miaou.>>

# polymorphismes :
class Chien:
    def faire_son(self):
        print("Chien ABOIE")
class Oiseau:
    def faire_son(self):
        print("Oiseau SOUFFLE")

def jouer_son(animal):
    animal.faire_son()


oiseau = Oiseau()
chien = Chien()

jouer_son(oiseau)
jouer_son(chien)