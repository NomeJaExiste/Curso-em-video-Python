palavras = ('hola','me', 'llamo', 'gustavo',
            'guacamole', 'i', 'soy', 'su',
            'professor', 'hasta', 'mañana')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos', end=' ')
    for letra in p:
        if letra.lower() in 'aiueoáíúéóâêîûêôãõñàìùèòäïüëö':
            print(letra, end=' ')