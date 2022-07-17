def voto_impresso():
    print('='*50)
    for c in range(6):
        if c == 0:
            print(f'| [{f"URNA ELETRÔNICA":^30}]  [{"":^10}]|')
        elif c == 1:
            print('|', f'='*32," [" f'{"":10}]|')
        elif c == 2:
            print(f'{"| |":33}|  [7] [8] [9] |')
        elif c == 3:
            print(f'{"| |":33}|  [6] [5] [4] |')
        elif c ==4:
            print(f'{"| |":33}|  [3] [2] [1] |')
        else:
            print(f'| {f"="*32}  [x] [←] [↲] |')
    print('='*50)