s=input("Saisir un montant : ")
print("Billets :")
print(f"{int(float(s)/100)} x 100$")
print(f"{int(((float(s)%100)/50))} x 50$")
print(f"{int(float(((float(s)%100)%50))/20)} x 20$")
print(f"{int(float(float(((float(s)%100)%50))%20)/10)} x 10$")
print(f"{int(float(float(float(((float(s)%100)%50))%20)%10)/5)} x 5$")
print(f" Reste{int(float(float(float(((float(s)%100)%50))%20)%10)/5)} x 5$")


