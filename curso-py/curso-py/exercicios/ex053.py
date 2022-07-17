frase = input('Frase: ').strip().lower().replace(' ', '')
esarf = frase[::-1]
if frase == esarf:
    print('A frase é um palindromo')
else:
    print('A frase NÃO é um palindromo')