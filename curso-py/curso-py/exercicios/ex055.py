maior = 0
menor = 0
for c in range(0,5):
    peso = float(input(f'Peso da {c+1}ª pessoa: '))
    if c == 0:
        maior = peso
        menor = peso
    else: 
        if peso < menor:
            menor = peso
        if peso > maior:
            maior = peso
print(f'Maior peso: {maior}Kg\nMenor peso: {menor}Kg')