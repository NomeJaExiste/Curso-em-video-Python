from random import randint
from time import sleep
n = randint(0, 10)
tantas = 1
acertou = False
print('Advinhe um número entre 0 e 10')
while not acertou:
    tentativa = int(input('Qual o seu palpite? '))
    print('processando...')
    sleep(1.5)
    if n == tentativa:
        print('Você acertou!!!')
        acertou = True
    elif n > tentativa:
        print('O número é maior')
    else:
        print('O número é menor')
    tantas += 1
print(f'Você venceu com {tantas} tentativas')
