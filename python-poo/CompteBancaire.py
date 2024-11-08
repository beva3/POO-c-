class CompteBancaire:
    def __init__(self,solde):
        self.__solde = solde # attribut privee

    def afficher_solde(self):
        print(f"Solde : {self.__solde}$")
    
    def deposer(self,montant):
        self.__solde += montant
        print(f"Dépot de {montant}$ effectué, nouveau solde : {self.__solde}$")

    
compte = CompteBancaire(100)
compte.afficher_solde()         # solde : 100$
compte.deposer(50)              # solde : 150$