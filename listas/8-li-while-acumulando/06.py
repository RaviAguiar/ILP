ativo = True
soma = 0
while ativo == True:
    n = int(input('Digite um número inteiro: '))
    if n == 0:
        ativo = False
    soma += n

print(soma)