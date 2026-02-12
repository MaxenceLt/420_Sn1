def aire_rectangle(longueur, largeur):
    return longueur * largeur

def volume_prisme(longueur, largeur, hauteur):
    return aire_rectangle(longueur, largeur) * hauteur

print(aire_rectangle(5,3))

print(volume_prisme(5, 3, 4))

