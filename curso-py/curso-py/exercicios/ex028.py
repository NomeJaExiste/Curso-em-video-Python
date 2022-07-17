import random
from time import sleep

n = random.randint(0, 5)
vidas = 3

while vidas != 0:
    tentativa = int(input('Adivinhe o número entre 0 e 5: '))
    print('processando...')
    sleep(2)
    if n == tentativa:
        print('Você acertou!!!')
        break
    elif n > tentativa:
        print('O número é maior')
    else:
        print('O número é menor')
    vidas = vidas-1
if vidas == 0:
    print(f'Computador Venceu e pensou em {n}')