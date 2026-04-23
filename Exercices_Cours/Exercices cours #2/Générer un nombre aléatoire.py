import random

from torch.cuda.nvtx import range_start

x=input("Nombre le plus bas : ")
y=input("Nombre le plus haut : ")
print()
z=random.randint(int(x), int(y))
print(f"Résultat de lance : {z}")

