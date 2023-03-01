# création classe "ville"
class Ville:
    # mes attributs pv nom + nb habitants
    def __init__(self, nom, nb_habitants):
        self.nom = nom
        self.__nb_habitants = nb_habitants

    def get_nb_habitants(self):
        return self.__nb_habitants

    def ajouterPopulation(self):
        self.__nb_habitants += 1


# ma classe personne
class Personne:
    # mes attributs pv nom+age+ville
    def __init__(self, nom, age, ville):
        self.nom = nom
        self.age = age
        self.ville = ville

    # création méthode
    def ajouterPopulation(self):
        self.ville.ajouterPopulation()


# objet ville paris marseille
paris = Ville("Paris", 1000000)
marseille = Ville("Marseille", 861635)

# Affichage du nombre d'habitants des villes
print("Population de la ville de Paris :", paris.get_nb_habitants())
print("Population de la ville de Marseille :", marseille.get_nb_habitants())

# objet john myrtill et chloe
john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

# je met john myrtille et chloe chacun dans leur ville
john.ajouterPopulation()
myrtille.ajouterPopulation()
chloe.ajouterPopulation()

# Affichage du nombre d'habitants des villes après l'arrivée des nouvelles personnes
print("Mis à jour de la population de la ville de Paris", paris.get_nb_habitants())
print("Mis à jour de la population de la ville de Marseille", marseille.get_nb_habitants())
