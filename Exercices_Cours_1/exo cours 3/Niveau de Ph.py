def niveau_du_ph(x):
    if x <= 6:
        return "acide"
    if x == 7:
        return "neutre"
    if x >= 8:
        return "basique"

print(f"Une solution avec un Ph de 5 est : {niveau_du_ph(5)}")
print(f"Une solution avec un Ph de 7 est : {niveau_du_ph(7)}")
print(f"Une solution avec un Ph de 10 est : {niveau_du_ph(10)}")
