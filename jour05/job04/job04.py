#liste modifiable
L = [1, 2, 3]

#mon programme
def cala(L):
    #calcul machine
    if len(L) == 1:
        return L[0]
    else:
        return max(L[0], cala(L[1:]))

#affichage
result = cala(L)
print("Le chiffre le + grand de la liste est : ", result)
