import math

a=1
b=5
c=6

if b**2 - 4*a*c > 0:
    x1= (-b + math.sqrt(b**2 - 4*a*c))/ 2*a
    x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / 2*a
    print(f"Il y a deux solitions possibles : {x1} et {x2}")
if b**2 - 4*a*c == 0:
    x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
    print(f"Il y a une seule solition (racine double) : {x1}")
if b**2 - 4*a*c < 0:
    print("Il n'y a pas de solution réelle pour ces valeurs de a, b et c.")

