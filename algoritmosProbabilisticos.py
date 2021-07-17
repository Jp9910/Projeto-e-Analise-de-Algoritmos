import random
import time

def monteCarlo(X,n,k):
    #Problema: Sejam n números inteiros em ordem arbitrária. 
    #          Encontrar um número que pertença à metade superior 
    #          (maior ou igual à mediana), considerando a ordem dos elementos
    
    #X é o vetor da qual será escolhido aleatoriamente um valor que deve estar na parte superior
    #n = len(X)
    #k é quantidade de índices testados. Será retornado o maior deles
    maior=-999999
    n=n-1
    for i in range(0,k):
        j = random.randint(0,n)
        print("índice aleatório:",j)
        if(X[j] >= maior):
            maior=X[j]
    return maior

def lasVegas(X):
    pass

def randomCongruenciaLinear(quantidade,startRange,endRange):
    r = [None]*(quantidade+1)
    b=3
    r[0] = int(time.time())
    #r[0] = 9910

    for i in range(1,quantidade+1):
        r[i] = ((r[i-1]*b + 1) % endRange)+startRange
    
    r.pop(0)
    return r

X = randomCongruenciaLinear(4,7,14)
print(X)

r = monteCarlo(X,len(X),5)
print("Número escolhido aleatoriamente que provavelmente está na parte superior de X:",r)