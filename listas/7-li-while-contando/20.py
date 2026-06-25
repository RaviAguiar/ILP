limite = -1
while limite < 0:
    limite = int(input('Digite o primeiro número inteiro positivo: '))

denominador = 1
resultado = 1

while denominador < limite:
    denominador += 1
    resultado = resultado + (1 / denominador)

print(resultado)