while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*33)
    if n < 0:
        break
    else: 
        for c in range(1,11):
            print(f'{n} x {c:2} = {n*c}')
    print('-'*33)
print('TABUADA ENCERRADA. Volte sempre!')