# comprendre les base : CLASS ET OBJETS
    - class : plan ou recent
    - objet : instance >> resultat correct ou realisation

    + ex : class Person

# apprendre petit a petit avec des analogues
    - class : Plan de constuction
    - Objet : Maison construite a partire du plan
    - Methodes : Action que l'objet peut faire
        + ouvrir la port
        + allumer la lumiere
        ...
    - attributs :Proprietes de l'objet
        + couleur
        + taille de la maison

# pratiquer avec des exemple du quotidien
    - fais des class basse sur des conceots simple : Animal, Voiture, Livre
    + ex : class Chien, 

# Utiliser le POO pour organiser ton code
    - But principale : Organiser les donnees et le comportement ensembles
    + ex : si tu travailes sur un jeu:
        class Joueur
        class Ennemi
        class Niveau
        ...

# Maitriser les concepts cles progressivements
    - Encapsulation (Cacher les details intern)
        - attribut privee 
        + ex : class compteBancaire
    
    - Heritage (reutiliser du code)
        - class Animal
        - class Char(Animal)
    
    - Polymorphism (Une interface : +r comportements):
        - chien.jouer_son != oiseau.jouer_son
    
# Projette-toi avec des petites projects
    - gestion d'une bibliotheque
        class Livre
        class Lecteur
        class Emprunt
    
    - jeu simple :
        class Personnage
        class Ennemi
        class Niveau

    - Application des gestoin:
        class Produit
        class Commande
        class Client
    
# le term super() est utile pour travailler avec l'HERITAGE
    - perment d'appeler le methoded'une class Parent depuis une class Enfant
    - outille dinalyque
    - syntax :  super().methode_parent()
                Parent.methode_parent()