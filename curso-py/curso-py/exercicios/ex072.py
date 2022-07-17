from custominput import intut
numeros =('zero', 'um', 'dois', 'três', 'quatro',
         'cinco', 'seis', 'sete', 'oito', 'nove',
         'dez', 'onze', 'doze', 'vinicciustreze',
         'catorze', 'quinze', 'dezesseis', 
         'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        n = intut('Digite um número entre 0 e 20: ')
        if n in range(0, 21):
            break
        else:
            print('Tente novamente.', end=' ')
    print(f'Você digitou o número {numeros[n]}')
    while True:
        cont = input('Quer continuar? [S/N] ').strip().upper()[0]
        if cont in 'SN':
            break
    if cont in 'N':
        break