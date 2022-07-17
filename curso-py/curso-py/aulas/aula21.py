def fact(num =1):
    '''Return the factorial of a given number'''
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
if par(num):
    print('É par')
else:
    print('Não é par')
    