n = int(input())
lista = []
while len(lista) != n:
    x = input()
    lista = str(x).split(' ')
print(sum(lista))