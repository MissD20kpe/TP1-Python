def calcul(somme, des, face):
    c = 0
    for d1 in range(1, face + 1):
        for d2 in range(1, face + 1):
            for d3 in range(1, face + 1):
                for d4 in range(1, face + 1):
                    for d5 in range(1, face + 1):
                        if d1 + d2 + d3 + d4 + d5 == somme:
                            c += 1
    return c
somme = 20
des = 5
face = 6
resultat = calcul(somme, des, face)
print(f"Nombre de façons d'obtenir une somme de {somme} avec {des} dés : {resultat}")

