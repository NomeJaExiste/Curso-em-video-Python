media = soma = maior = menor = 0
cont = 'Ss'
while cont not in 'Nn':
    n = int(input('Digite um número inteiro: '))
    if soma == 0:
        maior = menor = n
    else: 
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    soma += 1
    media += n
    cont = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if cont not in 'SsNn':
        print('Vou considerar isso como um sim')
media /= soma
print(f'''A média de todos os {soma} números é {media}
O maior número apresentado foi {maior}
O menor número apresentado foi {menor}''')