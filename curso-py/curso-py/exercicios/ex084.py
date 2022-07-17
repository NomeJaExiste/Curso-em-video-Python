from modulos.custominput import opção, flut


pessoas = list()
dados = list()
pesadas = list()
leves = list()
maior = menor = 0
while True:
    dados.append(input('Nome: '))
    dados.append(flut('Peso: '))
    pessoas.append(dados[:])
    dados.clear()
    cont = opção('Quer continuar? [S/N] ')
    if cont == 'N':
        break
for c, p in enumerate(pessoas):
    if c == 0:
        maior = menor = p[1]
    else:
        if p[1] > maior:
            maior = p[1]
        elif p[1] < menor:
            menor = p[1]
for p in pessoas:
    if p[1] == maior:
        pesadas.append(p[0])
    if p[1] == menor:
        leves.append(p[0])
print('-=-'*20)
print(f'Tivemos {len(pessoas)} pessoas cadastradas')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in pesadas:
    print(f'[{p}]', end=' ')
print(f'\nO menor peso foi de {menor}Kg. Peso de ', end='')
for p in leves:
    print(f'[{p}]', end=' ')