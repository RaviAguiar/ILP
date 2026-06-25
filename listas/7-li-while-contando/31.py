nota = -1
soma_das_notas = 0
aprovados = 0
reprovados = 0
em_recuperacao = 0


for i in range (1, 11):
    while 0 > nota or nota > 10:
        nota = float(input(f'Digite a nota {i}:'))


    soma_das_notas += nota

    if nota >= 7:
        aprovados += 1
    
    elif nota < 5:
        reprovados += 1

    else:
        em_recuperacao += 1

    nota = -1

print(f'A média das notas é de {soma_das_notas / 10}')
print(f'Quantidade de alunos aprovados: {aprovados}')
print(f'Quantidade de alunos reprovados: {reprovados}')
print(f'Quantidade de alunos em recuperação: {em_recuperacao}')