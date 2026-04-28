n = -1
while n < 0:
    n = int(input('Digite o número de notas: '))

contador = 0
nota = 0
menor_nota = nota
while contador < n:
    nota = int(input('Digite a nota: '))
    if nota < menor_nota:
        menor_nota = nota
    contador += 1

print(menor_nota)