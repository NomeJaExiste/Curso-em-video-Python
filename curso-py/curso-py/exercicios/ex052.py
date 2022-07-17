n = int(input('Digite um número inteiro: '))
p = 0
for c in range(1,n+1):
    if n%c == 0:
        print(f'\033[33m-> {c} <-', end='\033[m ')
        p += 1
    else:
        print(f'\033[36m{c}', end ='\033[m ')
print(f'\n{n} é divisivel por {p} número(s), ')
if p == 2:
    print(f'logo É PRIMO')
else:
    print(f'logo NÃO É PRIMO')
