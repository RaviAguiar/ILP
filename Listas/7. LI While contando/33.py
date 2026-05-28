soma_dos_pares = 0
soma_dos_impares = 0
n = 1

while n != 0:
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        soma_dos_pares += n
    else: 
        soma_dos_impares += n

print(f'A soma dos pares é {soma_dos_pares}')
print(f'A soma dos ímpares é {soma_dos_impares}')