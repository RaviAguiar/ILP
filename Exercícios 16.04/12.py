#Escreva um programa que tem como entrada um número inteito contador no intervalo [1; 10]. Quando for informado o contador == 0
#o programa deve encerrar. Quando o valor de contador estiver fora do intervalo, o programa deve informar que o número é inválido.

x = -1
while True:
    x = int(input('Digite um número entre 1 e 10 ou 0 para encerrar o programa: '))

    if x == 0:
        print('Encerrando programa')
        break

    elif x > 10 or x < 1:
        print('Número inválido, tente novamente.')

    else: 
        print('Show de bola!')