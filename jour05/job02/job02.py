#Question : pourquoi utilisé la récursivité alors qu'on peux faire + simple ?

#fonction de mon programme
def calcul(a, b):
    #partie calcul (aide chatgpt)
    if b == 0:
        return 1
    elif b % 2 == 0:
        p = calcul(a, b/2)
        return p * p
    else:
        return a * calcul(a, b-1)

#mes inputs a et b
a = float(input("Nombre à calculer : "))
b = int(input("Votre puissance en nombre ENTIER : "))

#affichage + result
result = calcul(a, b)
print(a, "à la puissance", b, "=", result)

