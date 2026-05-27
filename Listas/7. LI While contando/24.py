numero = -1

while numero < 0:
    numero = int(input('Digite um número inteiro positivo: '))

quantidade_de_digitos = len(str(numero))
soma_dos_digitos = 0

while quantidade_de_digitos >= 1:
    soma_dos_digitos = soma_dos_digitos + (numero % 10)
    numero = numero // 10
    quantidade_de_digitos -= 1

print(f'A soma dos dígitos do número digitado é: {soma_dos_digitos}')