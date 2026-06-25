n = 0
while n < 1:
    n = int(input('Digite o limite (inteiro e positivo): '))

repetidor = 1
x = 0
positivos = 0
negativos = 0


while repetidor <= n:
    x = int(input('Digita o número aí: '))
    if x > 0:
        positivos += x

    elif x < 0:
        negativos += x

    repetidor += 1

print(f'A soma dos valores positivos é {positivos}')
print(f'A soma dos valores negativos é {negativos}')