n = int(input('Digite um número inteiro positivo: '))
while n < 0:
    n = int(input('Digite um número válido: '))

n = str(n)
print(len(n))