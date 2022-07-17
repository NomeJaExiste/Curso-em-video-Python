from custominput import digite, opção
numeros = list()
while True:
    numeros.append(digite())
    cont = opção('Quer continuar? [S/N] ')
    if cont == 'N':
        break
print('-=-'*20)
print(f'Foram digitados {len(numeros)} números')
print(f'A lista ordenada de forma decrescente {sorted(numeros, reverse=True)}')
print(f'O valor 5 está na lista' if 5 in numeros else 'O valor 5 não está na lista')