def metade (__valor: float, form=False):
    if form:
        return f'R${__valor/2:.2f}'
    return f'{__valor/2}'


def dobro(__valor:float, form=False):
    if form:
        return f'R${__valor*2:.2f}'
    return f'{__valor*2}'


def aumentar(__valor:float, __percentage: float, form=False):
    if form:
        return f'R${__valor+(__valor*(__percentage/100)):.2f}'
    return f'{__valor+(__valor*(__percentage/100))}'


def diminuir(__valor:float, __percentage: float, form=False):
    if form:
        return f'R${__valor-(__valor*(__percentage/100)):.2f}'
    return f'{__valor-(__valor*(__percentage/100))}'


def resumo(__valor:float, __percentup: float, __percentdown: float):
    from modulos.linhas import lin
    lin(10)
    print(f'{"RESUMO DO VALOR":^30}')
    lin(10)
    print(f"{'Preço analisado:':<20}R${__valor:.2f}")
    print(f"{'Dobro do preço:':<20}{dobro(__valor, True)}")
    print(f"{'Metade do preço:':<20}{metade(__valor, True)}")
    print(f"{f'{__percentup}% de aumento:':<20}{aumentar(__valor,__percentup, True)}")
    print(f"{f'{__percentdown}% de redução:':<20}{diminuir(__valor,__percentdown, True)}")
    lin(10)
