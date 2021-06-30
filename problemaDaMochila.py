class nodeMochila():
    def __init__(self,e=0,p=0) -> None:
        self.existe = e
        self.pertence = p

class nodeItem():
    def __init__(self,v,p) -> None:
        self.valor = v
        self.peso = p

def printMochila(M,n,K):
    for i in range(0,n):
        for j in range(0,K):
            print(M[i][j].existe,end='-')
            print(M[i][j].pertence,end=' ')
        print()

def getItensMochila(S,n,K,M):
    w = K
    for i in range(n,0,-1):
        if(M[i-1][w-1].pertence):
            print(S[i-1].valor,"-",S[i-1].peso)
            w = w - S[i-1].peso


def mochila(S,n,K,M):
    M[0][0].existe = 1
    for j in range(1,K):
        M[0][j].existe = 0
    for i in range(1,n):
        for j in range(0,K):
            M[i][j].existe = 0
            if(M[i-1][j].existe):
                M[i][j].existe = 1
                M[i][j].pertence = 0
            elif (j - S[i].peso >= 0):
                if (M[i-1][j-S[i].peso].existe):
                    M[i][j].existe = 1
                    M[i][j].pertence = 1
    return M

#(valor,peso)
S = [nodeItem(7,5),nodeItem(10,7),nodeItem(8,2),nodeItem(5,3)]
n = len(S)
K = 13 #por algum motivo, K é como se fosse 12 para o problema (3+2+7=12)
M = [None]*n
for i in range(0,n):
    M[i] = [None]*K
for i in range(0,n):
        for j in range(0,K):
            M[i][j] = nodeMochila()

#python is pass-by-reference, so M is altered
mochila(S,n,K,M)
printMochila(M,n,K)
getItensMochila(S,n,K,M)
