def eh_numero_par(numero):
    if numero % 2 == 0:
        return True
        # return "par"
    else:
        # return "impar"
        return False
    
numero = int(input("digite um numero: "))

par = eh_numero_par(numero)
if par == True:
    print('É par.')
else:
    print('É ímpar.')