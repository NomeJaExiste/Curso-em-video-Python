def notas(*__nota, sit=False):
    '''notas(*__nota, sit=False)
    
    Retorna um dicionário com várias informações sobre a situação da turma.
    
    Palavras chave opcionais:
        sit: Indica se deve ou não mostrar a situação'''
    boletim = {}
    boletim['Total'] = sum(__nota)
    boletim['Maior'] = max(__nota)
    boletim['Menor'] = min(__nota)
    boletim['Média'] = sum(__nota)/len(__nota)
    if sit:
        if boletim['Média'] < 5:
            boletim['Situação'] = 'RUIM'
        elif boletim['Média'] < 7:
            boletim['Situação'] = 'RAZOÁVEL'
        else:
            boletim['Situação'] = 'BOA'
    return boletim


n = notas(3.5, 1.5, 10, 6.5, 7, 4, sit=True)
print(n)