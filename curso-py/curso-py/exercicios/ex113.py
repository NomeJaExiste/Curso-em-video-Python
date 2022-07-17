from modulos import cores

def leiaint(self: str):
    '''retorna um input convertido em int'''    

    while True:
        try:
            entrada = int(input(self).strip())
        except (ValueError, TypeError):
            print(f'{cores.colorir("ERRO, digite um número inteiro válido", cor="vm")}')
            continue
        except (KeyboardInterrupt):
            print(cores.colorir('\nUsuário decidiu não digitar o número', cor='vd'))
            return 0
        return entrada

def leiafloat(self: str):
    '''retorna um input convertido em float'''

    while True:
        
        try:
            entrada = float(input(self).strip().replace(',', '.'))
        except(ValueError, TypeError):
            print(cores.colorir(f'ERRO, digite um número real válido', cor="vm"))
            continue
        except(KeyboardInterrupt):
            print(cores.colorir('\nUsuário preferiu não digitar este número', cor='vd'))
            return 0
        return entrada


a = leiaint("Digite um número inteiro: ")
b = leiafloat("Digite um número com ponto flutuante: ")
print(f'número inteiro = {a}')
print(f'Número real = {str(b).replace(".",",")}')
