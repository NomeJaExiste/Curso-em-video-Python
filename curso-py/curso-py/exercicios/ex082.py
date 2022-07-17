from custominput import digite, opção
num = list()
while True:
    n = digite()
    num.append(n)
    cont = opção('Quer continuar? [S/N]')
    if cont == 'N':
        print('-=-'*20)
        break
par = []
imp = par[:]
for i in num:
    if i % 2 == 0:
        par.append(i)
    else:
        imp.append(i)
print(f'Lista dos números {num}')
print(f'Lista dos números pares {par}')
print(f'Lista dos números ímpares {imp}')
