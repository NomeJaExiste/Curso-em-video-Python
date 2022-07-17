import random
from time import sleep


def sorteio(list):
    list.clear()
    for c in range(0, 5):
        list.append(random.randint(1, 10))
    print('Sorteando os 5 valores da lista: ', end='')
    for i in numeros:
        print(i, end=' ', flush=True)
        sleep(0.5)
    print('PRONTO!')


def somaPar(list):
    spar =0
    for i in list:
        if i % 2 ==0:
            spar += i
    print(f'Somando os valores pares de {list} temos {spar}')


numeros = []
sorteio(numeros)
somaPar(numeros)
