a = 0
b = 0
resto = 0
while a <= 0:
    a = int(input('Digite o primeiro número: '))
while b <=0:
    b = int(input('Digite o segundo número: '))

menor = min(a, b)
maior = max(a, b)

while maior % menor != 0:
    resto = maior % menor
    maior = menor
    menor = resto
    
print(menor)