# ma classe
class Rectangle:
    # mon constructuer avec l'initialisation de longueur et largeur
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    # mon getters
    def get_longueur(self):
        return self.__longueur

    # mon setters
    def set_longueur(self, longueur):
        self.__longueur = longueur

    # mon getters
    def get_largeur(self):
        return self.__largeur

    # mon setters
    def set_largeur(self, largeur):
        self.__largeur = largeur


# Création d'un rectangle avec une longueur de 10 et une largeur de 5
rect = Rectangle(10, 5)

# Affichage des valeurs initiales
print("Longueur :", rect.get_longueur())
print("Largeur :", rect.get_largeur())
