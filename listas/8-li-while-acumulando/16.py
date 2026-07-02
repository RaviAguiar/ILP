n = int(input('Digite um número inteiro positivo: '))
while n < 0:
    n = int(input('Digite um número válido: '))

passos = 0
print(n, end =" ")
while n != 1:
    if n % 2 == 0:
        n //= 2
    else:
        n *= 3 
        n += 1
    passos += 1
    print(n, end=" ")
print(f'\nPassos = {passos}')