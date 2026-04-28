n = float(input('Digite o número de termos da progressão artimética: '))
a = float(input('Digite o primeiro termo da progressão aritmética: '))
r = float(input('Digite a razão da progressão aritmética: '))
contador = n - 1
resultado = a
print(a)
while contador > 0:
    resultado = resultado + r
    print(resultado)
    contador -= 1