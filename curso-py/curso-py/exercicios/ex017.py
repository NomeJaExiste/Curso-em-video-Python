from math import hypot
c1 = float(input('Cateto 1: '))
c2 = float(input('Cateto 2: '))
h = hypot(c1, c2)
print(f'{h:.2f}')