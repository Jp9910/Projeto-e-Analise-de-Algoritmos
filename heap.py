import random
def heapSort(A,n): #O(n*lg(n))
    montarHeapMaximo(A,n)
    print("heapSort heap montado: ",A)
    for i in range(n-1,0,-1):
        A[0],A[i]=A[i],A[0]
        rearranjarMaxHeap(A,i)
        print("heap rearranjado: ",A)

def deletarNo(A,n,i):
    if(i>=n):
        print("No invalido")
        return
    else:
        print("Removendo o no", A[i])
        A[i],A[n-1]=A[n-1],A[i]
        A.pop(n-1)
        n=n-1
        rearranjarMaxHeap(A,n)

def inserirHeapMax(A,n,el):
    print("inserindo",el)
    n=n+1
    A.append(el)
    filho = n-1
    pai = (n-2)//2
    while(pai>=0):
        print(A);print(A[pai],A[filho])
        if(A[pai]<A[filho]):
            A[pai],A[filho] = A[filho], A[pai]
            filho = pai
            pai = (pai-1)//2
        else:
            pai=-1
    print("inserido")

def popHeapMax(A,n):
    if(n==0):
        print("Heap Vazio")
        return
    else:
        print("Removendo a raiz", A[0])
        A[0],A[n-1]=A[n-1],A[0]
        A.pop(n-1)
        n=n-1
        rearranjarMaxHeap(A,n)

def rearranjarMaxHeap(A,n):
    pai = 0
    filho = 1
    while(filho<=n-1):
        print(A);print(A[pai],A[filho])
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
    print(A[i],end="-")
    if(esq<tamVetor):
        print(A[esq],end="-")
    if(dir <tamVetor):
        print(A[dir])
    else:
        print("")
    if(esq < tamVetor and A[esq] > A[i]):
        maior = esq
    else:
        maior = i

    if(dir < tamVetor and A[dir] > A[maior]):
        maior = dir
    
    if(maior != i):
        A[i],A[maior] = A[maior],A[i]
        print("maior!=i",heap)
        heapifyMax(A,maior,tamVetor)

heap = [8,7,4,1,21,10]
#heap = [1,2,3,0,9,7,10]
#heap3 = [4,10,38,16,24,14,17,29,12,3,5,23,20,1,13]
montarHeapMaximo(heap,len(heap))
#montarHeapMaximo(heap2,len(heap2))
#montarHeapMaximo(heap3,len(heap3))
print(heap)
#print(heap2)
#print(heap3)
inserirHeapMax(heap,len(heap),20)
inserirHeapMax(heap,len(heap),2)
inserirHeapMax(heap,len(heap),9)
inserirHeapMax(heap,len(heap),31)
inserirHeapMax(heap,len(heap),12)
inserirHeapMax(heap,len(heap),25)
inserirHeapMax(heap,len(heap),5)
popHeapMax(heap,len(heap))
print(heap)
popHeapMax(heap,len(heap))
print(heap)
popHeapMax(heap,len(heap))
print(heap)
popHeapMax(heap,len(heap))
print(heap)
deletarNo(heap,len(heap),3)
print(heap)
deletarNo(heap,len(heap),4)
print(heap)

testeHeapSort = random.sample(range(0,50),15)
heapSort(testeHeapSort,len(testeHeapSort))
print("Ordenado:",testeHeapSort)

#O heapsort primeiramente organiza o vetor como um heap: O(n)
#Em seguida tem-se o maior elemento como a raiz
#Para i=1 até n...
#Troca-se a raiz para coloca-la em seu lugar definitivo (n-i) no final do vetor: O(1)
#Rearranja o heap excluindo os últimos i elementos: O(log(n))
#Fazendo o mesmo processo para todos os n elementos no heap: O(n*log(n))