lojão = ('Lápis', 1.75,
        'Borracha', 2,
        'Caderno', 15.9,
        'Transferidor', 4.20,
        'Compasso', 9.99,
        'Mochila', 120.32,
        'Canetas', 22.30,
        'Livro', 34.9)
c =0
print('-'*44)
print(f'{"LISTAGEM DE PREÇOS":^44}')
print('-'*44)
while c < len(lojão):
    print(f'{lojão[c]:.<35}', end='')
    c +=1 
    print(f'R${lojão[c]:7.2f}')
    c += 1
print('-'*44)