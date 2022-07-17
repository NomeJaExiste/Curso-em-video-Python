from lib.interface import *
from lib.arquivo import *
from lib.cores import colorir
from time import sleep

arq = 'cursoemvideo.txt'

if not arqExiste(arq):
    criarArq(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar pessoas', 'Sair'])
    if resposta == 1:
        #Opção de listar o conteúdo de um arquivo
        leiaArq(arq)
    elif resposta == 2:
        print('Opção 2')
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print(colorir('ERRO. Digite uma opção válida!'))
    sleep(2)


