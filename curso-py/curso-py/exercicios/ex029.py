# Radar be like

v = float(input('Velocidade do veículo: '))

if v > 80:
    print(f'Você foi multado e sua multa é de R${((v-80)*7):.2f}')
print('Compreensível, tenha um bom dia!')