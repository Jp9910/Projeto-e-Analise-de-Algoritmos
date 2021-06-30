#Lista semanal de PAA - Lista 10 Questão 4
#Aluno: João Paulo Feitosa Secundo

class Ponto():
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y

def grahamProfundidade(P,n,profundidade,removidos,pontoAtual=0,z=0):

    print("-----")
    for a in range(0,n):
        print(P[a].x,P[a].y)
    print("------")
    if(n<3):
        for i in range(0,n):
            profundidade[pontoAtual] = z
            removidos[pontoAtual] = P[i]
        return
    trassarPoligonoSimples(P)
    #inicializar primeiros pontos de H
    H = [None]*n
    H[0] = P[0]; H[1] = P[1]; H[2] = P[2]; m = 2
    
    #construir o caminho
    for i in range(3,n):
        while(viraEsqOuDirPercorrendoPQeQR(H[m-1],H[m],P[i]) == 1):
            m=m-1 #vira a direita (maior que 180 graus). retroceder m
        m=m+1
        H[m] = P[i]
    
    for j in range(0,m+1):
        profundidade[pontoAtual] = z
        removidos[pontoAtual] = H[j]
        pontoAtual = pontoAtual + 1
        P.remove(H[j])
        n=n-1

    grahamProfundidade(P,n,profundidade,removidos,pontoAtual,z+1)

def trassarPoligonoSimples(pontos): #O(nlogn)
    def pontoExtremo(pontos,n): #O(n)
        extremo = 0
        for i in range(1,n):
            if(pontos[i].x > pontos[extremo].x) or ((pontos[i].x == pontos[extremo].x)and(pontos[i].y < pontos[extremo].y)):
                extremo = i
        return extremo
        
    def calcularSlope(slope,n): #O(n)
        slope[1] = (pontos[1].y - pontos[0].y)/(pontos[1].x-pontos[0].x)
        minSlope = slope[1]
        for i in range(2,n):
            slope[i] = (pontos[i].y - pontos[0].y)/(pontos[i].x - pontos[0].x)
            if(slope[i] < minSlope):
                minSlope = slope[i]
        return minSlope

    n = len(pontos)
    slope = [0]*n
    extremo = pontoExtremo(pontos,n)
    pontos[extremo],pontos[0] = pontos[0],pontos[extremo]
    minSlope = calcularSlope(slope,n)
    slope[0] = minSlope - 1
    heapSortSlope(slope,n,pontos) #O(nlogn)

def heapSortSlope(A,n,pontos): #O(n*lg(n))
    montarHeapMaximo(A,n,pontos)
    for i in range(n-1,0,-1):
        A[0],A[i]=A[i],A[0]
        pontos[0],pontos[i]=pontos[i],pontos[0]
        rearranjarMaxHeap(A,i,pontos)

def montarHeapMaximo(A,tamVetor,pontos):
    metade = (tamVetor)//2
    for i in range(metade-1,-1,-1):
        heapifyMax(A,i,tamVetor,pontos)

def heapifyMax(A,i,tamVetor,pontos):
    esq = (2*i)+1
    dir = (2*i)+2
    if(esq < tamVetor and A[esq] > A[i]):
        maior = esq
    else:
        maior = i
    if(dir < tamVetor and A[dir] > A[maior]):
        maior = dir
    if(maior != i):
        A[i],A[maior] = A[maior],A[i]
        pontos[i],pontos[maior] = pontos[maior],pontos[i]
        heapifyMax(A,maior,tamVetor,pontos)

def rearranjarMaxHeap(A,n,pontos):
    pai = 0
    filho = 1
    while(filho<=n-1):
        if(filho!=n-1 and A[filho]<A[filho+1]):
            filho=filho+1
        if(A[filho] > A[pai]):
            A[pai],A[filho]=A[filho],A[pai]
            pontos[pai],pontos[filho]=pontos[filho],pontos[pai]
            pai=filho
            filho=(2*filho)+1
        else:
            filho = n

def viraEsqOuDirPercorrendoPQeQR(p,q,r):
    produtoVetorial = produtoVetorialAPxBQ(p,r,p,q)
    if(produtoVetorial > 0):
        return 1
    elif(produtoVetorial < 0):
        return -1
    else: return 0

def produtoVetorialAPxBQ(a,p,b,q):
    return ((p.x-a.x) * (q.y-b.y)) - ((q.x-b.x)*(p.y-a.y))

pontos = [Ponto(-1,2),Ponto(-1,-1),Ponto(1,0),Ponto(2,2),Ponto(2,-2),Ponto(3,3),Ponto(4,0),Ponto(3,-3),Ponto(3,0),Ponto(2,0),Ponto(1.5,-0.5),Ponto(2,0.5),Ponto(2.5,-0.5)]
n=len(pontos)
removidos = [None]*n
profundidade = [None]*n
grahamProfundidade(pontos,n,profundidade,removidos)
print("\nProfundidade dos pontos:")
for i in range(0,len(profundidade)):
    print("Ponto (",removidos[i].x,removidos[i].y,") -- profundidade:",profundidade[i])