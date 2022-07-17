import random, time
escolhas = ['pedra', 'papel', 'tesoura']
pptbot = random.choice(escolhas)
ppth = input('Pedra papel tesoura! ').strip().lower()
time.sleep(0.5)
print('JO')
time.sleep(0.5)
print('KEN')
time.sleep(0.5)
print('PO!!!')
time.sleep(0.5)
print(f'''{"-=-"*8}
Computador jogou {pptbot.capitalize()}
Jogador jogou {ppth.capitalize()}
{"-=-"*8}''')
if pptbot == ppth:
    print('Empate')
elif (pptbot == 'tesoura' and ppth == 'pedra') or (pptbot == 'pedra' and ppth == 'papel') or (pptbot == 'papel' and ppth == 'tesoura'):
    print('Jogador venceu')
elif ppth in escolhas:
    print('Jogador perdeu')
else:
    print('Jogada inválida')