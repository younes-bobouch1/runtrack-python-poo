# je crée ma classe opération
class Operation:

    # self sert à initaliser les valeurs de nombre 1 et 2
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2


# ici je crée mon instance
operation = Operation()

# puis on l'affiche
print(operation)