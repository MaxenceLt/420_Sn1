import matplotlib.pyplot as plt

# Âge en années
# Tableau de données pour l'axe horizontal (axe des abscisses)
age = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Taille correspondante en cm (exemple fictif)
# Tableau de données pour l'axe vertical (axe des ordonnées)
taille = [50, 75, 85, 95, 105, 112, 118, 124, 130, 135, 140]

# Création du graphique
# Création d'une courbe
plt.plot(age, taille, marker='o', linestyle='-', color='g', label="Taille en fonction de l'âge")

# Ajout de titres et labels
plt.xlabel("Âge (années)")                    # Ajout d'un label sur l'axe horizontal
plt.ylabel("Taille (cm)")                     # Ajout d'un label sur l'axe vertical
plt.title("Courbe de croissance de l'enfant") # Ajout d'un titre au graphique
plt.legend()                                  # Générer une légende

# Affichage du graphique
plt.show()import matplotlib.pyplot as plt

# Âge en années
# Tableau de données pour l'axe horizontal (axe des abscisses)
age = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Taille correspondante en cm (exemple fictif)
# Tableau de données pour l'axe vertical (axe des ordonnées)
taille = [50, 75, 85, 95, 105, 112, 118, 124, 130, 135, 140]

# Création du graphique
# Création d'une courbe
plt.plot(age, taille, marker='o', linestyle='-', color='g', label="Taille en fonction de l'âge")

# Ajout de titres et labels
plt.xlabel("Âge (années)")                    # Ajout d'un label sur l'axe horizontal
plt.ylabel("Taille (cm)")                     # Ajout d'un label sur l'axe vertical
plt.title("Courbe de croissance de l'enfant") # Ajout d'un titre au graphique
plt.legend()                                  # Générer une légende

# Affichage du graphique
plt.show()