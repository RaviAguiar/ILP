nint = 1
contador = 0

while nint != 0:
    nint = int(input('Digite um número inteiro: '))
    contador += 1

contador -= 1

print(f'Quantidade de número lidos (sem contar o 0): {contador}.')