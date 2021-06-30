import random
def buscaBinaria(A,esq,dir,z):
    metade = (esq+dir)//2
    if(esq == dir):
        if(z==A[esq]): return esq
        else: return -1
    else:
        #achar a última ocorrencia: usar >=
        #achar a primeira ocorrencia: usar >
        if(z > A[metade]):
            return buscaBinaria(A,metade+1,dir,z)
        else:
            return buscaBinaria(A,esq,metade,z)

T = random.sample(range(-20,30),10)
T.sort()
print(T)
n = len(T)
indice = buscaBinaria(T,0,n-1,12)
print(indice)