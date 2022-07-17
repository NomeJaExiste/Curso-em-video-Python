v = int(input('Digite o valor: '))
#print(f'{v} x 1 = {v} \n{v} x 2 = {v*2} \n{v} x 3 = {v*3} \n{v} x 4 = {v*4} \n{v} x 5 = {v*5} \n{v} x 6 = {v*6}\n{v} x 7 = {v*7}\n{v} x 8 = {v*8}\n{v} x 9 = {v*9} \n{v} x 10 = {v*10}')

print('-'*12)
t = 1
while(t<11):
    print(f'{v} x {t:2} = {v*t}')
    t = t+1
print('-'*12)