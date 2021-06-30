#Lista semanal de PAA - Lista 7 Questão 1
#Aluno: João Paulo Feitosa Secundo
def acharPadroes(T,n,P,m,k):
    q = 3354393
    d = 32
    dM = 1
    for i in range(0,m-1):
        dM = (d*dM) % q
    
    h1 = [0]*k #hashes dos padroes
    h2 = 0 #hash do texto
    for j in range(0,k): #para cada palavra
        for i in range(0,m):
            h1[j] = (h1[j]*d+ord(P[j][i]))%q

    heapSort(h1,k) #ordenar vetor dos hashes dos padroes

    for i in range(0,m):
        h2 = (h2*d+ord(T[i]))%q #calcula o hash do texto para os m primeiros caracteres

    i=0
    cont=0
    indices = [-1]*k
    while(i <= n-m):
        indice = buscaBinaria(h1,0,k-1,h2)
        if(indice != -1):
            indices[cont] = i
            cont=cont+1
        if(i!=n-m):
            h2 = (h2 + d*q - ord(T[i])*dM )%q #remove o primeiro caractere
            h2 = (h2*d + ord(T[i+m]))%q #e adiciona o proximo
        i=i+1

    if(cont==k):
        print("Todas as palavras foram encontradas. Indices:")
        print(indices)
    else:
        print("Nem todas as palavras foram encontradas")

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

def heapSort(A,n): #O(n*lg(n))
    montarHeapMaximo(A,n)
    for i in range(n-1,0,-1):
        A[0],A[i]=A[i],A[0]
        rearranjarMaxHeap(A,i)

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

T = "xxabcxcdafjxxx"
P = ["abc","cda","xxx","afj"]
n = len(T)
k = len(P)
m = len(P[0])
acharPadroes(T,n,P,m,k)
