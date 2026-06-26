n = int(input('Digite um número positivo: '))
while n < 0:
    n = int(input('Digite um número válido: '))

soma = 0
for i in range(n):
    x = float(input('Digite uma nota de 0 a 10: '))
    while not 0 <= x <= 10:
        x = float(input('Digite um número válido: '))
    soma += x

print(soma / n)