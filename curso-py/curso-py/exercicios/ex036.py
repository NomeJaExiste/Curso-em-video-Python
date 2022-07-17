vcasa = float(input('Valor da casa: R$'))
vsal = float(input('Valor do salário: R$'))
ano = int(input('Em quantos anos vai pagar: '))
parcelas = ano*12
pres = vcasa / parcelas
print(f'Para pagar uma casa de {vcasa} em {ano} anos')
print(f'a prestação será de R${pres:.2f}')
if pres > (0.3*vsal):
    print('Seu empréstimo foi\033[31m NEGADO\033[m')
else:
    print(f'Seu empréstimo foi\033[32m APROVADO\033[m')