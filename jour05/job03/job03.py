#ma fonction
def maChaine(entree):
    #vérif de l'entrée
    if entree == '':
        return 0
    else:
        return 1 + maChaine(entree[1:])

#mon entrée utilisateur
entree = input("Entrée : ")

#affichage + prise en compte entrée
carac = maChaine(entree)
print("Il y'a", carac, "caractère(s)")
