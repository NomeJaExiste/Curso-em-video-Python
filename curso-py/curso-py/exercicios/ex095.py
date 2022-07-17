from  modulo.custominput import continuar
jogadores = []
while True:
    jogador = {'nome':'', 'gols':[], 'total':0}
    jogador['nome'] = input('Nome do jogador: ')
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, partidas):
        gols = int(input(f'Quantos gols na partida {c}? '))
        jogador['gols'].append(gols)
        jogador['total'] += gols
    jogadores.append(jogador.copy())
    jogador.clear()
    cont = continuar()
    if cont == 'N':
        break
print('-=-'*20)
print(f'cod {"nome":<15}{"gols":<15}{"total":<6}')
print('-'*36)
for c, j in enumerate(jogadores):
    print(f'{c:>3} {j["nome"]:<15}{str(j["gols"]):<15}{j["total"]}')
while True:
    print('-'*36)
    n = int(input('Mostrar os dados de quem? (999 pra parar) '))
    if n == 999:
        break
    if n >= len(jogadores):
        print(f'ERRO! Não existe jogador com o código {n}! Tente novamente')
        continue
    print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[n]["nome"]}: ')
    for i, g in enumerate(jogadores[n]["gols"]):
        print(f'No jogo {i} fez {g} gols')
print('<< VOLTE SEMPRE >>')
