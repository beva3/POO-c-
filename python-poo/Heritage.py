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