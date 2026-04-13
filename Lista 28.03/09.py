import math
c1 = float(input('Digite o valor do primeiro cateto: '))
c2 = float(input('Digite o valor do segundo cateto: '))
hipo = math.sqrt(c1**2 + c2**2)
if hipo.is_integer():
    print(f'O valor da hipotenusa é {hipo:.0f}.')
else:
    print(f'O valor da hipotenusa é {hipo:}.')