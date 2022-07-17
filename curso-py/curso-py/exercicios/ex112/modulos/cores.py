def colorir(texto='', cor='neutro'):
    cores = {"neutro":'\033[m',
        "vm":'\033[31m',
        "az":'\033[34m',
        "am":'\033[33m',
        "pb ":'\033[7m'}
    return f"{cores[cor]}{texto}\033[m"



def pcolorir(cor='neutro'):
        '''Deixa o texto feio com o fundo: 
        vermelho, amarelo, azul, verde, roxo ou laranja'''
        cores = {"neutro":'\033[m',
                "vermelho":'\033[41m',
                "verde":'\033[42m',
                "amarelo":'\033[43m',
                "azul":'\033[44m',
                "roxo":'\033[45m',
                "pb ":'\033[7m'}
        return print(cores[cor])