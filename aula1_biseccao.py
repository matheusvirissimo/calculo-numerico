"""
Dadas as funções
a) x^3 + 3x - 1 = 0
b) x^2 - sinx = 0 
Pesquise a existência de raizes e as determine
"""

import math as mt

tolerancia = 1e-6  

#bisseccao

def metodo_iterativo(f, f_a, f_b):
    if f(f_a) * f(f_b) > 0:
        raise ValueError("Intervalo inacessível")

    while abs(f_b - f_a) > tolerancia:
        c = media_simples(f_a, f_b)

        if c == 0:
            return c ## encontrou a raiz exata
        elif f(f_a)*f(c) < 0:
            f_b = c
        else:
            f_a = c

    return [f_a, f_b]
        

#achar c
def media_simples(a, b):
    return (a+b)/2

#criar equação
def f(x):
    return x**3 + 3 * x - 1

def h(x):
    return x**2 - mt.sin(mt.radians(x))

print(metodo_iterativo(f, 0, 3))
print(metodo_iterativo(h, 0, 100))


