n = 0
while n < 1:
    n = int(input('Digite o limite (inteiro e positivo): '))

testador = 0
for i in range(1, (n + 1)):
    if n % i == 0:
        testador += 1
    
if testador == 2:
    print(f'{n} é primo')

else: 
    print(f'{n} não é primo')