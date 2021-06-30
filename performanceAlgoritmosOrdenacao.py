import random, time

def mergeSort (X,esq,dir):
    if(esq < dir):
        metade = (esq+dir)//2
        mergeSort(X,esq,metade)
        mergeSort(X,metade+1,dir)
        intercalar(X,esq,metade,dir)

def intercalar(X,esq,metade,dir):
    tamAuxEsq = metade - esq + 1
    tamAuxDir = dir - metade
    auxEsq = [None] * tamAuxEsq
    auxDir = [None] * tamAuxDir
    i = j = 0
    k = esq

    for a in range(0,tamAuxEsq):
        auxEsq[a] = X[esq+a]
    for a in range(0,tamAuxDir):
        auxDir[a] = X[metade+1+a]

    while(i < tamAuxEsq and j < tamAuxDir):
        if(auxEsq[i] < auxDir[j]):
            X[k] = auxEsq[i]
            i=i+1
        else:
            X[k] = auxDir[j]
            j=j+1

        k=k+1

    while(i < tamAuxEsq):
        X[k] = auxEsq[i]
        i=i+1
        k=k+1
    while(j < tamAuxDir):
        X[k] = auxDir[j]
        j=j+1
        k=k+1

def ordenar (vetor,n):
    quickSort(vetor,0,n)

def quickSort (vetor,esq,dir):
    if (esq < dir):
        pos = particao(vetor,esq,dir)
        quickSort(vetor,esq,pos-1)
        quickSort(vetor,pos+1,dir)

def particao (vetor,esq,dir):
    pivo = vetor[esq]
    left = esq
    right = dir
    while (left < right):
        while (left <= dir and vetor[left] <= pivo):
            left += 1
        while (right >= esq and vetor[right] > pivo):
            right -= 1
        if(left < right):
            aux = vetor[left]
            vetor[left] = vetor[right]
            vetor[right] = aux
    pos = right
    aux = vetor[esq]
    vetor[esq] = vetor[pos]
    vetor[pos] = aux
    return pos

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

#---SETUP---#
teste = random.sample(range(1,1000001),1000000)
#heapSort(teste,len(teste))

#---INICIO---#
start_time = time.time()

#mergeSort(teste,0,len(teste)-1)
#quickSort(teste,0,len(teste)-1)
heapSort(teste,len(teste))

print("--- %s seconds ---" % (time.time() - start_time))
#---FIM---#


#---ESTATÍSTICAS COLETADAS---#
#-----NÚMEROS DE 1 À 1milhão EM ORDEM ALEATÓRIA-------#
#quickSort se aprensentou o mais rápido em tempo médio para um vetor de tamanho 100mil e 1milhao
#       100mil: 0.26 segundos
#       1milhão: média de 3.4 segundos
#mergeSort foi mais rapido que heapSort para um vetor de tamanho 100mil
#       100mil: 0.52 segundos
#       1milhão: média de 7.0 segundos
#heapSort
#       100mil: 0.55 segundos (maior: 0.97)
#       1milhão: média de 7.8 segundos

#-----NÚMEROS DE 1 À 1milhão JÁ ORDENADOS-------#
#heapSort: 0.54XXX segundos
#mergeSort: 0.46XXX segundos
#quickSort: erro de recusão

#-----NÚMEROS DE 1 À 1milhão EM ORDEM CONTRÁRIA (DECRESCENTE)-------#
#