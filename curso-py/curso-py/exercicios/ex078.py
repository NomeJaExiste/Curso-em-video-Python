from modulos.custominput import intut
num = list()
for c in range(0, 5):
    num.append(intut(f'Digite um valor para a posição {c}: '))
print('-=-'*20)
print(f'Números digitados {num}')
print(f'Maior valor foi {max(num)} nas posições ', end='')
for pos, c in enumerate(num):
    if c == max(num):
        print(pos, end='... ')
print(f'\nMenor valor foi {min(num)} nas posições ', end='')
for pos, c in enumerate(num):
    if c == min(num):
        print(pos, end='... ')