import random

def generer_nombre():
    unite = 1
    nombre = 0
    for _ in range(3):
        chiffre_aleatoire = random.randint(1,9)
        nombre += chiffre_aleatoire * unite
        unite = unite*10

    return nombre


resultat = generer_nombre()
print(f"Nombre généré : {resultat}")