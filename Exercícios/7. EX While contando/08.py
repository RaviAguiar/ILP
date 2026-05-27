#Programa FizzBuzz: escreva um programa que imprime os inteiros de 1 a 20 mas que substitui:
#os múltiplos de 3 pela palavra Fizz,
#os múltiplos de 5 pela palavra Buzz, e
#os múltiplos de 3 e 5 pela palavra FizzBuzz.
x = 1
while x <= 20:
    if x % 15 == 0:
        print('FizzBuzz')
        
    elif x % 3 == 0:
        print('Fizz')

    elif x % 5 == 0:
        print('Buzz')
    
    else:
        print(x)
    
    x += 1