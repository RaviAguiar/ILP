def soma(tung, sahur):
 return tung + sahur
def soma_e_subtracao(c, d):
 return c + d, c - d
x, y = 5, 8
sm = soma(x, y)
print(sm) # 13
sm, sb = soma_e_subtracao(x, y)
print(sm) # 13
print(sb) # -3
