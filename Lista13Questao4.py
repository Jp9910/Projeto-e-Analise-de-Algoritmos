#Lista semanal de PAA - Lista 13 Questão 4
#Aluno: João Paulo Feitosa Secundo
import random

def quickSortRand(vetor,esq,dir): #chamar com len(vetor)-1
    if (esq < dir):
        pos = particao(vetor,esq,dir)
        quickSortRand(vetor,esq,pos-1)
        quickSortRand(vetor,pos+1,dir)

def particao (vetor,inicio,fim):
    pivot = random.randint(inicio,fim)
    vetor[inicio],vetor[pivot] = vetor[pivot],vetor[inicio]
    pivot = inicio
    i = inicio+1
    j = 0
    for j in range (inicio+1,fim+1):
        if (vetor[j] <= vetor[pivot]):
            vetor[j], vetor[i] = vetor[i], vetor[j]
            i = i + 1
    vetor[pivot],vetor[i-1] = vetor[i-1], vetor[pivot]
    pivot = i-1
    return pivot

vetor = [0,5,-1,0,2,-4,0,1]
vetor = random.sample(range(1,1000),20)

quickSortRand(vetor,0,len(vetor)-1)

print(vetor)