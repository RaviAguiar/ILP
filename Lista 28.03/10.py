import math
n1 = float(input('Digite um número real positivo: '))
rq = math.sqrt(n1)
rqbaixo = math.floor(rq)
rqcima = math.ceil(rq)
print(f'O valor da raíz quadrada exata de {n1} é: {rq}')
print(f'O valor da raíz quadrada arredondada para baixo de {n1} é: {rqbaixo}')
print(f'O valor da raíz quadrada arredondada para cima de {n1} é: {rqcima}')