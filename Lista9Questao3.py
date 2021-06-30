def unboundKnapsack(V,W,Wmax,n):
    dp = [0 for i in range(Wmax+1)]
    for i in range(0,Wmax+1):
        for j in range(0,n):
            if(W[j] <= i):
                dp[i] = max(dp[i],dp[i-W[j]]+V[j])
    return dp

V = [100,40,30,60,1]
W = [4  ,4 ,6 ,3 ,1]
Wmax = 10
n = len(V)
T = unboundKnapsack(V,W,Wmax,n)
print(T)
print(T[Wmax])