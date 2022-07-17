from custominput import digi
num = list()
for c in range(0, 5):
    n = digi()
    if c == 0 or n > max(num):
        num.append(n)
        print('Adicionado ao final da lista...')
    else:
        for i in num:
            if n <= i:
                num.insert(num.index(i), n)
                print(f'Adcionado na posição {num.index(n)} da lista...')
                break
print('-=-'*24)
print(f'Os valores digitados em ordem foram {num}')