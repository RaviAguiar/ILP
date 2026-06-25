numero = -1
while numero < 0:
    numero = int(input('Digite um número inteiro e positivo: '))

quantidade_de_digitos = len(str(numero))
multiplicador = 10 ** (quantidade_de_digitos - 1)
resultado = 0

while multiplicador >= 1:
    resultado = resultado + (numero % 10) * multiplicador
    numero = numero // 10
    multiplicador = multiplicador // 10

print(resultado)