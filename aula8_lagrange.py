import numpy as np

def lagrange(x,y,c):
    n = len(x) 
    soma = 0

    for i in range(n):
        soma += y[i] * prod(x, c, i)

    return soma

def prod(x, c, i):
    valor = 1 
    n = len(x)

    for k in range(n):
        if i != k:
            valor *= ((c - x[k])/(x[i] - x[k]))

    return valor

x = np.array([-1, 0, 3], dtype=float) 
y = np.array([15, 0, -1], dtype=float) 

print(lagrange(x, y, 1))