#Lista semanal de PAA - Lista 5 Questão 3
#Aluno: João Paulo Feitosa Secundo
#mudar para heapsort e procurar as ocorrencias usando buscabinaria
class copiaC:
    def __init__(self,C,B) -> None:
        self.Z=C.copy()
        self.B=B

def countingSort(A,n) -> list:
    k=A[0]
    B = [None] * n
    for i in range(0,n): 
        if(A[i]>k): k=A[i]
    C = [0] * (k+1)

    for j in range(0,n):
        C[A[j]] += 1
    for i in range(1,k+1):
        C[i] = C[i] + C[i-1]
    obj = copiaC(C,B)
    for j in range(n-1,-1,-1):
        B[C[A[j]]-1] = A[j]
        C[A[j]] -= 1
    return obj

def inteirosNosIntervalos(A,tamA):
    numeros = []
    for i in range(0,tamA,2):
        for i in range(A[i],A[i+1]+1): #O(n), onde n = soma dos tamanhos dos intervalos
            numeros.append(i)
    numeros = countingSort(numeros,len(numeros))
    return numeros

def localizar(A,z):
    indice = buscaBinaria(A.B,0,len(A.B)-1,z)
    if(indice != -1):
        ultimo = A.Z[z] - 1
        primeiro = A.Z[z-1]
        print("primeiro:",primeiro,A.B[primeiro])
        print("ultimo:",ultimo,A.B[ultimo])
    else:
        print("elemento nao ocorre")

def buscaBinaria(X,esq,dir,z):
    if(dir >= esq):
        metade = (esq+dir)//2
        if X[metade] == z:
            return metade
        elif(z < X[metade]):
            return buscaBinaria(X,esq,metade-1,z)
        else:
            return buscaBinaria(X,metade+1,dir,z)
    else:
        return -1

I = [1,3, 7,9, 1,8, 0,0, 12,12, 3,4]
print(I)
numeros = inteirosNosIntervalos(I,len(I))
print(numeros.B)
print(numeros.Z)
localizar(numeros,3)

#O(n*log(n))
#nmrElementos = 0
#for i in range(0,tamA,2):
#   nmrElementos += A[i+1]-A[i]