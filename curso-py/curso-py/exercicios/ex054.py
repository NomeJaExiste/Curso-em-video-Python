from datetime import date
menores = 0
maiores = 0
for c in range(0,7):
    nasc = int(input(f'Ano de nascimento da {c+1}ª pessoa: '))
    ano = date.today().year
    idade = ano - nasc
    if idade < 21:
        menores += 1
    else:
        maiores += 1
print(f'Nessa familia há {menores} menores e {maiores} maiores de idade')
