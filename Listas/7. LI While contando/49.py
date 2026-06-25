n = int(input('Digite a quantidade de valores: '))
while n <= 0:
    n = int(input('Digite um número válido: '))

numeros = []

for i in range(n):
    x = int(input('Digite um valor: '))
    numeros.append(x)

media = sum(numeros) / len(numeros)
qnam = 0 #qnam = quantidade de números abaixo da média

for numero in numeros:
    if numero < media:
        qnam += 1

print('\nResultados:')      
print(f'Soma total: {sum(numeros)}')
print(f'Média dos valores: {media}')
print(f'O maior valor é {max(numeros)}')
print(f'O menor valor é {min(numeros)}')
print(f'A quantidade de números abaixo da média é {qnam}')