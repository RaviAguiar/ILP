#Escreva um programa que tem como entrada um número inteiro positivo [numero] e imprime os múltiplos de 3 compreendidos entre 1 e [numero]

limite = -1

while not limite > 0:
    limite = int(input('Digite um número inteiro positivo: '))

x = 1

while x <= limite:
    if x % 3 == 0:
        print(x)
    x += 1
