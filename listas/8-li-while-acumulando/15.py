n = int(input('Digite o primero número: '))
k = int(input('Digite o segundo número: '))

primeiro = 0
segundo = 0
if n < k or n == k:
    primeiro = n
    segundo = k
elif k < n:
    primeiro = k
    segundo = n

for i in range(primeiro, segundo + 1):
    if i % k == 0:
        print(i)