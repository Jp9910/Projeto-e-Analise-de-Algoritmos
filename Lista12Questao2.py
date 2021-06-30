#Lista semanal de PAA - Lista 12 Questão 2
#Aluno: João Paulo Feitosa Secundo

def combinacao(n,X,el,total,parcelas,resultado):
    m = len(X)
    if(el>=m):
        return

    soma = total + X[el]
    parcelasSoma = parcelas.copy()
    parcelasSoma.append(str(X[el]))
    subt = total - X[el]
    parcelasSubt = parcelas.copy()
    parcelasSubt.append("-"+str(X[el]))
    
    if(soma == n):
        resultado.append(parcelasSoma)
    if(subt == n):
        resultado.append(parcelasSubt)
        
    for i in range(1,m):
        combinacao(n,X,el+i,soma,parcelasSoma,resultado)
        combinacao(n,X,el+i,subt,parcelasSubt,resultado)

def pos(n,X):
    m = len(X)
    parcelas = []
    resultado = []
    for i in range(0,m):
        combinacao(n,X,i,0,parcelas,resultado)
    print(len(resultado),"Resultados:")
    print(resultado)


X = [5,3,-6,2]
n=6
pos(n,X)
