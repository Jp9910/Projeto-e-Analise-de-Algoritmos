import random

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

    for a in range(0,tamAuxEsq): #Preencher vetores auxiliar
        auxEsq[a] = X[esq+a]
    for a in range(0,tamAuxDir):
        auxDir[a] = X[metade+1+a]

    while(i < tamAuxEsq and j < tamAuxDir): #Intercalar - Para quando aux esquerdo ou direito termina
        if(auxEsq[i] < auxDir[j]): #Pega a cabeça com menor valor e põe no inicio (k)
            X[k] = auxEsq[i]
            i=i+1 #avança cabeça
        else:
            X[k] = auxDir[j]
            j=j+1 #avança cabeça

        k=k+1 #avança o ultimo ordenado

    while(i < tamAuxEsq): #Preenche o restante
        X[k] = auxEsq[i]
        i=i+1
        k=k+1
    while(j < tamAuxDir): #Preenche o restante
        X[k] = auxDir[j]
        j=j+1
        k=k+1

teste = random.sample(range(1,100),20)
print("\nVETOR INICIAL: ",teste)
mergeSort(teste,0,len(teste)-1)
print("\nORDENADO: ",teste)