from datetime import date
pessoa = {}
ano = date.today().year
pessoa['nome'] = input('Nome: ')
nasc =  int(input('Ano de nascimento: '))
pessoa['idade'] = ano - nasc
pessoa['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('Salário: R$'))
    pessoa['aposentadoria'] = (pessoa['contratação'] - nasc)+35

print('-=-'*20)
for k, v in pessoa.items():
    print(f'    - {k} tem o valor {v} ')