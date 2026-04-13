a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))
maior = max(a, b, c)
if maior.is_integer():
    print(f'O maior número é: {maior:.0f}')
else: 
    print(f'O maior número é: {maior}')