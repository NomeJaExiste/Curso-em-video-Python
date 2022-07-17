from linhas import lin


def leiaint(self):
    while True:
        __num = input(self).strip()
        if __num.isnumeric():
            return int(__num)
        print('\033[31mERRO! Digite um número inteiro válido. \033[m')

lin()
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')