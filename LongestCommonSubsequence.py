class nodeLCS:
    def __init__(self,tam=0,dir='') -> None:
        self.tam = tam
        self.dir = dir


def LongaSubseqComum(X,m,Y,n,LCS):
    #ANTES DA CHAMADA:
    #m = len(X)+1
    #n = len(Y)+1
    #LCS = [None]*m
    #for i in range(0,m):
    #    LCS[i] = [None]*n
    #for i in range(0,m):
    #    for j in range(0,n):
    #        LCS[i][j] = nodeLCS()
    
    #casos base
    for i in range(0,m):
        LCS[i][0].tam = 0
        LCS[i][0].dir = '*'
    for j in range(0,n):
        LCS[0][j].tam = 0
        LCS[0][j].dir = '*'

    #caso geral
    for i in range(1,m):
        for j in range(1,n):
            if(X[i-1] == Y[j-1]):
                LCS[i][j].tam = 1 + LCS[i-1][j-1].tam
                LCS[i][j].dir = 'D'
            else:
                if(LCS[i-1][j].tam >= LCS[i][j-1].tam):
                    LCS[i][j].tam = LCS[i-1][j].tam
                    LCS[i][j].dir = 'A'
                else:
                    LCS[i][j].tam = LCS[i][j-1].tam
                    LCS[i][j].dir = 'E'
    
    for i in range(0,m):
        for j in range(0,n):
            print(LCS[i][j].tam,end='-')
            print(LCS[i][j].dir,end=' ')
        print()

def printLCS(LCS,i,j,X):
    #printLCS(LCS,m-1,n-1,X)
    if not(i==0 or j==0):
        if(LCS[i][j].dir == 'D'):
            printLCS(LCS,i-1,j-1,X)
            print(X[i-1])
        elif(LCS[i][j].dir == 'A'):
            printLCS(LCS,i-1,j,X)
        else:
            printLCS(LCS,i,j-1,X)

X = "xcxagx"
Y = "gcagf"
#X = "abcbdab"
#Y = "bcdb"
m = len(X)+1
n = len(Y)+1
LCS = [None]*m
for i in range(0,m):
    LCS[i] = [None]*n

for i in range(0,m):
        for j in range(0,n):
            LCS[i][j] = nodeLCS()

LongaSubseqComum(X,m,Y,n,LCS)
print("Size of LCS: ",LCS[m-1][n-1].tam)
printLCS(LCS,m-1,n-1,X)