#création de ma fonction
def fact(x):
    #mon calcul pour obtenir le fact' (ma récursion)
    if x == 0:
        return 1
    else:
        return x * fact(x-1)

#création de mon iput pour l'entrée utilisateur
nb = int(input("Tapez un nombre ENTIER : "))

#affichage + résultat
result = fact(nb)
print("Factorielle de", nb, "=", result)
