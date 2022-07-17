n = int(input('Digite um valor: '))
fat = 1
#Com for
'''for c in range(n,0,-1):
    fat *= n
    n -= 1
print(fat)'''

#Com while
print(f'{n}! = ', end='')
while n > 0:
    fat *= n
    print(n, end='')
    print(' x ' if n > 1 else ' = ', end='')
    n -= 1
print(fat)

#Com bibliotecas
'''from math import factorial
print(factorial(n))'''