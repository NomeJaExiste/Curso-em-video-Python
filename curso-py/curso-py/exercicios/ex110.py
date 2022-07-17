from modulos import moeda
from modulos.custominput import flut


p = flut('Digite o preço: R$')
moeda.resumo(p, 80, 35)