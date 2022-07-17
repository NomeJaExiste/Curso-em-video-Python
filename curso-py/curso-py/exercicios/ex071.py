from custominput import intut
print('='*33)
print(f'{"BANCO CEV":^33}')
print('='*33)
divid = 50
saque = intut('Qual valor você quer sacar? R$')
while True:
    cinquenta = saque // divid
    res = saque % divid
    if cinquenta > 0:
        print(f'Total de {cinquenta} cédulas de R${divid}')
    if res == 0:
        break
    if divid == 50:
        divid = 20
    elif divid == 20:
        divid = 10
    elif divid == 10:
        divid = 1
    saque = res
print('='*33)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')