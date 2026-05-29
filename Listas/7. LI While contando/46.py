# Solicita o número de termos ao usuário
n = int(input("Quantos termos da sequência de Fibonacci você quer ver? "))

# Primeiros dois termos
a, b = 0, 1
contagem = 0

# Validação para o caso de o usuário digitar 0 ou números negativos
if n <= 0:
    print("Por favor, insira um número inteiro positivo maior que 0.")
elif n == 1:
    print(f"Sequência de Fibonacci até {n} termo: {a}")
else:
    print("Sequência de Fibonacci:", end=" ")
    while contagem < n:
        print(a, end=" ")
        # Atualiza os valores para os próximos termos
        a = b
        b = a + b
        contagem += 1
    print()  # Apenas para pular a linha no final do programa