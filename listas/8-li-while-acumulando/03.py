n = int(input('Digite um número entre 1 e 10: '))
while not 1 <= n <= 10:
    n = int(input('Digite um número válido: '))

for i in range(1, 11):
    print(f'{n} x {i} = {n * i}')