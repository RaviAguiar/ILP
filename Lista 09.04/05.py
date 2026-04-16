n1 = -1
while not (0 <= n1 <= 10):
    n1 = float(input('Digite a nota (entre 0 a 10): '))

if (n1 >= 7):
    print('Aprovado')
else:
    print('Reprovado')