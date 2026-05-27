contador = 1
n = 0
n_positivos = 0
n_negativos = 0
n_zero = 0

while contador <= 10:
    n = int(input('Digite um número inteiro: '))

    if n > 0:
        n_positivos += 1

    elif n < 0:
        n_negativos += 1

    else:
        n_zero += 1

    contador += 1

print(f'Quantidade de números digitados positivos: {n_positivos}')
print(f'Quantidade de números digitados negativos: {n_negativos}')
print(f'Quantidade de números digitados iguais a 0: {n_zero}')