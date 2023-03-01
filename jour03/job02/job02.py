#création de ma classe comptebancaire
class CompteBancaire:
    #tout mes attributs pv
    def __init__(self, num_compte, nom, prenom, solde, autorisation_decouvert=False):
        self.__num_compte = num_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert_autorise = autorisation_decouvert

    #affichage du détail du compte
    def afficher(self):
        print("Numéro compte:", self.__num_compte)
        print("Détenteur:", self.__prenom, self.__nom)
        print("Solde:", self.__solde, "€")

    #affichage de mon solde
    def afficherSolde(self):
        print("Argent :", self.__solde, "euro")

    #versement sur compte
    def versement(self, ajout):
        self.__solde += ajout
        print("Versement de", ajout, "euro")
        self.afficherSolde()

    #retrait d'argent
    def retrait(self, ajout):
        if self.__solde >= ajout or self.__decouvert_autorise:
            self.__solde -= ajout
            print("RETRAIT DE :", ajout, "euro")
            self.afficherSolde()
        else:
            print("Opération impossible, solde insuffisant.")

#partie pour l'affichage
acc = CompteBancaire("00000000", "Mr", "XXX", 1000, True)

acc.afficher()
acc.afficherSolde()
acc.versement(50)
acc.retrait(20)
acc.retrait(5)
