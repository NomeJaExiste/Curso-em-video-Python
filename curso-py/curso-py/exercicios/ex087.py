matrix = [[],[],[]]
sp = 0
for p in range(0, 3):
    for p1 in range(0, 3):
        n = int(input(f'Digite um valor para [{p}, {p1}]: '))
        if n % 2 ==0:
            sp+=n
        matrix[p].append(n)
print('-=-'*20)
for c in range(0, 3):
    for p in matrix[c]:
         print(f'[{p:^5}]', end=' ')
    print()
print('-=-'*20)
stc = matrix[0][2] + matrix[1][2] + matrix[2][2]
print(f'A soma de todos os valores pares digitados é {sp}')
print(f'A soma dos valores da terceira coluna é {stc}.')
print(f'O maior valor da segunda linha é {max(matrix[1])}.')
