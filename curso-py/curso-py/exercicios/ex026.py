frase = input('Digite uma frase: ').lower().strip()
print(f'''
A letra a aparece {frase.count('a')} vezes
A letra a aparece pela primeira vez na posição {frase.find('a')+1}
A letra a aparece pela ultima vez na posição {frase.rfind('a')+1}
''')