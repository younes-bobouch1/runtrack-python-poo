# création de ma classe Personne
class Personne:
    # méthode privée
    def __init__(self, age=14):
        self.age = age

    # méthode pour afficher l'age entrée en paramètre
    def afficherAge(self):
        print("Age personne =", self.age)

    # méthode simple pour print "Hello"
    def bonjour(self):
        print("Hello")

    # méthode pour modifier l'age en fonction du paramètre rentré
    def modifierAge(self, agee):
        self.age = agee


# création de ma classe Eleve
class Eleve(Personne):
    # méthode simple pour print "Je vais en cours"
    def allerEnCours(self):
        print("Je vais en cours")

    # méthode textualisé l'age
    def affichageAge(self):
        print("J'ai", self.age, "ans")


# création de ma classe Professeur
class Professeur(Personne):
    # méthode privée (aide chatgpt)
    def __init__(self, matiereEnseignee, age=30):
        super().__init__(age)
        self.matiereEnseignee = matiereEnseignee

    # méthode simple pour print "Le cours va commencer"
    def enseigner(self):
        print("Le cours va commencer")


# instance eleve + personne
personne = Personne()
elevve = Eleve()

# âge eleve
elevve.affichageAge()

# appel des méthodes
personne.afficherAge()
personne.bonjour()
elevve.allerEnCours()
elevve.affichageAge()
Professeur("").enseigner()  # faut-il afficher la matière ?
