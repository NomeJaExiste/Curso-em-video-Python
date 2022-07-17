hvelho = 0
mnova = 0
midade = 0
for c in range(1,5):
    print(f'{f"{c}ª PESSOA":-^21}')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('''Homem ou Mulher? (H/M) ''').strip()
    if sexo in 'Mm':
        if idade > hvelho:
            hvelho = idade
            nomevelho = nome
    elif sexo in 'Ff':
        if idade < 20:
            mnova += 1
    else:
        print('\033[31m[ERRO]\033[m Escolha uma opção válida')
        break
    midade += idade
midade /= 4
print(f'''A média das idades é {midade:.1f} anos
O homem mais velho é {nomevelho} com {hvelho} anos
{mnova} mulhere(s) tem menos de 20 anos''')