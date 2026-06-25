n = int(input('Digite um número inteiro positvo: '))
while n <= 0:
    print('\nNúmero inválido.')
    n = int(input('Digite um número inteiro positivo: '))

verificador = 0
for i in range(1, n):
    if n % i == 0:
        verificador += i

if verificador == n:
    print(f'{n} é um número perfeito.')
else:
    print(f'{n} não é um número perfeito.')