from datetime import date
nascimento = int(input('Digite o ano em que você nasceu: '))
ano = date.today().year
alistamento = nascimento + 18
idade = ano - nascimento
print(f'Quem nasceu em {nascimento} tem {idade} anos em {ano}')
if idade < 18:
    print(f'Ainda faltam {18-idade} anos para seu alistamento')
    print(f'Seu alistamento será em {alistamento}')
elif idade == 18:
    print('Está na hora de você se alistar')
else:
    print(f'Você já deveria ter se alistado há {idade-18}')
    print(f'Seu alistamento foi em {alistamento}')
    