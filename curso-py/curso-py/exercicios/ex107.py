from modulos import moeda
from modulos.custominput import flut

p = flut('Digite o preço: R$')
print(f'A metade de {p} é {moeda.metade(p, True)}')
print(f'O dobro de {p} é {moeda.dobro(p, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13, True)}')
