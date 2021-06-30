
def buscaBinariaListaBugada(A,esq,dir,z):
    #Udi Manber - exercicio 6.19 (pdf pag 194)
    #lista A tal que A[i+1] >= A[i]-1 (prox elemento é pelo menos o anterior -1)
    metade = (esq+dir)//2
    if(esq == dir):
        if(z==A[esq]): return esq
        else: return -1
    else:
        if(z > A[metade]):
            return buscaBinariaListaBugada(A,metade+1,dir,z)
        else:
            return buscaBinariaListaBugada(A,esq,metade,z)

A = [3,5,4,3,4,6,12]
#A = [3,4,5,6,7,12]
print(A)
indice = buscaBinariaListaBugada(A,0,len(A)-1,5)
print(indice)