#Lista semanal de PAA - Lista 6 Questão 4
#Aluno: João Paulo Feitosa Secundo
def horspool(T,n,P,m):
    D = {
        "a":m,"b":m,"c":m,"d":m,"e":m,"f":m,"g":m,"h":m,"i":m,"j":m,"k":m,"l":m,"m":m,
        "n":m,"o":m,"p":m,"q":m,"r":m,"s":m,"t":m,"u":m,"v":m,"w":m,"x":m,"y":m,"z":m
    }
    calcularDeslocamento(P,m,D)
    i=m-1;indexFim=-1;indexIni=-1;maior=-1
    print(T,"--",n)
    print(P,"--",m)
    while(i<=n-1):
        k=0;cont=0;esq=-1
        while(k<=m-1):
            if(P[m-1-cont] == T[i-k]):
                cont+=1
                if(esq==-1): esq=k
            elif(esq!=-1):break
            k=k+1
        if(cont>0):
            if(cont>maior):
                maior=cont
                indexFim = i-esq #indice final
                indexIni = i-esq-cont+1 #indice inicial
            i=i+D[T[i]]
        else:
            i=i+D[T[i]]
    print("Maior sufixo encontrado tem tamanho",maior)
    print("--com inicio no indice",indexIni,"e fim no indice",indexFim)

def calcularDeslocamento(P,m,D):
    for j in range(0,m-1):
        D[P[j]] = m-1-j

T = "xxbaabaxxbaxbax"
P = "bababa"
#T = "xxxxxxabaabxxxxxxx"
#P = "ababa"
n = len(T)
m = len(P)
resultado = horspool(T,n,P,m)