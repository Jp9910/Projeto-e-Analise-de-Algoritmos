def corte(V,n,Wmax):
    #W = Weight = Tamanho do pao será representado pelo indice de V
    #V = valor do pedaço de pao
    #Wmax = peso máximo = tamanho original do pao
    Tab = [0 for k in range(Wmax+1)]
    for i in range(1,Wmax+1): #todosOsPesos
        for j in range (0,n):#qntDeValores
            if(j <= i): #apenas considera os paes de tamanho menor que o maximo
                Tab[i] = max(Tab[i],V[i-j]+V[j])
    print(Tab)
    return Tab


precos = [0,1,5,8,9,10,11,17,20]
n=len(precos)
#tamanhos = [1,2,3,4,5,6,7,8]
#m=len(tamanhos)
tamanhoOriginal = 6
r = corte(precos,n,tamanhoOriginal)
print(r[tamanhoOriginal])