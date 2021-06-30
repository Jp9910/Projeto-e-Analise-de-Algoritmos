def knapsack(V,W,Wmax,n):
    T = [[0 for k in range(Wmax+1)] for l in range(n+1)]
    U = [[0 for k in range(Wmax+1)] for l in range(n+1)]
    for i in range(1,n+1):
        for w in range(0,Wmax+1):
            if(W[i-1] <= w):
                T[i][w] = max(T[i-1][w],V[i-1]+T[i-1][w-W[i-1]])
                U[i][w] = 1
            else:
                T[i][w] = T[i-1][w]
                U[i][w] = 0
    w = Wmax
    for i in range(n,0,-1):
        if(U[i][w]):
            print(V[i-1],"-",W[i-1])
            w = w - W[i-1]
    return T

def getItens(Wmax,U,W,V):
    w = Wmax
    for i in range(n,0,-1):
        if(U[i][w]):
            print(V[i],"-",W[i])
            w = w - W[i]

V = [100,35,50,65]
W = [1,5,7,4]
Wmax = 10
n = len(V)
T = knapsack(V,W,Wmax,n)
for i in range(0,n+1):
    print(T[i])
print(T[n][Wmax])