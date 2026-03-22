import math

def quadratic_equation(a, b, c):
    if b**2 - 4*a*c > 0:
        x1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
        x2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
        return f"Il y 2 deux solutions possibles :{x1} et {x2}"
    if b**2 - 4*a*c == 0:
        reponse = (-b/(2*a))
        return f"Il y une seule solution :{reponse}"
    else:
        return "Il n'y a pas de solution réelle pour ces valeurs de a, b et c."


print(quadratic_equation(1, 6, 9))