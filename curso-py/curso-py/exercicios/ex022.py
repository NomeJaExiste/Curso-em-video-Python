nome = input('Digite seu nome completo: ').strip()
print(f'''Seu nome em caixa alta: {nome.upper()}
Seu nome em caixa baixa: {nome.lower()}
Seu nome tem {len(''.join(nome.split()))} letras
Seu primeiro nome tem {len(nome.split()[1])} letras''')