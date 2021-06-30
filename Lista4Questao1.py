#Lista semanal de PAA - Lista 4 Questão 1
#Aluno: João Paulo Feitosa Secundo
import random
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

def testarSomas(S,T,tamS,tamT,z):
    mergeSort(T,0,tamT-1)
    for i in range (0,tamS):
        dif = z - S[i]
        termo2 = buscaBinaria(T,0,tamT-1,dif)
        if(termo2 != -1):
            print(S[i],"+", T[termo2],"=",z)
            return True
    return False


S = random.sample(range(-20,20),8) #VETOR DE 8 ELEMENTOS ALEATORIOS
T = random.sample(range(-20,30),10) #VETOR DE 10 ELEMENTOS ALEATORIOS
intAleatorio = random.randint(-50,50) #INTEIRO ALEATORIO

print("VETOR S:",S)
print("VETOR T:",T)
print("SOMA PROCURADA:",intAleatorio)

teste = testarSomas(S,T,len(S),len(T),intAleatorio)
print(teste)