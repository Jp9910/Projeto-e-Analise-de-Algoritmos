import math

def buscarPico(vetor,esq,dir) -> int:
    if(esq==dir):
        return vetor[esq]
    else:
        metade = math.floor((esq+dir)/2)
        if(vetor[metade] < vetor[metade+1]):
            #sequencia ainda está crescendo
            return buscarPico(vetor,metade+1,dir)
        else:
            #ja parou de crescer
            return buscarPico(vetor,esq,metade)

vetor = [1,5,7,9,15,17,18,20,21,22,27,35,39,40,44,71,55,44,43,42,30,19,10]

pico = buscarPico(vetor,0,len(vetor)-1)

print(pico)