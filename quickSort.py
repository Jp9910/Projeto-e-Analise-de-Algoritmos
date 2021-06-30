
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

vetor = [0,5,-1,0,2,-4,0,1]

ordenar(vetor,len(vetor)-1)

print(vetor)