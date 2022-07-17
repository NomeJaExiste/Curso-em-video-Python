from lib.cores import colorir
from lib.linhas import lin


def leiaint(self: str):
    '''retorna um input convertido em int'''    

    while True:
        try:
            entrada = int(input(self).strip())
        except (ValueError, TypeError):
            print(f'{colorir("ERRO, digite um número inteiro válido", cor="vm")}')
            continue
        except (KeyboardInterrupt):
            print(colorir('\nUsuário decidiu não digitar o número', cor='vd'))
            return 3
        return entrada


def cabeçalho(txt):
    lin(10)
    print(txt.center(30))
    lin(10)

    
def menu(lista: list):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{colorir(f"{c}", cor="am")} - {colorir(f"{item}", cor="az")}')
        c += 1
    opc = leiaint(colorir('Sua Opção: ', cor='vd'))
    return opc



        
