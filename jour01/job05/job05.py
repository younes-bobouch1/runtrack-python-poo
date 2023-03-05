# ma classe Point
class Point:
    # créa attributs
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # méthode pour afficher x et y
    def afficherLesPoints(self):
        print(f"{self.x} {self.y}")

    # méthode pour afficher x
    def afficherX(self):
        print(f"X = {self.x}")

    # méthode pour afficher y
    def afficherY(self):
        print(f"Y = {self.y}")

    # méthode pour changer valeur
    def changerX(self, nv):
        self.x = nv

    # méthode pour changer valeur
    def changerY(self, nv):
        self.y = nv


# affichage
xy = Point(10, 50)
print(xy.x)
print(xy.y)
xy.afficherLesPoints()
xy.afficherX()
xy.afficherY()

# affichage valeur changé
xy.changerX(20)
xy.changerY(100)
xy.afficherLesPoints()
