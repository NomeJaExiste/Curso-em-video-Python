s = 0 #Acumulador
numeros = 0 #Contador
for c in range(1,501,2):
    if c % 3 == 0:
        s += c
        numeros += 1
print(f'A soma desses {numeros} numeros é {s}')
