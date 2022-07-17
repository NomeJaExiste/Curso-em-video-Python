pessoas = []
dados = {}
media = 0
while True: 
    dados['Nome'] = input('Nome: ')
    while True:
        sexo = input('Sexo [F/M]: ').strip().upper()[0]
        if sexo in 'JFM':
            break
        print('ERRO: Por favor, digite apenas M ou F ou J.')
    dados['Sexo'] = sexo
    dados['Idade'] = int(input('Idade: '))
    pessoas.append(dados.copy())
    dados.clear()
    while True:
        cont = input('Quer continuar? [S/N]: ')
        if cont in 'nNsS':
            break
        else:
            print('ERRO: Responda S ou N.')
    if cont in 'Nn':
        break
for p in pessoas:
    media += p['Idade']
media /= len(pessoas)
print('-=-'*20)
print(f'- Foram cadastradas {len(pessoas)} pessoas.')
print(f'- A média de idade é de {media:.1f} anos. ')
print(f'- As mulheres cadastradas foram: ', end='')
for mulheres in pessoas:
    if mulheres['Sexo'] == 'F':
        print(f'{mulheres["Nome"]}', end=', ' if pessoas.index(mulheres) < len(pessoas)-1 else f'\n')
print('- Lista de pessoas que estão acima da média: \n')
for p in pessoas:
    if p["Idade"] > media:
        for k, i in p.items():
            print(f'{k} = {i}', end=' ;')
        print('\n')
print('<< ENCERRANDO >>')
 