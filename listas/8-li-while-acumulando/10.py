# 0 1 1 2 3 5 8 13 21 34
frente = 0
meio = 1
anterior = 0
n = int(input('Digite a quantidade de números da sequência de Fibonacci: '))
while n <= 0:
    print('Digite um número válido.')
    n = int(input('Digite a quantidade de números da sequência de Fibonacci: '))

if n == 1:
    print(0)
elif n == 2:
    print('0 1')
else:
    print('0 1', end=" ")
    for i in range(3, n + 1):
        frente = anterior + meio
        print(f'{frente}', end=" ")
        anterior = meio
        meio = frente
        frente = 0