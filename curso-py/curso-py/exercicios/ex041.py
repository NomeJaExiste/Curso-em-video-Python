from datetime import date
ano = date.today().year
while True:
    idade = input('Ano em que você nasceu: ').strip()
    if idade.isnumeric():
        idade = ano - int(idade)
        print(f'O atleta tem {idade} anos.')
        if idade <= 9:
            clas = 'MIRIM'
        elif idade <= 14:
            clas = 'INFANTIL'
        elif idade <= 19:
            clas = 'JUNIOR'
        elif idade <= 25:
            clas ='SÊNIOR'
        else:
            clas = 'MASTER'
        print(f'Classificação: {clas}')
        break
    else:
        print('Digite um ano válido')