n = int(input('Digite a quantidade de pares: '))
while n <= 0:
    print('\nValor inválido')
    n = int(input('Digite a quantidade de pares: '))

for i in range(n):
    a = int(input('Digite o valor do primeiro número: '))
    b = int(input('Digite o valor do segundo número: '))
    print(f'Soma: {a + b}')
    print(f'Diferença: {a - b}')
    if a == b:
        print(f'Os números digitados são iguais')