temperatures = [23.5, 25.4, 27.6, 21.9, 26.7, 24.6]

print(f"Temperatures : {temperatures}")
print(f"nb. mesures : {len(temperatures)}")
print(f"somme : {sum(temperatures)}")
print(f"moyenne : {round(sum(temperatures)/len(temperatures), 2)}")
print(f"min : {min(temperatures)}")
print(f"max : {max(temperatures)}")