
def segundoMenorElemento(vetor) -> int:
    #O(n)
    if(vetor[0] < vetor[1]):
        menor=vetor[0]
        segMenor=vetor[1]
    else:
        menor = vetor[1]
        segMenor = vetor[0]
    
    for i in range(2,len(vetor)):
        if(vetor[i] < menor):
            segMenor = menor
            menor = vetor[i]
        elif (vetor[i] < segMenor):
            segMenor = vetor[i]
    
    print("menor elemento:",menor)
    print("seg menor:",segMenor)
        

vetor = [2,1,6,3,0,4,5,4,6]

segundoMenorElemento(vetor)