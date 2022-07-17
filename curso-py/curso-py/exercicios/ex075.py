from custominput import intut
pares =()
valores = ()
while True:
    n1 = intut('Digite um valor: ')
    if n1 % 2 == 0:
        pares += n1,
    valores += n1,
    if len(valores) == 4:
        break
print(f'Você digitou os números {valores}')
print(f'O número 9 apareceu {valores.count(9)} vezes')
print(f'O número 3 foi digitado pela primeira vez na {valores.index(3)+1}ª posição' if 3 in valores else 'O número 3 não apareceu na lista')
if len(pares) > 0:
    print(f'Os números pares digitados foram ', end='')
    for c in pares:
        print(c, end=' ')