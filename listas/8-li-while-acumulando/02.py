n = int(input('Digite um número: '))
while n <= 0:
    n = int(input('Digite um número válido: '))

soma = 0
for i in range(1, n+ 1):
    soma += i

print(soma)