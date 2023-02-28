# je crée ma classe opération
class Operation:

    # self sert à initaliser les valeurs de nombre 1 et 2
    def __init__(self, nombre1=12, nombre2=3):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    # création de la méthode addition
    def addition(self):
        # notre variable de calcul
        result = self.nombre1 + self.nombre2
        # afficher le resultat
        print(result)


# on crée l'objet de notre classe Operation + on initialise nb1 et 2 avec nos valeurs
operation = Operation(nombre1=5, nombre2=3)

# ici on appelle notre addition à s'effectuer
operation.addition()