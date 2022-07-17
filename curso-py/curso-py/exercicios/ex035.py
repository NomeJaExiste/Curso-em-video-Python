print('-=-'*9)
print('Analisador de triangulos')
print('-=-'*9)

r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))

# nunca copie e cole

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos assima podem formar um triangulo')
else:
    print('Os segmentos assima NÃO formam um triângulo.')