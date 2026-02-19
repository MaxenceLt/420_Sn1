def densite(masse, volume):
    if masse <= 0:
        raise ValueError("La masse doit être positive")
    if volume <= 0:
        raise ValueError("Le volume doit ètre positif")
    return masse * volume

print(densite(10, -2))

