brasileirão = ('Palmeiras', 'Atlético-MG', 'Fortaleza', 'Bragantino',
             'Athletico-PR', 'Flamengo', 'Ceará SC', 'Fluminense',
             'Bahia', 'Santos', 'Atlético-GO', 'Corinthians',
              'Internacional', 'Juventude', 'Cuiabá', 'São Paulo',
               'Sport Recife', 'América-MG', 'Grêmio', 'Chapecoense')

print(f'''{"-=-"*13}
Lista de times do Brasileirão: {brasileirão}')
{"-=-"*35}
Os 5 primeiros times são {brasileirão[:5]}')
{"-=-"*35}
Os 4 últimos são {brasileirão[-4:]}
{"-=-"*35}
Times em ordem alfabética {sorted(brasileirão)}
{"-=-"*35}
O Chapecoense está na {brasileirão.index('Chapecoense')+1}ª posição''')
