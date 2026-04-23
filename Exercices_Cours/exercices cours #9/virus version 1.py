virus = ["Virus-T", "Virus-C", "Virus-G", "Uroboros", "caca"]
caracteristiques = [
    "Transforme les humains en zombies et armes biologiques",
    "Provoque des mutations extrêmes et régénère les tissus",
    "Cause des mutations incontrôlables avec régénération cellulaire rapide",
    "Consomme les organismes incompatibles et renforce les hôtes compatibles", "y pue" ]

if len(virus)>0:
    print(f"Liste des {len(virus)} virus:")
    for i in range(len(virus)):
        print(f"{virus[i]} - {caracteristiques[i]}")
else:
    print("Désolé aucun produit pharmaceutique mortel disponible")
