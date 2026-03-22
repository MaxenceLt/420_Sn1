def densite(masse, volume):
    if masse <= 0:
        raise ValueError("La masse doit être positive")
    if volume < 0:
        raise ValueError("Le volume ne peut pas être négatif")
    if volume == 0:
        raise ZeroDivisionError("Le volume doit être strictement positif")
    return masse/volume

print(densite(2, -8))      # 5.0
print(densite(25, 5))   # 5.0
