n = int(input('Digite a quantidade de números a serem lidos: '))
while n <= 0:
    n = int(input('Digite um número válido: '))
for i in range(n):
    x = int(input('Digite um número: '))
    if x < 10:
        print(f'{x} é um número pequeno')
    elif 10 <= x <= 100:
        print(f'{x} é um número médio')
    else:
        print(f'{x} é um número grande')