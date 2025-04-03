"""
Continuação do exemplo
    | 5  2  1 |
A = | 3  1  4 |
    | 1  1  3 |

b) calcular det(A)
c) Resolver Ax=b onde b = (0, -7, -5)^t(rasnposta)
"""

import numpy as np


# Superior triangular INFERIOR -> L * y = b
def triangular_lower(L, b):
    n = len(L)
    x = np.zeros(n)
    x[0] = calculte_first_value(L,b) # calcula o primeiro valor de x
    somatorio = 0 ## tem que começar fora do for logicamente

    for i in range(1, n):
        for k in range(i):
            somatorio += L[i][k]*x[k]
        
        x[i] = (b[i] - somatorio)/L[i][i]

    return x # x seria y e é a solução do sistema


# fórmula do primeiro valor = x_1 = b_1/a_11
def calculte_first_value(L, b):
    return (b[0]/L[0][0])


# Superior triangular SUPERIOR -> U * x = y
def triangular_upper(U,y):
    n = len(U) # tamanho de U
    x = np.zeros(n) # zera a solução
    x[-1] = calculate_last_value(U, y) # calcula o último valor

    for i in range(n-2, -1, -1): # começa da penúltima linha até a primeira
        somatorio = sum(U[i][k] * x[k] for k in range(i+1, n)) # soma dos termos conhecidos 
        x[i] = (y[i] - somatorio/U[i][i]) # só segui a fórmula a fórmula 

    return x # solução do sistema

# fórmula do último valor = x_n = y_n/u_nn
def calculate_last_value(U, y):
    return (y[-1]/U[-1][-1])


# Calculando determinante

def determinante(U):
    n = len(U)
    det = 1

    for i in range(n):
        for j in range(n):
            if i == j:
                det *= U[i][j]
        
    return det

