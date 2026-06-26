n = int(input('Digite a quantidade de números: '))
while n <= 0:
    n = int(input('Digite uma quantidade válida: '))

pares = 0
impares = 0
for i in range(n):
    x = int(input('Digite um número: '))
    if x % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f'Pares = {pares}')
print(f'Impares = {impares}')