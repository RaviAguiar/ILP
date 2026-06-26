n = int(input('Digite um número: '))
while n <= 0:
    n = int(input('Digite um número válido: '))

for i in range(0, n + 1):
    print(2 ** i,end=" ")