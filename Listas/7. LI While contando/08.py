limite = -1
while limite < 0:
    limite = int(input('Digite um número inteiro positivo: '))

#incrementando:
#contador = 1
#resultado = 1
#while contador <= limite:
    # resultado = limite * (limite - 1) * (limite - 2)  ... * 1
    # resultado = contaodor * (contador + 1) * (contador + 2) ... * limite
#    resultado = resultado * contador
#    contador += 1
#print(resultado)

# decrementando :
contador = limite
resultado = limite
while contador > 1:
    resultado = resultado * (contador - 1)
    contador -= 1
print(resultado)