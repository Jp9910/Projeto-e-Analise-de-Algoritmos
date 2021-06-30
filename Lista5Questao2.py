#Lista semanal de PAA - Lista 5 Questão 2
#Aluno: João Paulo Feitosa Secundo
#usar vetor para lembrar posiçao original das strings
#complexidade: fórmula H(i)
def heapSort(A,n): #O(n*lg(n))
    montarHeapMaximo(A,n)
    print("heapMaximo:",A)
    for i in range(n-1,0,-1):
        A[0],A[i]=A[i],A[0]
        rearranjarMaxHeap(A,i)

def rearranjarMaxHeap(A,n):
    pai = 0
    filho = 1
    while(filho<=n-1):
        if(filho!=n-1 and len(A[filho])<len(A[filho+1])):
            filho=filho+1
        if(len(A[filho]) > len(A[pai])):
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
    if(esq < tamVetor and len(A[esq]) > len(A[i])):
        maior = esq
    else:
        maior = i

    if(dir < tamVetor and len(A[dir]) > len(A[maior])):
        maior = dir
    
    if(maior != i):
        A[i],A[maior] = A[maior],A[i]
        heapifyMax(A,maior,tamVetor)

A = ["eeee","ccc","bbbbb","pp","dd","ffff","aaa","xxxxxx","n","tt","pppp",""]
print("original:",A)
heapSort(A,len(A))
print("ordenado:",A)