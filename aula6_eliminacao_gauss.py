def eliminicao_gauss(A, b):
    n = len(A) # obtém o número de linhas da matriz A

    for k in range(n-1): #percorre cada coluna até a penúltima 
        for i in range(k+1,n): # percorre as linhas abaixo da primeira para zerar a coluna k 
            b[i] = b[i] - (A[i][k]/A[k][k]) * b[k] #atualiza o vetor b (possível divisão por 0 aqui)
            

            #quando k+1, os valores de b são atualizados corretamente, mas não de A
            #quando k, os valores de A são atualizados corretamente, mas não de b
            for j in range(k+1,n): # percorre a coluna a partir da que estamos atualmente
                A[i][j] = A[i][j] - (A[i][k]/A[k][k] * A[k][j]) # atualiza os coeficientes de A (possível divisão por 0)
        
    return A, b


def determinante(A):
    n = len(A)
    det = 1

    for i in range(n):
        for j in range(n):
            if i == j:
                det *= A[i][j]
        
    return det

"""
    | 2  -3  1 |
A = | 4  -6  -1 |
    | 1  2  1 |
"""

if __name__ == "__main__":

    matriz_a = [[2,3,1], 
                [4,7,5], 
                [6,18,11]]

    b = [1, 3, 6]

    matriz_escalonada, termos_independentes = eliminicao_gauss(matriz_a, b)

    det = determinante(matriz_escalonada)

    print(matriz_escalonada)
    print(termos_independentes)