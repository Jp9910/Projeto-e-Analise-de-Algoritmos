def unboundKnapsack(V,W,Wmax,n):
    DP = [[0 for k in range(Wmax+1)] for l in range(n+1)]
    for i in range (1,n+1):
        for j in range(0,Wmax+1):
            if(j==0):
                DP[i][j] = 0
            elif(i==0 and j>0):
                DP[i][j]=-999999999
            elif(j-W[i-1] >= 0):
                DP[i][j] = max(DP[i-1][j],DP[i-1][j-W[i-1]]+V[i-1])
    return DP

V = [100,40,30,60,1]
W = [4  ,4 ,6 ,3 ,1]
Wmax = 10
n = len(V)
T = unboundKnapsack(V,W,Wmax,n)
print(T)
print(T[n][Wmax])