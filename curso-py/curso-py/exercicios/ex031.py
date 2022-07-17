d = float(input('Distância percorrida: '))
#if d <=200:
   # print(f'Sua passagem vale: {d*0.5:.2f}')
#else:
    #print(f'Sua passagem vale: {d*0.45:.2f}')

print(f'Sua passagem vale: R${d*0.5:.2f}') if d<= 200 else print(f'Sua passagem vale: R${d*0.45:.2f}')