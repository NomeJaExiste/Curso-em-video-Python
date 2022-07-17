def dinput(self):
    from modulos.cores import colorir
    while True:
        dindin = input(self).strip().replace(',','.')
        if dindin.replace('.','',1).isdigit():
            return float(dindin)
        print(f'{colorir("ERRO! "+f"{dindin}"+" é um preço inválido", cor="vm")}')