from ex097 import escreva
from time import sleep
from cores import pcolorir

def ajuda():
    while True:
        pcolorir('verde')
        escreva('SISTEMA DE AJUDA PYHELP')
        pcolorir()
        cont = input('Função ou Biblioteca > ')
        if cont.upper() == 'FIM':
            break
        pcolorir('azul')
        escreva(f'Acessando o manual do comando "{cont}"')
        sleep(1)
        pcolorir()
        pcolorir('pb ')
        help(cont)
        pcolorir()
        sleep(1)
    pcolorir('vermelho')
    escreva('Até logo')
    pcolorir()

ajuda()