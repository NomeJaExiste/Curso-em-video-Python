a1 = float(input('Primeiro termo: '))
r = float(input('Razão: '))
c = 0
while c < 11:
    print(a1, end=' -> ')
    a1 += r
    c += 1
print('FIM')