n = int(input('Quantos termos você quer ver? '))
f1 = 0
f2 = 1
c = 3
print(f'{f1} → {f2}', end=' → ')
while c <= n:
    f3 = f1 + f2
    print(f3, end=' → ')
    f1 = f2
    f2 = f3
    c += 1
print('FIM')