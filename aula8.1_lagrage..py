def lagrange(x, c, y):
    n = len(x)
    soma = 0 
    pi = 1 

    for j in range(n):
        pi *= (c-x[j])

    for i in range(n):
        soma += y[i]/prod(x,c,i)

    return pi*soma

def prod(x, c, i):
    n = len(x)
    d = 1

    for k in range(n):
        if k != i:
            d *= (x[i] - x[k])
        
    return d*(c-x[i])

