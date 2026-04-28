base = int(input('Digite a base da operação: '))

expoente = -1
while expoente < 0:
    expoente = int(input('Digite o expoente positivo: '))

contador = 0
resultado = 1
while contador < expoente:
    resultado = resultado * base
    contador += 1

print(resultado)