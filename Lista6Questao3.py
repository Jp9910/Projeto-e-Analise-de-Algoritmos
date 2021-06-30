#Lista semanal de PAA - Lista 6 Questão 3
#Aluno: João Paulo Feitosa Secundo
def cas_palavras(T,n,Palavras):
    p = len(Palavras)
    colunas = [""]*n
    for j in range(0,n):
        for k in range(0,n):
            colunas[j] = colunas[j] + T[k][j] #Montando as colunas
    print(colunas)
    tamPalavras = [0]*p
    for i in range(0,p):
        print("--- Procurando",Palavras[i],"---")
        tamPalavras[i] = len(Palavras[i])
        for j in range(0,n):
            resultado = horspool(T[j],n,Palavras[i],tamPalavras[i])
            if(resultado != -1):
                print("Encontrado \""+Palavras[i]+"\" na linha",j,"coluna",resultado\
                    ,"terminando na coluna",resultado+tamPalavras[i]-1,"linha",j)
            resultado = horspool(colunas[j],n,Palavras[i],tamPalavras[i])
            if(resultado != -1):
                print("Encontrado \""+Palavras[i]+"\" na coluna",j,"linha",resultado\
                    ,"terminando na linha",resultado+tamPalavras[i]-1,"coluna",j)

def horspool(T,n,P,m):
    D = { #dicionario do alfabeto inicialmente com deslocamento do tamanho do padrao
        "A":m,"B":m,"C":m,"D":m,"E":m,"F":m,"G":m,"H":m,"I":m,"J":m,"K":m,"L":m,"M":m,
        "N":m,"O":m,"P":m,"Q":m,"R":m,"S":m,"T":m,"U":m,"V":m,"W":m,"X":m,"Y":m,"Z":m
    }
    calcularDeslocamento(P,m,D)
    i=m-1;index=-1
    #print(T,"--",n)
    #print(P,"--",m)
    while(i<=n-1):
        k=0
        while(k<=m-1 and P[m-1-k] == T[i-k]):
            k=k+1
        if(k==m):
            index = i-m+1
            i=i+D[T[i]]
        else:
            i=i+D[T[i]]
    return index

def calcularDeslocamento(P,m,D):
    for j in range(0,m-1):
        D[P[j]] = m-1-j

T = ["LMPORCOBGCA","EMYKVACAGAL","BMACACOMALP","RLLMATNGAMA","ELEPATNMACT"\
    ,"OURSTIFOCCO","MRUYYTXZEBR","NAUTICHZATC","PAMELHEUSAA","YLULHABIUSL"\
    ,"BCVABELHABA"]
Palavras = ["LEBRE","MACACO","ASDF","ORCA","PATO","PORCO","VACA"]
n = len(T)
cas_palavras(T,n,Palavras)