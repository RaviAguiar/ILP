verificador_de_primo = 0
soma_dos_primos = 0
contador = 2
inicio = int(input('Digite o início: '))
fim = int(input('Digite o fim: '))
if fim < inicio:
    inicio *= -1
    fim *= -1

#os dois negativos
if inicio < 0 and fim < 0:
    print(f'A soma dos primos entre {inicio} e {fim} = 0')

#inicio negativo e fim positivo
elif inicio < 0 and fim > 1:
    for x in range(2, fim + 1):
        for i in range(2, x + 1):
            if x % i == 0:
                verificador_de_primo += 1
        if verificador_de_primo == 2:
            soma_dos_primos += x

print(f'A soma dos primos entre {inicio} e {fim} é igual a {soma_dos_primos}')