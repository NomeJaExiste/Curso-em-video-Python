aluno = {}
aluno['Nome'] = input('Nome: ')
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] < 5:
    aluno['Situação'] = 'Reprovado'
elif aluno['Média'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Aprovado'
for k, v in aluno.items():
    print(f'{k} é igual a {v} ')
