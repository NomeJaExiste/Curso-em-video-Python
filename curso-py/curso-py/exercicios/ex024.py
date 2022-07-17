cidade = input('Digite o nome da sua cidade: ').strip().lower()
tes = 'Santo' in cidade.split()[0]
print(f'Essa cidade começa com santo? {tes}')