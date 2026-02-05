nom_etudiant=(input("Étudiant : "))
note_tp1=(input("Note TP1 (20% sur 10 pts) : "))
note_tp2=(input("Note TP2 (30% sur 10 pts) : "))
examen_1=(input("Note examen #1 (20% sur 100 pts) : "))
examen_2=(input("Note examen #2 (30% sur 100 pts) : "))
print(f"Note obtenue pour ce cours : {(((float(note_tp1))*2)+((float(note_tp2))*3)+((float(examen_1))*0.2)+((float((examen_2))*0.3))):.2f}")
print("Attention, l'application de la double sanction n'a pas été réalisée!")



