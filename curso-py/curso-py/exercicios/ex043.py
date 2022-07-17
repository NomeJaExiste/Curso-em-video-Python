peso = float(input('Qual seu peso? (Kg) '))
altura = float(input('Qual sua altura? (m) '))
imc = peso / altura**2
print(f'O IMC dessa pessoa é de {imc:.1f}')
print('Você está na faixa ',end='')
if imc < 18.5:
    print('ABAIXO DO PESO')
elif imc < 25:
    print('PESO NORMAL')
elif imc < 30:
    print('SOBREPESO')
elif imc < 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MÓRBIDA')
