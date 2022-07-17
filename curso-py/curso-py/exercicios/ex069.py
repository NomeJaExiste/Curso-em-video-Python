from custominput import intut, opção
sh = soma18 = msub20 = j =0
while True:
    print(f'''{"-"*33}
{"CADASTRE UMA PESSOA":^33}
{"-"*33}''')
    idade = intut('Idade: ')
    if idade >= 18:
        soma18 +=1
    while True:
        sexo = opção('Sexo: [F/M] ')
        if sexo in 'MmFfJj':
            break
    print('-'*33)
    if sexo in 'F' and idade < 20:
        msub20 += 1
    elif sexo in 'M':
        sh += 1
    elif sexo in 'J':
        j += 1
    while True:
        cont = opção('Quer continuar? [S/N] ')
        if cont in 'SsNn':
            break
    if cont in 'Nn':
        break
print(f'''
Total de pessoas com mais de 18 anos: {soma18}
Ao todo temos {sh} homens cadastrados
E temos {msub20} mulheres com menos de 20 anos
''')
print(f'E temos {j} jabutis.' if j >= 1 else '')