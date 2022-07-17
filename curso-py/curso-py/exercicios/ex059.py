import random, time
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro número: '))
op = 0
while op != 5:
    print(f'''{"="*30}
Números digitados {n1} e {n2}
{"="*30}
Escolha uma opção
[1] somar os números
[2] multiplicar os números
[3] verificar qual é o maior
[4] inserir novos números
[5] sair do programa    
[6] jogar jokenpo
''')
    op = int(input('Sua escolha: '))
    if op == 1:
        print(f'{"="*30}\nA soma ente {n1} e {n2} é {n1+n2}')
    elif op == 2:
        print('='*30)
        print(f'{n1} x {n2} = {n1*n2}')
    elif op == 3:
        print('='*30)
        if n1 > n2:
            print(f'O maior é {n1}')
        else:
            print(f'O maior é {n2}')
    elif op == 4:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
    elif op == 6:
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
        print(f'''{"-=-"*11}
    Computador jogou {pptbot.capitalize()}
    Jogador jogou {ppth.capitalize()}
{"-=-"*11}''')
        if pptbot == ppth:
            print('Empate')
        elif (pptbot == 'tesoura' and ppth == 'pedra') or (pptbot == 'pedra' and ppth == 'papel') or (pptbot == 'papel' and ppth == 'tesoura'):
            print('Jogador venceu')
        elif ppth in escolhas:
            print('Jogador perdeu')
        else:
            print('Jogada inválida')
    time.sleep(2)
print('FIM')