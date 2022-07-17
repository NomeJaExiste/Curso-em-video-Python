from custominput import opção, flut, intut
alunos = []
c = 0
while True:
    alunos.append([[], [], []])
    alunos[c][0].append(input('Nome: '))
    alunos[c][1].append(flut('Nota 1: '))
    alunos[c][1].append(flut('Nota 2: '))
    m = (alunos[c][1][0] + alunos[c][1][1])/2
    alunos[c][2].append(m)
    c += 1
    cont = opção('Quer continuar? [S/N] ')
    if cont == 'N':
        break
print('-=-'*25)
print('No. NOME            MÉDIA')
print('-'*30)
for i, aluno in enumerate(alunos):
    print(f'{i}   {aluno[0][0]:15} {aluno[2][0]:.1f}')
print('-'*30)
while True: 
    cont = intut('Mostrar nota de qual aluno?: (999 interrompe): ')
    print('-'*30)
    if cont != 999:
        if cont <= len(alunos)-1 and cont >= 0:
            print(f'As notas de {alunos[cont][0][0]} são {alunos[cont][1]}')
    else:
        break
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')