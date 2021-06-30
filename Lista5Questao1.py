#Lista semanal de PAA - Lista 5 Questão 1
#Aluno: João Paulo Feitosa Secundo

def heapSort(A,n): #O(n*lg(n))
    montarHeapMaximo(A,n)
    for i in range(n-1,0,-1):
        A[0],A[i]=A[i],A[0]
        rearranjarMaxHeap(A,i)

def montarHeapMaximo(A,tamVetor):
    metade = (tamVetor)//2
    for i in range(metade-1,-1,-1):
        heapifyMax(A,i,tamVetor)

def heapifyMax(A,i,tamVetor):
    esq = (2*i)+1
    dir = (2*i)+2
    if(esq < tamVetor and A[esq] > A[i]):
        maior = esq
    else:
        maior = i

    if(dir < tamVetor and A[dir] > A[maior]):
        maior = dir
    
    if(maior != i):
        A[i],A[maior] = A[maior],A[i]
        heapifyMax(A,maior,tamVetor)

def rearranjarMaxHeap(A,n):
    pai = 0
    filho = 1
    while(filho<=n-1):
        if(filho!=n-1 and A[filho]<A[filho+1]):
            filho=filho+1
        if(A[filho] > A[pai]):
            A[pai],A[filho]=A[filho],A[pai]
            pai=filho
            filho=(2*filho)+1
        else:
            filho = n

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

def intersecoes(A,B,tamA,tamB):
    inter = []
    heapSort(A,tamA)
    for i in range(0,tamB):
        indice = buscaBinaria(A,0,tamA-1,B[i])
        if(indice != -1 ):
            inter.append(B[i])
    return inter

A = [7,5,8,3,4]
B = [9,4,0,3,5]
tamA = len(A)
tamB = len(B)
resultado = intersecoes(A,B,tamA,tamB)
print(resultado)
#O((n+m)*log m)