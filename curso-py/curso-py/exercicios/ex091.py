from random import randint
from time import sleep
from operator import itemgetter
dados = {}
print('Valores sorteados: ')
for c in range(1, 5):
    dados[f'jogador {c}'] = randint(1,6)
    print(f"    O jogador {c} tirou {dados[f'jogador {c}']}")
    sleep(0.75)
ranking = []
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
print('Ranking dos jogadores: ')
for i, j in enumerate(ranking):
    print(f'{i+1}º: {j[0]} {j[1]}. ')
    sleep(0.75)