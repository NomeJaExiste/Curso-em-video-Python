jogador = {'nome':'', 'gols':[], 'total':0}
jogador['nome'] = input('Nome do jogador: ')
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, partidas):
    gols = int(input(f'Quantos gols na partida {c}? '))
    jogador['gols'].append(gols)
    jogador['total'] += gols
print('-=-'*20)
print(jogador)
print('-=-'*20)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=-'*30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i, c in enumerate(jogador['gols']):
    print(f'    => Na partida {i}, fez {c} gols.')
print(f'Foi um total de {jogador["total"]} gols.')