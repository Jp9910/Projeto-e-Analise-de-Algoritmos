#Lista semanal de PAA - Lista 5 Questão 5
#Aluno: João Paulo Feitosa Secundo
#usar uma matriz pra lembrar a lista de origem do elemento no heap
class Node:
    def __init__(self,valor,origem) -> None:
        self.valor = valor
        self.origem = origem

def kWayMerge(A,k):
    heap = []
    final = []
    print("Sequencias:")
    print(A)
    for i in range(0,k):
        heap.append(Node(A[i].pop(0),i))
    montarHeapMinimo(heap,k)
    n=k
    while(n>0): #enquanto houver elementos no heap
        print(A)
        min = popHeapMin(heap,n)
        n=n-1
        final.append(min)
        if(not A[min.origem]): #se a sequencia de origem do elemento mínimo esvaziou
            pass #não podemos inserir o proximo elemento da sequencia no heap
        else: #caso contrário, inserimos seu proximo elemento no heap
            inserirHeapMin(heap,n,Node(A[min.origem].pop(0),min.origem))
            n=n+1
    return final
            
def montarHeapMinimo(A,tamVetor):
    metade = (tamVetor)//2
    for i in range(metade-1,-1,-1):
        heapifyMin(A,i,tamVetor)

def heapifyMin(A,i,tamVetor):
    esq = (2*i)+1
    dir = (2*i)+2
    if(esq < tamVetor and A[esq].valor < A[i].valor):
        menor = esq
    else:
        menor = i

    if(dir < tamVetor and A[dir].valor < A[menor].valor):
        menor = dir
    
    if(menor != i):
        A[i],A[menor] = A[menor],A[i]
        heapifyMin(A,menor,tamVetor)

def inserirHeapMin(A,n,el):
    n=n+1
    A.append(el)
    filho = n-1
    pai = (n-2)//2
    while(pai>=0):
        if(A[pai].valor>A[filho].valor):
            A[pai],A[filho] = A[filho], A[pai]
            filho = pai
            pai = (pai-1)//2
        else:
            pai=-1

def popHeapMin(A,n):
    if(n==0):
        print("Heap Vazio")
        return
    else:
        raiz = A[0]
        A[0],A[n-1]=A[n-1],A[0]
        A.pop(n-1)
        n=n-1
        rearranjarMinHeap(A,n)
        return raiz

def rearranjarMinHeap(A,n):
    pai = 0
    filho = 1
    while(filho<=n-1):
        if(filho!=n-1 and A[filho].valor > A[filho+1].valor):
            filho=filho+1
        if(A[filho].valor < A[pai].valor):
            A[pai],A[filho]=A[filho],A[pai]
            pai=filho
            filho=(2*filho)+1
        else:
            filho = n

#teste=[7,5,2,3,1,6,23,8,11,15]
#montarHeapMinimo(teste,len(teste))
#print(teste)
#popHeapMin(teste,len(teste))
#print(teste)
#inserirHeapMin(teste,len(teste),1)
#print(teste)
A=[[0,1,3,4,9,10],[4,5,6,10],[2,3,6,7,11]]
k=len(A)
merge = kWayMerge(A,k)
for i in range (0,len(merge)):
    print(merge[i].valor,end=', ')