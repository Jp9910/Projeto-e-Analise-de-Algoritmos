def coinRow(valores,n):
    F = [None]*n
    cond = [None]*n
    indices = [None]*(n//2)
    k=0
    F[0] = 0
    F[1] = valores[1]
    for i in range(2,n):
        if(valores[i]+F[i-2] >= F[i-1]):
            F[i] = valores[i]+F[i-2]
            cond[k] = 0
            k=k+1
        else:
            F[i] = F[i-1]
            cond[k] = 1
            k=k+1
    a=0
    k=k-1
    #print(k)
    for i in range(n-1,0,-2):
        if(cond[k] == 0):
            indices[a] = i
            a=a+1
            k=k-2
        else:
            indices[a] = i-1
            a=a+1
            k=k-2
    #print(cond)
    #print(F)
    print("indices dos itens que compoem a soluçao:",indices)
    return F[n-1]

#valores = ['*',7,5,1,5,8,9,10,11]
valores = ['*',5,1,2,10,6,2]
n = len(valores)
valor = coinRow(valores,n)
print("solução:",valor)