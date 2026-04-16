a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))
menor = min(a, b, c)
if menor.is_integer():
    print(f'O menor número é: {menor:.0f}')
else: 
    print(f'O menor número é: {menor}')