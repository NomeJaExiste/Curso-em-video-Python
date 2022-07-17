from custominput import digi, opção
num = list()
while True:
    n = digi()
    if n not in num:
        print('Valor adicionado com sucesso')
        num.append(n)
    else:
        print('Número já adicionado.')
    cont = opção('Quer continuar? [S/N] ')
    if cont in 'N':
        break
print('-=-'*20)
print(f'Você digitou os valores {sorted(num)}')
