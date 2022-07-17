def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        r = 'NÃO VOTA'
    elif idade < 18 or idade > 65:
        r = 'VOTO OPCIONAL'
    else:
        r = 'VOTO OBRIGATÓRIO'
    return f'Com {idade} anos: {r} '


nasc = int(input('Digite o ano de nascimento de uma pessoa: '))
1999
print(voto(nasc))
