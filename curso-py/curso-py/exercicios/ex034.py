sal = float(input('Salário: R$'))
if sal < 1250:
    print(f'Seu salário será de {sal+sal*0.15:.2f}')
else:
    print(f'Seu salário será de {sal+sal*0.1:.2f}')