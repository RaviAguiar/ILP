n = int(input('Digite um número inteiro positivo: '))
while n <= 0:
    print('\nNúmero inválido.')
    n = int(input('Digite um número inteiro positivo: '))

for i in range(1, n + 1):
    if i % 14 == 0:
        print(i)