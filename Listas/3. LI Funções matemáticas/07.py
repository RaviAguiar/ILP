import math
area = float(input('Digite a área a ser revestida em metros quadrados: '))
ceramica = 1.5
qmin = math.ceil(area / ceramica)
print(f'A quantidade mínima de caixas de cerâmica que devem ser compradas é de: {qmin} caixas.')