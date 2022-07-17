from lib.interface import *

def arqExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArq(__nome):
    try:
        a = open(__nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo')
    else:
        print(f'Arquivo {__nome} criado com sucesso')


def leiaArq(__nome):
    try:
        a = open(__nome, 'rt')
    except:
        print('Erro ao abrir o arquivo')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        print(a.read())
    