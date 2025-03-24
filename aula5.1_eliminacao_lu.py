"""
Continuação do exemplo
    | 5  2  1 |
A = | 3  1  4 |
    | 1  1  3 |

b) calcular det(A)
c) Resolver Ax=b onde b = (0, -7, -5)^t(rasnposta)
"""

import numpy as np

# Superior triangular INFERIOR
def triangular_lower(L, b):
    n = len(L)
    x = np.zeros(n)
    x[0] = calculte_first_value(L,b) # calcula o primeiro valor de x

    for i in range(1, n):
        somatorio = 0
        for k in range(i):
            somatorio += L[i][k]*x[k]
        
        x[i] = (b[i] - somatorio)/L[i][i]

    return x # x seria y


# fórmula do primeiro valor = x_1 = b_1/a_11
def calculte_first_value(L, b):
    return (b[0]/L[0][0])

# Superior triangular SUPERIOR

def triangular_upper():
    pass



# Calculando determinante

def determinante(U):
    n = len(U)
    det = 1

    for i in range(n):
        for j in range(n):
            if i == j:
                det *= U[i][j]
        
    return det



b = [0, -5, -7]
L = [[1,0,0][2,1,0],[3,2,1]]
y = triangular_lower(L, b)

