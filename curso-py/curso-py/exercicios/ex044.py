print(f'{"LOJAS GUANABARA":=^40}')
valor = float(input('Valor do produto: R$'))
pagamento = input('''Escolha a forma de pagamento
[d] para dinheiro/cheque
[c] para cartão
Sua opção: ''').strip().lower()
if pagamento == 'd':
    desconto = valor - (valor*0.1)
    print(f'Sua compra de {valor} vai custar R${desconto:.2f}')
elif pagamento == 'c':
    parcelas = int(input('Quantidade de parcelas (1 para à vista): '))
    if parcelas == 1:
        desconto = valor - (valor*0.05)
    elif parcelas == 2:
        desconto = valor
        print(f'Você vai pagar em 2x de R${desconto/parcelas:.2f}')
    else:
        desconto = valor+(valor*0.2)
        print(f'Você vai pagar em {parcelas}x de R${desconto/parcelas:.2f} com 20% de JUROS')
    print(f'Valor final R${desconto:.2f}')
else:
    print('Escolha uma forma de pagamento válida')
