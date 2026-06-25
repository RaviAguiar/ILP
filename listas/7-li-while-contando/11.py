n = -1
while n < 0:
    n = int(input('Digite um número inteiro positivo: '))

multiplicador = 1
resultado = n

while multiplicador <= 10:
    resultado = n * multiplicador
    print(f'{n} x {multiplicador} = {resultado}')
    multiplicador += 1