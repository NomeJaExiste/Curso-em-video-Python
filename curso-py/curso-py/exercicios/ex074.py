from random import randint
tupla = ()
print('Os valores sorteados foram: ', end='')
for c in range (0,5):
    tupla += (randint(1,10),)
    print(tupla[c], end=' ')
ordem = sorted(tupla)
print(f'''
O menor valor sorteado foi {ordem[0]}
O maior valor sorteado foi {ordem[-1]}''')