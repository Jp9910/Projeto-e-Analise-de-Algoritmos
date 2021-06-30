
def LCSubString(X,m,Y,n):
    #LongestCommonSubString
    LCSS = [[0 for k in range(n+1)] for l in range(m+1)]
    resultado = 0
    ind = -1
    for i in range(0,m+1):
        for j in range(0,n+1):
            if(i==0 or j==0):
                LCSS[i][j] = 0
            elif(X[i-1] == Y[j-1]):
                LCSS[i][j] = 1 + LCSS[i-1][j-1]
                if(LCSS[i][j] > resultado):
                    resultado = LCSS[i][j]
                    ind = i
            else:
                LCSS[i][j] = 0
    for i in range(0,m+1):
        for j in range(0,n+1):
            print(LCSS[i][j],end='')
        print()
    substring = ''
    for i in range(ind-resultado,ind):
        substring = substring+X[i]
    print("mais longa subcadeia de elementos consecutivos:",substring)
    print("indice da ultima letra em X:",ind)
    return resultado

X = "palavras sao dificeis preciso achar substrings"
Y = "asdf kicej jasdf jpalxz ojstrif xnja jifjs ksdu"
m = len(X)
n = len(Y)
r = LCSubString(X,m,Y,n)
print("tamanho:",r)