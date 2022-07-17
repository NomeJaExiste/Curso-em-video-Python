from time import sleep


def lin():
    print('-=-'*20)



def contador(inicio, fim, passo):
    lin()
    if passo < 0:
        passo *= -1 
    if passo == 0:
        passo = 1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo} ')
    if inicio < fim:
        for c in range(inicio, fim+1, passo):
            print(c, end=', ' if c < fim else '\n', flush=True)
            sleep(0.5)
    elif inicio > fim:
        for c in range(inicio, fim-1, (passo*(-1))):
            print(c, end=', ' if c > fim else '\n', flush=True)
            sleep(0.5)


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
contador(int(input('Inicio: ')), int(input('Fim: ')), int(input('Passo: ')))
