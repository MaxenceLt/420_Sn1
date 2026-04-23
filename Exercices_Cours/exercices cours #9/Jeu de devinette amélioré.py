import random

reponse=int(input("Chiffre aléatoire entre 0 et 100 :"))
nombre_secret=random.randint(1,100)

liste=[]

while reponse != nombre_secret:
    if reponse in liste:
        print("Tu pue du bat")
    liste.append(reponse)
    if reponse>nombre_secret:
        print("Plus bas!")
        reponse=int(input("Essaie Encore :"))
    if reponse<nombre_secret:
        print("Plus haut!")
        reponse=int(input("Essaie Encore :"))
if reponse==nombre_secret:
    print("Bravo humain, vous avec trouvé le nombre!")