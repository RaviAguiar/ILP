n = int(input('Digite um número positivo: '))
while n < 0:
    n = int(input('Digite um número válido: '))
fatorial = 1

if n == 0:
    print(0)
else:
    for i in range(1, n + 1):
        fatorial *= i
    print(fatorial)