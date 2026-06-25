n = int(input('Digite a quantidade de pares: '))
while n <= 0:
    n = int(input('Digite um número válido: '))

for i in range(1, n + 1):
    n1 = int(input(f'Digite o primeiro número do {i} par: '))
    n2 = int(input(f'Digite o segundo número do {i} par: '))
    if n1 == n2:
        print(f'Os dois números são iguais')
    else:
        print(f'O maior número do {i} par é: {max(n1, n2)}')
        print(f'O menor número do {i} par é: {min(n1, n2)}')
