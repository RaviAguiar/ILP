# 0 1 1 2 3 5 8 13 21 34
proximo = 0
anterior = 1
n = 0
while n <= 0:
    n = int(input('Digite o número da sequência Fibonacci que deseja: '))

if n == 1:
    print(0)
elif n == 2:
    print(1)

else:
    print(0)
    print(1)
    for i in range(n):
        proximo = anterior + anterior - 1
        print(proximo)
        anterior = proximo