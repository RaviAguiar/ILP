n = int(input('Digite um número inteiro positivo: '))
while n < 0:
    n = int(input('Digite um número válido: '))

eh_primo = 0
for i in range(2, n + 1):
    if n % i == 0:
        eh_primo += 1

if eh_primo == 1:
    print('É primo')
else:
    print('Não é primo')