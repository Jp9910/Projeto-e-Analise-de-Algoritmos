#Lista semanal de PAA - Lista 4 Questão 3
#Aluno: João Paulo Feitosa Secundo

import random
def particaoNulo (lista,tamanho):
    i = 0
    for j in range (0,tamanho):
        if (lista[j] < 0):
            lista[j], lista[i] = lista[i], lista[j]
            i = i + 1
    
    for j in range (i,tamanho):
        if (lista[j] == 0):
            lista[j], lista[i] = lista[i], lista[j]
            i = i + 1

vetor = random.sample(range(-50,50),15)
vetor.append(0)
vetor.append(0)
particaoNulo(vetor,len(vetor))

print(vetor)