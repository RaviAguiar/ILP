n = int(input('Digite um número: '))
while n < 0:
    n = int(input('Digite um número válido: '))

if n == int(str(n)[::-1]):
    print(f'{n} é um palíndromo')
else:
    print(f'{n} não é um palíndromo')