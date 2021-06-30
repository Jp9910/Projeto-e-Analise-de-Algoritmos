#Lista semanal de PAA - Lista 6 Questão 2
#Aluno: João Paulo Feitosa Secundo
def KMP(padrao,texto,m,n):
    lps = [0]*m
    calcularLPS(padrao,m,lps)
    i=0;j=0
    print("---",texto,n)
    print("---",padrao,m)
    while(i < n):
        #print("inicio")
        #print("i:",i)
        #print(texto[i],padrao[j])
        if(padrao[j] == "#"):
            #print("1")
            if(j+1!=m):
                return KMP(padrao[j+1:],texto[i:],m-j-1,n-i)
            else:
                return True
        elif(texto[i] == padrao[j]):
            #print("-2-",i,j)
            i+=1
            j+=1
        elif(i<n and texto[i] != padrao[j]):
            #print("3")
            if(j!=0):
                j=lps[j-1]
            else:
                i+=1
        if(j==m):
            print("Ocorre",i-j)
            return True
            j=lps[j-1]
    #print("teste final: ",padrao[j],j,m)
    if(padrao[j] == "#" and j+1 == m):
        return True
    else: return False

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

texto = "xxbcxxxxxxxabcxxb"
padrao = "#bc#abc#b#a"
#texto = "cabccbacbacab"
#padrao = "ab#ba#c"
n = len(texto)
m = len(padrao)
resultado = KMP(padrao,texto,m,n)
print("Resultado: ",resultado)