sexo = input('Digite seu sexo [F/M]: ').strip().upper()[0]
while sexo not in 'MmFfJj':
    sexo = input('Dados inválido, tente novamente, seu sexo [F/M]: ').strip().upper()[0]
print('Compreensivel tenha um bom dia')