import math
import copy
class Ponto():
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y

"""
def pontosProximos(pontos,esq,dir):
    if(dir - esq < 3):
        return math.sqrt(((pontos[dir].x-pontos[esq].x)**2)+((pontos[dir].y-pontos[esq].y)**2))
    n=dir-esq+1
    X = [None]*n
    Y = [None]*n
    XL = [None]*(n//2)
    XR = [None]*(n//2)
    YL = [None]*(n//2)
    YR = [None]*(n//2)
    for i in range(0,n):
        X[i] = pontos[i+esq]
        Y[i] = pontos[i+esq]
    heapSortPontosCrescenteX(X,n)
    heapSortPontosCrescenteY(Y,n)
    meio = (esq+dir)//2
    for i in range(esq,meio):
        XL[i] = X[i]
    for i in range(meio+1,dir):
        XR[i] = X[i]
    
    k=0;l=0
    for i in range(0,n):
        if(Y[i].x < X[meio].x or (Y[i].x == X[meio].x and Y[i].y <= X[meio].y)):
            YL[k] = Y[i]
            k=k+1
        else:
            YR[l] = Y[i]
            l=l+1
    
    pontosProximos(YL,)
    pontosProximos(YR,)
"""

def dist(p1, p2):
    return math.sqrt((p1.x - p2.x) *
                     (p1.x - p2.x) +
                     (p1.y - p2.y) *
                     (p1.y - p2.y))
 
# A Brute Force method to return the
# smallest distance between two Pontos
# in P[] of size n
def bruteForce(P, n):
    min_val = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            if dist(P[i], P[j]) < min_val:
                min_val = dist(P[i], P[j])
 
    return min_val
 
# A utility function to find the
# distance beween the closest Pontos of
# strip of given size. All Pontos in
# strip[] are sorted accordint to
# y coordinate. They all have an upper
# bound on minimum distance as d.
# Note that this method seems to be
# a O(n^2) method, but it's a O(n)
# method as the inner loop runs at most 6 times
def stripClosest(strip, size, d):
     
    # Initialize the minimum distance as d
    min_val = d
 
    
    # Pick all Pontos one by one and
    # try the next Pontos till the difference
    # between y coordinates is smaller than d.
    # This is a proven fact that this loop
    # runs at most 6 times
    for i in range(size):
        j = i + 1
        while j < size and (strip[j].y -
                            strip[i].y) < min_val:
            min_val = dist(strip[i], strip[j])
            j += 1
 
    return min_val
 
# A recursive function to find the
# smallest distance. The array P contains
# all Pontos sorted according to x coordinate
def closestUtil(P, Q, n):
     
    # If there are 2 or 3 Pontos,
    # then use brute force
    if n <= 3:
        return bruteForce(P, n)
 
    # Find the middle Ponto
    mid = n // 2
    midPonto = P[mid]
 
    #keep a copy of left and right branch
    Pl = P[:mid]
    Pr = P[mid:]
 
    # Consider the vertical line passing
    # through the middle Ponto calculate
    # the smallest distance dl on left
    # of middle Ponto and dr on right side
    dl = closestUtil(Pl, Q, mid)
    dr = closestUtil(Pr, Q, n - mid)
 
    # Find the smaller of two distances
    d = min(dl, dr)
 
    # Build an array strip[] that contains
    # Pontos close (closer than d)
    # to the line passing through the middle Ponto
    stripP = []
    stripQ = []
    lr = Pl + Pr
    for i in range(n):
        if abs(lr[i].x - midPonto.x) < d:
            stripP.append(lr[i])
        if abs(Q[i].x - midPonto.x) < d:
            stripQ.append(Q[i])
 
    stripP.sort(key = lambda Ponto: Ponto.y) #<-- REQUIRED
    min_a = min(d, stripClosest(stripP, len(stripP), d))
    min_b = min(d, stripClosest(stripQ, len(stripQ), d))
     
     
    # Find the self.closest Pontos in strip.
    # Return the minimum of d and self.closest
    # distance is strip[]
    return min(min_a,min_b)
 
def closest(P, n):
    heapSortPontosCrescenteX(P,n)
    Q = copy.deepcopy(P)
    heapSortPontosCrescenteY(Q,n) 

    return closestUtil(P, Q, n)

def heapSortPontosCrescenteX(A,n): #O(n*lg(n))
    montarHeapMaximoX(A,n)
    for i in range(n-1,0,-1):
        A[0],A[i]=A[i],A[0]
        rearranjarMaxHeapX(A,i)

def montarHeapMaximoX(A,tamVetor):
    metade = (tamVetor)//2
    for i in range(metade-1,-1,-1):
        heapifyMaxX(A,i,tamVetor)

def heapifyMaxX(A,i,tamVetor):
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
        heapifyMaxX(A,maior,tamVetor)

def rearranjarMaxHeapX(A,n):
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


#----------------------------------------#

def heapSortPontosCrescenteY(A,n): #O(n*lg(n))
    montarHeapMaximoY(A,n)
    for i in range(n-1,0,-1):
        A[0],A[i]=A[i],A[0]
        rearranjarMaxHeapY(A,i)

def montarHeapMaximoY(A,tamVetor):
    metade = (tamVetor)//2
    for i in range(metade-1,-1,-1):
        heapifyMaxY(A,i,tamVetor)

def heapifyMaxY(A,i,tamVetor):
    esq = (2*i)+1
    dir = (2*i)+2
    if(esq < tamVetor and A[esq].y > A[i].y):
        maior = esq
    else:
        maior = i
    if(dir < tamVetor and A[dir].y > A[maior].y):
        maior = dir
    if(maior != i):
        A[i],A[maior] = A[maior],A[i]
        heapifyMaxY(A,maior,tamVetor)

def rearranjarMaxHeapY(A,n):
    pai = 0
    filho = 1
    while(filho<=n-1):
        if(filho!=n-1 and A[filho].y < A[filho+1].y):
            filho=filho+1
        if(A[filho].y > A[pai].y):
            A[pai],A[filho]=A[filho],A[pai]
            pai=filho
            filho=(2*filho)+1
        else:
            filho = n


P = [Ponto(0,0),Ponto(1,5),Ponto(6,6),Ponto(5,7),Ponto(-1,2),Ponto(-1,-1),Ponto(1,0),Ponto(2,2),Ponto(2,-2),Ponto(3,3),Ponto(4,0),Ponto(3,-3)]

n = len(P)
print("The smallest distance is",closest(P, n))