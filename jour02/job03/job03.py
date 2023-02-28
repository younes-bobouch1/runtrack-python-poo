class Livre:
    # mes attributs pv "__"
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages
        self.__disponible = True

    # nvl méthode "vérification"
    def verification(self):
        return self.__disponible

    # nvl méthode "emprunter" (+ chatgpt)
    def emprunter(self):
        try:
            if self.__disponible:
                self.__disponible = False
                return True
            else:
                return False
        except:
            return False

    # nvl méthode "rendre" (+ chatgpt)
    def rendre(self):
        try:
            if not self.__disponible:
                self.__disponible = True
                return True
            else:
                return False
        except:
            return False


# objet
livre = Livre("A", "A", 0)

# livre présent ou pas
print(livre.verification())

# fonction emprunter
livre.emprunter()

# livre après emprunter
print(livre.verification())

# rendre livre
livre.rendre()

# voir livre après rendu
print(livre.verification())




