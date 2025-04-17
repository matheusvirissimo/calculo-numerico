# sin(x) - e^x
import math as mt

TOL = 1e-2
ITER_MAX = 100

def newton_raphton(x_old):
    i = 0
    erro = 2*TOL # para garantir um erro maior que a tolerância logo no início

    while i < ITER_MAX and erro > TOL:
        x_new = x_old - f(x_old)/df(x_old)
        erro = erro_relativo(x_new, x_old)
        x_old = x_new
        i += 1

    return x_new, x_old, erro, i 

def erro_relativo(x_atual, x_antigo):
    return abs(x_atual - x_antigo)/abs(x_atual)


def f(x):
    return mt.sin(x) - mt.e ** x

def df(x):
    return mt.cos(x) - mt.e ** x

raiz_aproximada, ultima_raiz, erro, iteracoes = newton_raphton(0.5)
print(f"A raiz encontrada foi: {raiz_aproximada}")
print(f"A última raiz foi: {ultima_raiz}")
print(f"O erro foi: {erro}")
print(f"A quantidade de iterações: {iteracoes}")