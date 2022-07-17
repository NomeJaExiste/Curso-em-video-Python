from typing import SupportsInt


def fact(__x: SupportsInt, show: bool = False):
    '''Find x!.

    Optional keword argument:
        show: shows the counting process'''
    print('='*30)
    f = 1
    s = ''
    for c in range(__x, 0, -1):
            f *= c
            s += f'{c} x ' if c > 1 else f'{c} ' 
    if show:
        return f'{s}= {f}'
    else:
        return f


print(fact('5'))
