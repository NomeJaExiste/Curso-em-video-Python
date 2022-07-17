n = int(input('Digite um número: '))
print(f'''
unidade: {n//1%10}
dezena: {n//10%10}
centena: {n//100%10}
milhar: {n//1000%10}
''')