from random import randint
v = 0
while True:
    pc = randint(0, 10)
    while True:
        h = input('Par ou ímpar? ').strip().upper()[0]
        if h in 'PI':
            break
    nh = int(input('Escolha um número: '))
    s = nh+pc
    print(f"""{'=-='*11}
Computador jogou {pc}
Jogador jogou {nh}
{'=-='*11}""")
    print('par' if s % 2 == 0 else 'ímpar')
    if s % 2 == 0 and h in 'Pp' or s % 2 == 1 and h in 'Ii':
        print('Jogador venceu')
        v += 1
    else:
        print('Jogador perdeu')
        break
print(f'Jogador perdeu após {v} vitórias consecutivas')
