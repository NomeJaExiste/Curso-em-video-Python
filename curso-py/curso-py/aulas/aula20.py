''' 
 # 
    def soma(a, b):
        print(f'A = {a} e B = {b} ')
        s = a + b
        print(f'A soma A + B = {s} ')


    #Programa principal
    soma(b =4, a= 5)
    soma(7, 2)
    soma(3, 9, 5) #Causa erro
 #
    def contador(*num):
        print(f'Recebi os valores {num} e são ao todo {len(num)} números. ')


    contador(2, 1, 7)
    contador(8, 0)
    contador(4, 4, 7, 8, 2)
    
 # 
    def dobra(lista):
    for pos in range(0, len(lista)):
        lista[pos] *= 2


    valores = [6, 3, 9, 1, 0, 2]
    dobra(valores)
    print(valores)
'''

def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

soma(5, 2)
soma(2, 9, 4)
