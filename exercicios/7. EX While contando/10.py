#Escreva um programa que tem como entrada um número inteiro positivo [numero] e imprime os números inteiros compreendidos no intervalo [-numero; numero].
numero_lim = -1

while not numero_lim > 0:
    numero_lim = int(input('Digite um número inteiro positivo: '))

numero_neg = -numero_lim

while numero_neg <= numero_lim:
    print(numero_neg)
    numero_neg += 1