n = 0
soma = 0
contador = 0

while contador <= 9:
    n = float(input('Digite um valor: '))
    soma = soma + n
    contador += 1

print(f'A média aritmética dos valores digitados é : {soma / 10}')