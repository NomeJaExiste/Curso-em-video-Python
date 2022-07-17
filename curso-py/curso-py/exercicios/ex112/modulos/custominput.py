def intut(self):
    '''retorna input convertido em int'''
    return int(input(self))

def flut(self):
    '''retorna input convertido em float'''
    return float(input(self))
    
def opção(self):
    '''retorna a primeira letra de uma string em maísculo'''
    return input(self).strip().upper()[0]

def digite():
    '''int(intput('Digite um número: '))'''
    return int(input('Digite um número: '))

def continuar():
        while True:
            cont = input('Quer continuar? [S/N] ').strip().upper()[0]
            if cont in 'SN':
                return cont
            print('ERRO: Digite apenas S ou N')

