n = -1
while n < 0:
    n = int(input('Digite o número de notas: '))

contador = 0
nota = 0
maior_nota = -1
while contador < n:
    nota = int(input('Digite a nota: '))
    if nota > maior_nota:
        maior_nota = nota
    contador += 1

print(maior_nota)
# contador = 0
# while contador < ?:
#  exec
#  contador = contador + 1