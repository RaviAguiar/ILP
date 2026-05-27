def numeros(a, b, c, d, e):
    menor = min(a, b, c, d, e)
    maior = max(a, b, c, d, e)

#def maior_numero(numeros):
#    maior = -1
#    for numero in numeros:
#        if maior < numero:
#            maior = numero

[num1, num2, num3, num4, num5] = map(float, input().split())
numeros = list(map(float, input().split()))


numeros(num1, num2, num3, num4, num5)
print(menor)
print(maior)