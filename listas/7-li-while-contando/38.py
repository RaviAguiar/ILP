n = 0
while n <= 0:
    n = int(input('Digite um número inteiro e positivo: '))

x = 0
maior = x
menor = x

for i in range(1, n + 1):
    x = int(input('Digite um número: '))
    if x > maior:
        maior = x
    if x < menor:
        menor = x

print(f'O menor número é {menor}')
print(f'O maior número é {maior}')