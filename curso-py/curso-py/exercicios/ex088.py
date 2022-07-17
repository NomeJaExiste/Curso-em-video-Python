import random, time
palpites = []
print('-'*30)
print(f'{"Joga na megasena":^30}')
print('-'*30)
jogos = int(input('Quantos palpites você quer gerar? '))
for c in range(0, jogos):
    palpites.append([])
    for c1 in range(0, 6):
        while True:
            n = random.randint(1,60)
            if n not in palpites[c]:
                palpites[c].append(n)
                break
print(f'{f" SORTEANDO {jogos} JOGOS ":=^30}')
for i, c in enumerate(palpites):
    print(f'Jogo {i+1}: {sorted(c)} ')
    time.sleep(1)
print(f'{" BOA SORTE ":=^30}')
