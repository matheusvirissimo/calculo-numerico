"""
Seja 

    | 5  2  1 |
A = | 3  1  4 |
    | 1  1  3 |

a) decompor A em L.U.
"""

import numpy as np # criar matrizes e facilita cálculos númericos

import aula5_eliminacao_lu

def lu_decomposition(A):
    """
    Realiza a decomposição LU de uma matriz A.
    Retorna as matrizes L e U, onde L é triangular inferior e U é triangular superior.
    """
    n = len(A)  # Obtém a dimensão da matriz
    L = np.zeros((n, n))  # Inicializa L como uma matriz de zeros com a dimensão de n na linha e na coluna
    # L = np.eye((n,n)) coloca a matriz principal como a identidade, onde a diagonal principal é 1
    U = np.zeros((n, n))  # Inicializa U como uma matriz de zeros
    
    for i in range(n):
        # Preenchendo a matriz U
        for j in range(i, n):
            soma = sum(L[i][k] * U[k][j] for k in range(i))
            U[i][j] = A[i][j] - soma
        
        # Preenchendo a matriz L
        for j in range(i, n):
            if i == j:
                L[i][i] = 1  # Diagonal principal de L é 1
            else:
                soma = sum(L[j][k] * U[k][i] for k in range(i))
                L[j][i] = (A[j][i] - soma) / U[i][i]
    
    return L, U

# Exemplo de uso
A = np.array([[5, 2, 1], [3, 1, 4], [1, 1, 3]], dtype=float)  # Matriz de entrada
L, U = lu_decomposition(A)
print("Matriz L:")
print(L)
b = [0, -5, -7]
print("Matriz U:")
print(U)

