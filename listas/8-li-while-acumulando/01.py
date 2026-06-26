n = int(input('Digite um número: '))
while n <= 0:
    n = int(input('Digite um número válido: '))

for i in range(n, 0, -1):
    print(i, end=" ")
print('Fogo!')