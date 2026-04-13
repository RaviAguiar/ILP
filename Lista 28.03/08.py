import math
tempo = float(input('Digite a quantidade de tempo em horas: '))
horas = math.floor(tempo)
minutos = math.floor((tempo - horas) * 60)
print(f'Tempo:{horas} hora(s) e {minutos} minuto(s)')