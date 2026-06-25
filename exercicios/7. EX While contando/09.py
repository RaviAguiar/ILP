#Escreva um programa que tem como entrada um número inteiro positivo numero e imprime os números inteiros de 1 a numero.
n1 = 1
limite = -1

while not limite > 0:
    limite = int(input('Digite um número inteiro positivo: '))

while n1 <= limite:
    print(n1)
    n1 += 1
