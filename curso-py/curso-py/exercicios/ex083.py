frase = input('Digite uma expressão: ').replace(' ', '')
parenteses = 0
for i in frase:
    if i == '(':
        parenteses += 1
    elif i == ')':
        parenteses -= 1
    if parenteses < 0:
        break
if parenteses == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão errada!')
