def aula19():
    '''pessoas = {'nome':'Gustavo', 'sexo':'M', 'idade':'22'}
    print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos ')
    pessoas['peso'] = 98.5
    for k, v  in pessoas.items():
        print(f'{k} = {v}')
 #
    brasil = []
    estado1 = {'uf':'Rio de Janeiro', 'sigla':'RJ'}
    estado2 = {'uf': 'São Paulo', 'sigla':'SP'}
    brasil.append(estado1)
    brasil.append(estado2)

    print(brasil[1]['sigla'])'''

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla do estado: ')
    brasil.append(estado.copy())
for e in brasil:
    for  v in e.values():
        print(v, end=' ')
    print()