from random import sample

MegaSena = sample(range(1, 61), 6)
MegaSena.sort()
for c in range(0, 6):
    print(f'[{c + 1}]: {MegaSena[c]}')