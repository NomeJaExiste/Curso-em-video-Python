from linhas import lin
from time import sleep


def maior(*num):
    lin()
    if len(num) == 0:
        mai = 0
    print('Analisando os valores passados...')
    for i, p in enumerate(num):
        if i == 0 or p > mai:
            mai = p
        print(p, end=' ', flush=True)
        sleep(0.5)
    print(f'foram informados {len(num)} valores ao todo.')
    print(f'o maior valor informado foi {mai}. ')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
