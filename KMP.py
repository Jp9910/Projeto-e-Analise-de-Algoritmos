def KMP(padrao,texto):
    N = len(texto)
    M = len(padrao)
    lps = [0]*M
    calcularLPS(padrao,M,lps) #longest prefix that is also a sufix
    i=0;j=0
    passos=0
    while(i < N):
        passos+=1
        if(texto[i] == padrao[j]):
            i+=1
            j+=1
        else:
            if(j!=0):
                j=lps[j-1]
                passos+=1
            else:
                i+=1
        if(j==M):
            print(i-j)
            j=lps[j-1]
    print("passos:",passos)

def calcularLPS(padrao,m,lps):
    len=0
    i=1
    lps[0]=0
    while(i < m):
        if(padrao[i] == padrao[len]):
            lps[i] = len+1
            len+=1
            i+=1
        else:
            if(len!=0):
                len=lps[len-1]
            else:
                lps[i]=0
                i+=1

texto = "0"*1000
padrao = "0001"
KMP(padrao,texto)