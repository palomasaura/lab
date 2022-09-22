###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Ingresso do Cinema
# Nome: Paloma Saura Tirolti
# RA: 237694
###################################################

# leitura de dados

d = int(input())
h = int(input())
m = int(input())
e = input()
p = input()
S = 1
N = 0
C = 1
D = 0

# valor do ingresso inteiro

if d == [1, 7] and h <= 18 and m < 30:
    t = (30)
elif d == [2, 3, 4] and h <= 18 and m < 30:
    t = (15)
elif d == [5, 6] and h <= 18 and m < 30:
    t = (20)
elif d == [1, 4, 5] and h >= 18 and m >= 30:
    t = (30)
elif d == [2, 3] and h >= 18 and m >= 30:
    t = (20)
else:
    t = (40)

# valor d pagar

if d == 1 and e == S:
    ingresso = t/2
elif d == 1 and p == C:
    ingresso = t - (30*t/100)
elif d == 1 and e == N and p == D:
    ingresso = t
elif d == (2, 3, 4, 5, 6) and h <= 18 and m < 30 and e == S or p == C:
    ingresso = t/2
elif d == (2, 3, 4, 5) and h <= 18 and m < 30 and e == N or p == D:
    ingresso = t
elif d == (2, 3, 4, 5) and h >= 18 and m > 29 and e == S or p == C:
    ingresso = t/2
elif d == (2, 3, 4, 5) and h >= 18 and m > 29 and e == N or p == D:
    ingresso = t
elif d == 6 and h >= 18 and m > 29 and e == N or p == C:
    ingresso = t - (30*t/100)
elif d == 6 and h >= 18 and m > 29 and e == N or p == D:
    ingresso = t
elif d == 7 and e == S:
    ingresso = t/2
elif d == 7 and p == C:
    ingresso = t - (20*t/100)
else:
    ingresso = t

# saída do valor do ingresso
print('Valor do ingresso: R$', format(ingresso, '.2f').replace('.', ','))