from custominput import flut, opção
tot = mil = bpreço =  c = 0
barato = ''
while True:
    print('-'*30)
    print(F"{'LOJA SUPER BARATÃO':^30}")
    print('-'*30)
    nome = input('Nome do produto: ').strip()
    preço = flut('Valor do produto: R$')
    tot += preço
    c += 1
    if c == 1 or preço < bpreço:
        barato = nome
        bpreço = preço
    if preço > 1000:
        mil += 1
    while True:
        cont = opção('Quer continuar? ')
        if cont in 'SsNn':
            break
    if cont in 'Nn':
        break
print(f'''{" FIM DO PROGRAMA ":-^33}
Total gasto {tot}
{mil} produtos custaram mais de 1000 reais
{barato} foi o produto mais barato custando R${bpreço:.2f}''')