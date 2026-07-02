n = int(input('Digite um número inteiro positivo: '))
while n < 0:
    n = int(input('Digite um número válido: '))

lista = [int(digito) for digito in str(n)]
print(sum(lista))