"""
x^2 - 2 = 0
"""

import math as mt

#constantes

TOL = 1e-3
ITER_MAX = 100
CSI = mt.sqrt(2)

x_old = 1.0
x_old_old = x_old


def metodo_newton():
    global x_old, x_old_old
    erro = 2*TOL
    p = 0
    i = 0

    while erro > TOL and i < ITER_MAX:
        x_new = x_old - f(x_old)/df(x_old) ## método newton
        erro = abs(x_new - x_old)/abs(x_new) ## erro relativo

        if(i >= 1):
            e_1 = abs(CSI - x_new)
            e_2 = abs(CSI - x_old)
            e_3 = abs(CSI - x_old_old)

            p = ordem_convergencia(e_1, e_2, e_3)

        x_old_old = x_old
        x_old = x_new
        i += 1
    
    print(f"A raiz da equação é: {x_new}")
    print(f"Erro: {erro}")
    print(f"Numero de iterações: {i}")
    print(f"Ordem de convergência estimada: {p}")

    return

def f(x):
    return (x ** 2 - 2.0)

def df(x):
    return (2*x)

def ordem_convergencia(e_1, e_2, e_3):
    return (mt.log(e_1/e_2)/mt.log(e_2/e_3))


metodo_newton()