birthday = {'Alice':'Aprl 1', 'Bob':'Dec 12', 'Carol':'Mar14'}

while True:
    name = input('Enter a name: (blank to quit) ')
    if name == '':
        break

    if name in birthday:
        print(f'{birthday[name]} is the birthday of {name}')
    else:
        print(f"I don't have birthday information for {name}")
        bday = input('What is their birthday? ')
        birthday[name] = bday
        print('Birthday datavase updated.')