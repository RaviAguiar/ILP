n = True

x = 0
pares = 0
impares = 0
while n == True:
    x = float(input('Digite um número: '))
    if x < 0:
        n = False

    if x % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f'Quantidade de números pares digitados: {pares}')
print(f'Quantidade de números impares digitados: {impares}')