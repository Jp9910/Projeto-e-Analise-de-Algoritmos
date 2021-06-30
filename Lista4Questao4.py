#Lista semanal de PAA - Lista 4 Questão 4
#Aluno: João Paulo Feitosa Secundo

import random
def quickSort (lista,inicio,fim):
    if (inicio < fim):
        pivot = particao(lista,inicio,fim)
        quickSort(lista,inicio,pivot-1)
        quickSort(lista,pivot+1,fim)

def particao (lista,inicio,fim):
    pivot = lista[fim]
    i = inicio
    for j in range (inicio,fim):
        if (lista[j] <= pivot):
            lista[j], lista[i] = lista[i], lista[j]
            i = i + 1
    lista[i],lista[fim] = lista[fim], lista[i] 
    return i

def quickSortDec (lista,inicio,fim):
    if (inicio < fim):
        pivot = particaoDec(lista,inicio,fim)
        quickSortDec(lista,inicio,pivot-1)
        quickSortDec(lista,pivot+1,fim)

def particaoDec (lista,inicio,fim):
    pivot = lista[fim]
    i = inicio
    for j in range (inicio,fim):
        if (lista[j] >= pivot):
            lista[j], lista[i] = lista[i], lista[j]
            i = i + 1
    lista[i],lista[fim] = lista[fim], lista[i] 
    return i

def particaoParImpar (lista,fim):
    i = 0
    for j in range (0,fim):
        if (lista[j] % 2 == 0):
            lista[j], lista[i] = lista[i], lista[j]
            i = i + 1
    lista[i],lista[fim] = lista[fim], lista[i]
    return i

def OrdenarParImpar (vetor,n):
    limite = particaoParImpar(vetor,n)
    if(vetor[limite] % 2 == 0):
        quickSort(vetor,0,limite)
        quickSortDec(vetor,limite+1,n)
    else:
        quickSort(vetor,0,limite-1)
        quickSortDec(vetor,limite,n)


vetor = random.sample(range(1,50),15)
OrdenarParImpar(vetor,len(vetor)-1)
print(vetor)