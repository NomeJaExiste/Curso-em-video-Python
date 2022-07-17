def aula17():
    '''num = [2, 5, 9, 1]
        num[2] = 3
    # Inserir um valor numa lista
        num.append(7)
    # Deixar os itens em ordem crescente
        num.sort()
    # Deixar os itens em ordem decrescente
        num.sort(reverse=True)
    # Inserir um valor numa posição especifica
        num.insert(2, 2)
    # Remover um elemento pela key (x), para remover o ultimo ()
        num.pop()
    # Remover um elemento especifico (x)
        if 4 in num:
            num.remove(4)
        else:
            print('Não achei o número 4')
        print(num)
    # Mostrar quantos elementos há numa lista
        len(num)
        print(f'Essa lista tem {len(num)} elementos.')valores = list()
    # Inserir valores numa lista com for
        for cont in range(0,5):
            valores.append(int(input('Digite um valor: ')))
    # Mostrar os itens da lista com suas respectivas posições
        for c, v in enumerate(valores):
            print(f'Na posição {c} encontrei o valor {v}.')

        print('Cheguei no final da lista.')
    # Quando uma lista é igual a outra o pyton cria uma ligação entre elas
        a = [2, 3, 4, 7]
        b = a
        # Para copiar uma lista sem ligar ela com a nova
        b = a[:]
        b[2] = 8

        print(f'lista A: {a}')
        print(f'Lista B: {b}')'''