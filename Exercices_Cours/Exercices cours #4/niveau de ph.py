from logging.config import valid_ident


def niveau_de_ph(x) :
    if x > 7:
        return "Base"
    elif x == 7:
        return "Neutre"
    elif x < 7 and x > 0:
        return "Acide"
    else:
        return "Erreur"

print(f"Une solution avec un Ph de 5 est : {niveau_de_ph(5)}")
print(f"Une solution avec un Ph de 7 est : {niveau_de_ph(7)}")
print(f"Une solution avec un Ph de 10 est : {niveau_de_ph(10)}")
print(f"Une solution avec un Ph de -1 est : {niveau_de_ph(-1)}")