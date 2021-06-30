#Lista semanal de PAA - Lista 2 Questão 4
#Aluno: João Paulo Feitosa Secundo

def ordenarParImpar(vetor,tamanho):
    
    pares = []
    impares = []
    temp = 0

    for i in range (0 , tamanho):
        if (vetor[i] % 2 == 0):
            pares.append(vetor[i])
        else:
            impares.append(vetor[i])
    
    for i in range (0,int(tamanho/2)):
        for j in range (i+1,int(tamanho/2)):
            if pares[j] < pares[i]:
                temp = pares[i]
                pares[i] = pares[j]
                pares[j] = temp
            
            if impares[j] > impares[i]:
                temp = impares[i]
                impares[i] = impares[j]
                impares[j] = temp
    
    for i in range (0,tamanho,2):
        vetor[i] = pares.pop(0)
        vetor[i+1] = impares.pop(0)
        # OU:
        #vetor[i] = pares[int(i/2)]
        #vetor[i+1] = impares[int(i/2)]

    return vetor


vetor = [5,9,4,3,2,10,13,8]

vetor = ordenarParImpar(vetor,len(vetor))

print("resultado: ",vetor)

#Elabore um algoritmo para retornar o mesmo vetor
#com os elementos pares e ímpares alternados
#e com os pares em ordem crescente e os
#ímpares em ordem decrescente.