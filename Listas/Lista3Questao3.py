import math

def buscaTernaria(vetor,esq,dir,valor) -> int:
    
    if(dir == esq):
        if (vetor[esq] == valor):
            return esq
        else:
            return -1
    else:
        dif = math.floor((dir-esq)/3)
        terco2 = (esq+dif)
        terco3 = (dir-dif)
        
        if(valor < vetor[terco2 +1]):
            #está no primeiro terço
            return buscaTernaria(vetor,esq,terco2,valor)
        if(valor > vetor [terco2] and valor < vetor[terco3]):
            #está no segundo terço
            return buscaTernaria(vetor,terco2 +1,terco3 -1,valor)
        if(valor > vetor[terco3 -1]):
            #está no terceiro terço
            return buscaTernaria(vetor,terco3,dir,valor)

vetor = [1,3,4,6,9,15,19,20,23,26,30,31]

busca1 = buscaTernaria(vetor,0,len(vetor)-1,1)
print(busca1)
busca3 = buscaTernaria(vetor,0,len(vetor)-1,3)
print(busca3)
busca4 = buscaTernaria(vetor,0,len(vetor)-1,4)
print(busca4)
busca6 = buscaTernaria(vetor,0,len(vetor)-1,6)
print(busca6)
busca9 = buscaTernaria(vetor,0,len(vetor)-1,9)
print(busca9)
busca15 = buscaTernaria(vetor,0,len(vetor)-1,15)
print(busca15)
busca19 = buscaTernaria(vetor,0,len(vetor)-1,19)
print(busca19)
busca20 = buscaTernaria(vetor,0,len(vetor)-1,20)
print(busca20)
busca23 = buscaTernaria(vetor,0,len(vetor)-1,23)
print(busca23)
busca26 = buscaTernaria(vetor,0,len(vetor)-1,26)
print(busca26)
busca30 = buscaTernaria(vetor,0,len(vetor)-1,30)
print(busca30)
busca31 = buscaTernaria(vetor,0,len(vetor)-1,31)
print(busca31)
busca0 = buscaTernaria(vetor,0,len(vetor)-1,0)
print(busca0)
busca10 = buscaTernaria(vetor,0,len(vetor)-1,10)
print(busca10)
busca55 = buscaTernaria(vetor,0,len(vetor)-1,55)
print(busca55)