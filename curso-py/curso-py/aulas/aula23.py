try:
    a = int(input("Numerador: "))
    b = int(input('Denominador: '))
    r = a/b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados inseridos.')
except (ZeroDivisionError):
    print('Erro, não é possivel dividir um número por 0.')
except (KeyboardInterrupt):
    print('\nUsuário preferiu não informar os dados')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre')


# um mesmo try pode ter vários except