def BFSM(T,n,P,m):
#entrada: texto T de tamanho n e um padrão P de tamanho m
#saída: o menor índice (index) para o qual P ocorre em T ou -1 se não ocorrer
#Complexidade: O(m*n)
    i=0
    j=0
    index=-1
    qntOperacoes = 0
    print("n -",n,"m -",m)
    while(index == -1 and i < n):
        qntOperacoes+=1
        print("\ni -",i,"j -",j)
        if(P[j] == T[i]):
            print(1)
            j+=1
            i+=1
        else:
            print(2)
            i=i+1-j #HÁ necessidade de '-j' (exemplo onionions-onions)
            j=0
        if(j==m):
            index=i-m
        print("i -",i,"j -",j)
    print("quantidade de operações:",qntOperacoes)
    return index

#T = "xyxxyxyxyyxyxyxyyxyxyxx"
#P = "xyxyyxyxyxy"
T = "onionions"
P = "onions"
match = BFSM(T,len(T),P,len(P))
print(match)