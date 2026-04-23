temperatures = [23.5, 25.4, 27.6, 21.9, 26.7, 24.6]

print(f"Temperatures : {temperatures}")
x=0
final=0
for temp in temperatures:
    x+=1
print(f"nb. mesures : {x}")
for temp in temperatures:
    final+=temp
f=round(final, 2)
print(f"somme : {f}")
t = round((final/x), 2)
print(f"moyenne : {t}")
for temp in temperatures:
    min_temp=temperatures[0]
    if temp<min_temp:
        min_temp=temp
print(f"min : {min_temp}")
for temp in temperatures:
    max_temp=temperatures[0]
    if temp>max_temp:
        max_temp=temp
print(f"max : {max_temp}")

