print('1 - Somar dois números')
print('2 - Subtrair dois números')
print('3 - Sair')
escolha = 0
while escolha != 3:
    while escolha != 1 or 2 or 3:
        escolha = input('Escolha a opção desejada: ')

    if escolha == 1:
