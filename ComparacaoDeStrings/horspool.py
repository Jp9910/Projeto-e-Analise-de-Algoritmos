def horspool(T,n,P,m):
    D = { #dicionario do alfabeto inicialmente com deslocamento do tamanho do padrao
        "a":m,"b":m,"c":m,"d":m,"e":m,"f":m,"g":m,"h":m,"i":m,"j":m,"k":m,"l":m,"m":m,
        "n":m,"o":m,"p":m,"q":m,"r":m,"s":m,"t":m,"u":m,"v":m,"w":m,"x":m,"y":m,"z":m,
        "A":m,"B":m,"C":m,"D":m,"E":m,"F":m,"G":m,"H":m,"I":m,"J":m,"K":m,"L":m,"M":m,
        "N":m,"O":m,"P":m,"Q":m,"R":m,"S":m,"T":m,"U":m,"V":m,"W":m,"X":m,"Y":m,"Z":m,
        "1":m,"2":m,"3":m,"4":m,"5":m,"6":m,"7":m,"8":m,"9":m,"0":m,
    }
    #print(D["a"])
    calcularDeslocamento(P,m,D)
    i=m-1;index=-1;
    print(T,"--",n)
    print(P,"--",m)
    comparacoes = 0
    while(i<=n-1):
        k=0
        #print(P[m-1-k],"(",m-1-k,")", T[i-k],"(",i-k,")")
        comparacoes+=1
        while(k<=m-1 and P[m-1-k] == T[i-k]):
            comparacoes+=1
            k=k+1
        if(k==m):
            index = i-m+1
            print("Encontrado no indice",index)
            i=i+D[T[i]]
        else:
            i=i+D[T[i]]
    print("comparacoes feitas:",comparacoes)
    return index

def calcularDeslocamento(P,m,D):
    for j in range(0,m-1):
        D[P[j]] = m-1-j
    print(D)

T = "zensaz"*1000
P = "mensal"
n = len(T)
m = len(P)
resultado = horspool(T,n,P,m)
#print(resultado)