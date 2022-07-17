nome = input('Qual é seu nome: ')
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Cláudio Jéssica Juliana Ariel':
    print('Belo nome feminino')
print(f'Tenha um bom dia {nome}!')