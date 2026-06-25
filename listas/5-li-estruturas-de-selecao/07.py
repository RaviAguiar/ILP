nome = input('Digite um nome de usuário: ').strip()
q_caracteres = len(nome)
if q_caracteres > 10:
    print(f'Nome muito longo.')
else:
    print('show de bola')