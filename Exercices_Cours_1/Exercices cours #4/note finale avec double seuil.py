
note_tp1=(input("Note TP1 (20% sur 10 pts) : "))
note_tp2=(input("Note TP2 (30% sur 10 pts) : "))
examen_1=(input("Note examen #1 (20% sur 100 pts) : "))
examen_2=(input("Note examen #2 (30% sur 100 pts) : "))

note_tp1=float(note_tp1)
note_tp2=float(note_tp2)
examen_1=float(examen_1)
examen_2=float(examen_2)

def note(note_tp1 , note_tp2 , examen_1 , examen_2):
    note_tp=note_tp1*2+note_tp2*3
    note_exam=examen_1*0.2+examen_2*0.3
    if note_tp>note_exam and note_exam<30:
        note_finale=2*note_exam
        print(f"Échec, double seuil non atteint. La note finale est donc de : {note_finale}")
    elif note_tp<note_exam and note_tp<30:
        note_finale=2*note_tp
        print(f"Échec, double seuil non atteint. La note finale est donc de : {note_finale}")
    else:
        note_finale=note_tp+note_exam
        print(f"La note finale est : {note_finale} %")


note(note_tp1 , note_tp2 , examen_1 , examen_2)