precedent = 0
preprecedent = 1


for _ in range(100):
    nombre = precedent + preprecedent
    print(nombre)
    preprecedent = precedent
    precedent = nombre

