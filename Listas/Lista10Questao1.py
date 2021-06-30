#Lista semanal de PAA - Lista 10 Questão 1
#Aluno: João Paulo Feitosa Secundo

def linhaDoHorizonte(predios,esq,dir):
    if (esq==dir):
        return ((predios[esq][0],predios[esq][1]),(predios[esq][2],0))
    meio = (esq+dir)//2
    E = linhaDoHorizonte(predios,esq,meio)
    D = linhaDoHorizonte(predios,meio+1,dir)
    return mergeHorizonte(E,D)

def mergeHorizonte(E,D):
    i = j = 0
    z = 0
    tamEsq = len(E); tamDir = len(D)
    resultado = []*(tamEsq+tamDir)
    #intercalar
    altE=0;altD=0
    while(i < tamEsq and j < tamDir):
        if(E[i][0] < D[j][0]):
            altE = E[i][1]
            altmax = max(altE,altD)
            if(not checarRedundante((E[i][0],altmax),z,resultado)):
                resultado.append((E[i][0],altmax))
                z=z+1
            i=i+1
        else:
            altD = D[j][1]
            altmax = max(altE,altD)
            if(not checarRedundante((D[j][0],altmax),z,resultado)):
                resultado.append((D[j][0],altmax))
                z=z+1
            j=j+1

    while(i < tamEsq): #Preencher o restante
        resultado.append((E[i][0],E[i][1]))
        i=i+1
        z=z+1
    while(j < tamDir): #Preencher o restante
        resultado.append((D[j][0],D[j][1]))
        j=j+1
        z=z+1
    return resultado

def checarRedundante(S,z,resultado):
    if(z>0 and resultado[z-1][1] == S[1]):
        return True
    if(z>0 and resultado[z-1][0] == S[0]):
        resultado[z-1][1] = max(resultado[z-1][1],S[1])
        return True
    return False

input = [(1,11,5),(2,6,7),(3,13,9),(12,7,16),(14,3,25),(19,18,22),(23,13,29),(24,4,28)]
r = linhaDoHorizonte(input,0,len(input)-1)
print(r)

#output = [(1,11,3,13,9,0,12,7,16,3,19,18,22,3,23,13,29,0)]