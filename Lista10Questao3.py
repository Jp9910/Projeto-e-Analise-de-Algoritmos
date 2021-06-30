#Lista semanal de PAA - Lista 10 Questão 3
#Aluno: João Paulo Feitosa Secundo
class Ponto():
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y

class Reta():
    def __init__(self,a,b) -> None:
        self.ponto1 = a
        self.ponto2 = b

def maiorInclinacao(P,n):
    #inclinação é deltaY/deltaX, medida em relação ao eixo X como no polígono simples
    heapSortPontosCrescenteX(P,n)
    for i in range(0,n):
        print(P[i].x,P[i].y)

    pts = [0,1]
    if(P[1].x-P[0].x != 0):
        maiorInc = (P[1].y-P[0].y)/(P[1].x-P[0].x)
    for i in range(2,n):
        if(P[i].x-P[i-1].x != 0):
            proximaInc = (P[i].y-P[i-1].y)/(P[i].x-P[i-1].x)
        if(proximaInc > maiorInc): 
            maiorInc = proximaInc
            pts[0]=i-1;pts[1]=i
    print(pts)
    return maiorInc

def heapSortPontosCrescenteX(A,n): #O(n*lg(n))
    montarHeapMaximo(A,n)
    for i in range(n-1,0,-1):
        A[0],A[i]=A[i],A[0]
        rearranjarMaxHeap(A,i)

def montarHeapMaximo(A,tamVetor):
    metade = (tamVetor)//2
    for i in range(metade-1,-1,-1):
        heapifyMax(A,i,tamVetor)

def heapifyMax(A,i,tamVetor):
    esq = (2*i)+1
    dir = (2*i)+2
    if(esq < tamVetor and A[esq].x > A[i].x):
        maior = esq
    else:
        maior = i
    if(dir < tamVetor and A[dir].x > A[maior].x):
        maior = dir
    if(maior != i):
        A[i],A[maior] = A[maior],A[i]
        heapifyMax(A,maior,tamVetor)

def rearranjarMaxHeap(A,n):
    pai = 0
    filho = 1
    while(filho<=n-1):
        if(filho!=n-1 and A[filho].x<A[filho+1].x):
            filho=filho+1
        if(A[filho].x > A[pai].x):
            A[pai],A[filho]=A[filho],A[pai]
            pai=filho
            filho=(2*filho)+1
        else:
            filho = n

pontos = [Ponto(3,2),Ponto(2,2),Ponto(5,5),Ponto(6,4)]
r = maiorInclinacao(pontos,len(pontos))
print("Maior inclinação:",r)