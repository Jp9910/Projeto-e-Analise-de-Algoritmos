#Lista semanal de PAA - Lista 10 Questão 2
#Aluno: João Paulo Feitosa Secundo
class Ponto():
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y

def maximais(C,n):
    #procurar pontos cujo x OU y são maiores
    heapSortPontosCrescenteX(C,n)
    #for i in range(0,n):
    #    print(C[i].x,C[i].y)
    pmaximais = [None]*n;k=0
    ymax = -9999999999
    for i in range(n-1,-1,-1):
        if(C[i].y > ymax):
            ymax = C[i].y
            pmaximais[k] = C[i];k=k+1
    
    return pmaximais,k

def heapSortPontosCrescenteX(A,n): #O(n*lg(n))
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
    if(esq < tamVetor and A[esq].x > A[i].x):
        maior = esq
    else:
        maior = i
    if(dir < tamVetor and A[dir].x > A[maior].x):
        maior = dir
    if(maior != i):
        A[i],A[maior] = A[maior],A[i]
        heapifyMax(A,maior,tamVetor)

def rearranjarMaxHeap(A,n):
    pai = 0
    filho = 1
    while(filho<=n-1):
        if(filho!=n-1 and A[filho].x<A[filho+1].x):
            filho=filho+1
        if(A[filho].x > A[pai].x):
            A[pai],A[filho]=A[filho],A[pai]
            pai=filho
            filho=(2*filho)+1
        else:
            filho = n

C = [Ponto(2,4),Ponto(4,4),Ponto(5.1,3),Ponto(1.1,0.2),Ponto(3.3,5.2)]
pmaximais,k = maximais(C,len(C))
print("\nMaximais:")
for i in range(0,k):
    print(pmaximais[i].x,pmaximais[i].y)