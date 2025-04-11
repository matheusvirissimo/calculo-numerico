import math as mt

ITER_MAX = 1000
EPSILON = 10 ** -6


def f(x):
    return mt.e ** x - 2 * x - 1

a = 1 
b = 2
x_antigo = 1.5 ## chute inicial (deve estar no intervalo)
x_novo = 0
iter = 1 
erro_relativo = 2*EPSILON

while((erro_relativo > EPSILON) and (iter < ITER_MAX)):
    x_novo = f(x_antigo)
    erro_relativo = abs(x_novo - x_antigo)/abs(x_novo)

    x_antigo = x_novo
    iter += 1

print(f"raiz={x_antigo}")

if __name__ == "__main__":
    print()
