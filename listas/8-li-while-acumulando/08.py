n = int(input('Digite um número: '))
while not n >= 1:
    n = int(input('Digite um número válido: '))

x = int(input('Digite um número: '))
menor = x
maior = x
for i in range(n - 1):
    x = int(input('Digite um número: '))
    if x > maior:
        maior = x
    elif x < menor:
        menor = x

print(f'Maior = {maior}')
print(f'Menor = {menor}')