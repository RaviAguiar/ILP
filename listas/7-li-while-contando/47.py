import random
n = random.randint(1, 100)
acerto = False
while acerto == False:
    x = int(input('Faça seu chute: '))
    if x < n:
        print('Muito baixo!')
    elif x > n:
        print('Muito alto!')
    elif x == n:
        print('Acertou!')
        acerto = True