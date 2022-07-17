s = c = n = 0
tru = True
while tru:
    print('-=-'*13)
    n = int(input('Digite um número inteiro [999 para parar]: '))
    if n != 999:
        s += n
        c += 1
    else:
        tru = False
print(f'''{"="*39}
Ao todo foram digitados {c} números.
A soma entre todos eles é {s}''')