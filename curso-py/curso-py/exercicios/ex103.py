def ficha(__name: str = '<desconhecido>', __gols: int = 0):
    '''Retorna a string:
    O jogador __name fez __gols no campeonato'''
    if __name == '':
        __name = '<desconhecido>'
    if __gols == '' or not (str(__gols).isnumeric()):
        __gols = 0
    return f'o jogador {__name} fez {__gols} no campeonato. '


nom = input('Nome do Jogador: ')
gol = input('Número de gols: ')
print(ficha(nom, gol))