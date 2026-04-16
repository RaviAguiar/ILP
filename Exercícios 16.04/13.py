#Programa FizzBuzz: Escreva um programa que tem como entrada um número inteiro positivo n e imprime os inteiros de 1 a n, mas que
#substitui os múltiplos de 3 pela palavra Fizz, os múltiplos de 4 pela palavra Buzz e os múltiplos de 3 e 4 pela palavra FizzBuzz.
limite = -1
while limite < 1:
    limite = int(input('Digite um número inteiro positivo: '))

contador = 1
while contador <= limite:
    if contador % 12 == 0: print('FizzBuzz')

    elif contador % 3 == 0: print('Fizz')

    elif contador % 4 == 0: print('Buzz')

    else: print(contador)

    contador += 1
