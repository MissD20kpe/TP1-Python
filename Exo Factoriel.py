n = int(input("Entrer un nombre :"))

# Factoriel d'un nombre
# Solution 1 avec utilisation de la boucle for
def factoriel(n):
    resultat = 1
    for i in range(1, n + 1):
        resultat *= i
    return resultat

# Solution 2 avec utilisation de la boucle while
def Factoriel(n):
    resultat = 1
    compteur = 1
    while compteur <= n:
        resultat *= compteur
        compteur += 1
    return resultat

print(f"Factoriel de {n} avec la boucle for : {factoriel(n)}")
print(f"Factoriel de {n} avec la boucle while : {Factoriel(n)}")

# Afficher mon nom ou prénom ou nom et prénom si n est multiple (3,5)
nom= "CODJOGAN "
prenom= "Samia "

if 1 <= n <=50:
    if n % 3 == 0 and n % 5 == 0:
        print(f"{nom}{prenom}")
    elif n % 3 == 0:
        print(nom)
    elif n % 5 == 0:
        print(prenom)
    else:
        print(f"{n} n'est pas multiple de 3 ou 5.")
else:
    print("Veuiller entrer un entier entre 1 et 50")
   



