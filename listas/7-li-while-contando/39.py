print('1 - Somar dois números')
print('2 - Subtrair dois números')
print('3 - Sair')

escolha = 0
n1 = 0.0
n2 = 0.0

while escolha != 3:
    while escolha not in [1, 2, 3]:
        escolha = int(input('Escolha a opção desejada: '))

    if escolha == 1:
        while not isinstance(n1, int):
            n1 = int(input('Digite o primeiro número: '))
        
        while not isinstance(n2, int):
            n2 = int(input('Digite o segundo número: '))

        print(f'{n1} + {n2} = {n1 + n2}')
        escolha = 0

    elif escolha == 2:
        while not isinstance(n1, int):
            n1 = int(input('Digite o primeiro número: '))
        
        while not isinstance(n2, int):
            n2 = int(input('Digite o segundo número: '))

        print(f'{n1} - {n2} = {n1 - n2}')
        escolha = 0
    
    print('')
    print('1 - Somar dois números')
    print('2 - Subtrair dois números')
    print('3 - Sair')

print('Programa finalizado')