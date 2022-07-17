print('\033[33m-=-'*9,)
print('Analisador de triângulos')
print('-=-'*9, '\033[m')

r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        tipo = 'EQUILÁTERO'
    elif r1 == r2 or r1 == r3 or r2 == r3:
        tipo = 'ISÓSCELES'
    else:
        tipo = 'ESCALENO'
    print(f'Os seguimentos podem formar um triângulo do tipo {tipo}')
else:
    print('Os segmentos NÃO podem formar um triângulo.')