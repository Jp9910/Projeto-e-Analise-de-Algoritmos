#Lista semanal de PAA - Lista 6 Questão 1
#Aluno: João Paulo Feitosa Secundo
def KMP(padrao,texto,k,n):
    #n = len(texto)
    m = k
    lps = [0]*m
    calcularLPS(padrao,m,lps)
    i=0;j=0
    passos=0
    while(i < n):
        if(texto[i] == padrao[j]):
            i+=1
            j+=1
        else:
            if(j!=0):
                j=lps[j-1]
            else:
                i+=1
        if(j==m):
            print(i-j)
            j=lps[j-1]

def calcularLPS(padrao,m,lps):
    len=0
    i=1
    lps[0]=0
    while(i < m):
        if(padrao[i] == padrao[len]):
            len+=1
            lps[i] = len
            i+=1
        else:
            if(len!=0):
                len=lps[len-1]
            else:
                lps[i]=0
                i+=1

texto = "Vejam as araras e ararinhas azuis na arvore durante a viagem."
padrao = "ara"
k=2
KMP(padrao,texto,k,len(texto))