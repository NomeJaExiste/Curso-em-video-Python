n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1+n2)/2

print(f'Sua média foi {m}')
if m < 5:
    print('Você foi \033[31mREPROVADO\033[m')
elif m < 6.9:
    print('Você está de \033[33mRECUPERAÇÃO\033[m')
else:
    print('Você foi \033[32mAPROVADO\033[m')