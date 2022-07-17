import math
num = int(input('Digite um número inteiro: '))
op = int(input('''---------------------
Escolha a opção
- 1 para \033[7mbinário\033[m
- 2 para\033[31m otcal \033[m
- 3 para\033[36m hexadecimal \033[m
---------------------
'''))

if op == 1:
    print(f'{num} convertido para binário {bin(num)[2:]}')
elif op == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')
elif op == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')
else:
    print('digite uma opção válida')