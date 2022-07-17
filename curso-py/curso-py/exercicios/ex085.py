from modulos.custominput import intut
num = [[], []]
for c in range(1, 8):
    n = intut(f'Digite o {c}º valor: ')
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)
num[0].sort()
num[1].sort()
print(f'Lista dos números pares {num[0]}')
print(f'Lista dos números ímpares {num[1]}')