#je crée ma classe
class Personne:
    #fonction ou j'initialise des 2 valeurs
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    #ma méthode
    def SePresenter(self):
        #je veux prenom et nom
        return f"Je suis  {self.prenom} {self.nom}."

#les valeurs que je veux donner a prenom et nom 2x
p1 = Personne("John", "Doe")
p2 = Personne("Jean", "Dupond")

#j'affiche mes valeurs
print(p1.SePresenter())
print(p2.SePresenter())