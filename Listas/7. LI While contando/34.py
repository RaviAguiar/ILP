a = 0
b = 0
primo = 2
primo_final = 0
eh_primo = 0
divisores_do_primo = 0
testador_divisao_inteira_a = 0
testador_divisao_inteira_b = 0
testador_divisores = 0

while a < 1:
    a = int(input('Digite o primeiro número: ')) #garante que o número digitado é maior que 0

while b < 1:
    b = int(input('Digite o segundo número: ')) #mesma coisa

if a == 1 or b == 1: #caso algum dos números digitados seja 1
    print('1')

else:
    while a != 1 and b != 1: #enquanto o mdc não tiver terminado
        while eh_primo == False: #enquanto um primo não for encontrado
            for i in range(1, primo + 1): #testa quantos dividores o número tem
                if primo % i == 0:
                    testador_divisores += 1

            if testador_divisores == 2: #se tiver 2 divisores é primo
                eh_primo = True
            else: 
                eh_primo = False #senão não é primo e repete o processo até achar um primo
            
        if isinstance(a / primo, int)
            testador_divisao_inteira_a = True
        else:
            testador_divisao_inteira_a = False

        if isinstance(b / primo, int):
            testador_divisao_inteira_b = True
        else:
             testador_divisao_inteira_b =  False

        if testador_divisao_inteira_a == True:
            a = a / primo
        if testador_divisao_inteira_b == True:
            a = a / primo
        if testador_divisao_inteira_a == True and testador_divisao_inteira_b == True:
            primo_final = primo_final * primo

        eh_primo = False
        primo +=

        676767676767676767676767676767676767676767