nome = input('Digite seu nome completo: ').strip().split()
print(f'''
Primeiro nome: {nome[0]}
Ultimo nome: {nome[len(nome)-1]}
''')