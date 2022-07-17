'''r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = input('Quer continuar? [S/N] ').upper()
print('FIM')'''
par = 0
impar = 0
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} números ímpares.')