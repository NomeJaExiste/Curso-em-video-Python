matrix = [[],[],[]]
for p in range(0, 3):
    for p1 in range(0, 3):
        matrix[p].append(int(input(f'Digite um valor para [{p}, {p1}]: ')))
print('-=-'*20)
for c in range(0, 3):
    for p in matrix[c]:
         print(f'[{p:^5}]', end=' ')
    print()
