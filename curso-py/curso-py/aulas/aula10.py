n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1+n2)/2

print(f'A sua média foi {m:.1f}')

if m >= 6:
    print('Sua média foi boa!')
else:
    print('Sua média foi ruim.')