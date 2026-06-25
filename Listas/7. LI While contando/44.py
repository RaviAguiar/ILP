n = int(input('Digite um número inteiro positivo: '))
while n <= 0:
    print('\nValor inválido')
    n = int(input('Digite um número inteiro positivo: '))

contador = 1
while contador <= n:
    for i in range(contador):
        print('*', end="")
    print('')
    contador += 1
#(vou deixar esse comentário aqui caso tenha alguem sem nada pra fazer que esteja olhando meu código (provavelmente ninguém))
#nesse código eu pensei "ah vou tentar replicar aquela função do html no vs code de multiplicar" (por exemplo li*4 que faz 4 li em 4 linhas)
#aí dps de muita tentativa e erro cheguei nesse código que funciona, fiquei mto orgulhoso de mim mesmo pq foi difícil pra mim e eu fiz com 0 ajuda, só raciocinando mesmo
#nisso eu vou no gemini e peço pra ele fazer a questão pra ver como ele faria, se tem algo que eu podia otimizar e tal
#só pra descobrir que a função do html que eu tava tentando replicar FUNCIONA (pelo menos de forma parecida) no python
#aí só de raiva vou deixar aqui a resolução usando essa funcionalidade (que deixa o código beem mais limpo e simples

#n = int(input('Digite um número inteiro positivo: '))
#while n <= 0:
#    print('\nValor inválido')
#    n = int(input('Digite um número inteiro positivo: '))
#
#for i in range(1, n + 1):
#   print('*' * i)