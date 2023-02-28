# ma classe
class Livre:
    # mes attributs pv "__"
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages

    # mes getters
    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_nb_pages(self):
        return self.__nb_pages

    # mes setters
    def set_titre(self, sortie_titre):
        self.__titre = sortie_titre

    def set_auteur(self, sortie_auteur):
        self.__auteur = sortie_auteur

    def set_nb_pages(self, sortie_nb_pages):
        self.__nb_pages = sortie_nb_pages


# mon objet
obj = Livre("La rue", "La ruelle", 5)

# afficher les "attributs" avec mes getters
print(obj.get_titre())
print(obj.get_auteur())
print(obj.get_nb_pages())
