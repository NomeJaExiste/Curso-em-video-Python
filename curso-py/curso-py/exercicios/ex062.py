a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 1
tot = 0
mais = 10
while mais != 0:
    tot += mais
    while c <= tot:
        print(a1, end=' -> ')
        a1 += r
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos mais você quer ver? '))
print(f'Processo finalizado com {tot} termos mostrados')
