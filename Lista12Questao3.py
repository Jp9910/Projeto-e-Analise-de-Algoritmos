#Lista semanal de PAA - Lista 12 Questão 3
#Aluno: João Paulo Feitosa Secundo

def alocar(C,n):
    qntZeros = 0
    zeros = [[0]*n for i in range(n)]
    m3 = [[0]*n for i in range(n)]

    for i in range(0,n): #encontrar o mínimo e subtrair de cada linha
        menor=C[i][0]
        for j in range(0,n):
            if(C[i][j] < menor):
                menor=C[i][j]
        for j in range(0,n):
            C[i][j] = C[i][j]-menor
            #if(C[i][j]==0 and menor != 0):
            #    qntZeros = qntZeros + 1
            #    zeros.append((i,j))

    for i in range(0,n): #encontrar o mínimo e subtrair de cada coluna
        menor=C[0][i]
        for j in range(0,n):
            if(C[j][i] < menor):
                menor=C[j][i]
        for j in range(0,n):
            C[j][i] = C[j][i]-menor
            #if(C[j][i]==0 and menor != 0):
            #    qntZeros = qntZeros + 1
            #    zeros.append((i,j))

    for i in range(0,n): #encontrar numero max de 0s horizontal ou verticalmente
        for j in range(0,n):
            if(C[i][j]==0):
                zeros[i][j] = hvMax(C,n,i,j)

    qntLinhas=0
    for i in range(0,n): #preencher a matriz que representa as linhas de acordo com os 0s máximos
        for j in range(0,n):
            if(abs(zeros[i][j]) > 0):
                matrizLinhas(zeros,m3,i,j,n)
                qntLinhas = qntLinhas+1
    
    while(qntLinhas != n): #caso o número de linhas seja diferente do número de pessoas/tarefas
        menor = 999999
        for i in range(0,n): #encontrar menor elemento fora das linhas
            for j in range(0,n):
                if(m3[i][j]==0 and C[i][j] < menor):
                    menor = C[i][j]
        
        for i in range(0,n): 
            for j in range(0,n):
                if(m3[i][j]==0):
                    C[i][j] = C[i][j]-menor #subtrair esse menor elemento dos outros fora das linhas
                if(m3[i][j]==1 and intersectingLines(m3,n,i,j)):
                    C[i][j] = C[i][j]+menor #somar esse menor elemento aos elementos interseptados por 2 linhas
        
        for i in range(0,n):
            for j in range(0,n):
                if(C[i][j]==0):
                    zeros[i][j] = hvMax(C,n,i,j)

        qntLinhas=0
        m3 = [[0]*n for i in range(n)]
        for i in range(0,n): #redesenhar linhas
            for j in range(0,n):
                if(abs(zeros[i][j]) > 0):
                    matrizLinhas(zeros,m3,i,j,n)
                    qntLinhas = qntLinhas+1

    poss = [0]*n
    for i in range(0,n):
        for j in range(0,n):
            if(C[i][j]==0):
                poss[i]=poss[i]+1
                #print("Pessoa",i+1,"pode fazer a tarefa",j+1)
    
    k=0
    alocado=[False]*n
    while(k<n):
        menorPoss=999999
        for i in range(0,n):
            if(poss[i]<menorPoss):
                menorPoss = poss[i]
                pessoa=i
        i=-1
        while(i<n):
            i=i+1
            if(C[pessoa][i]==0 and alocado[i]==False):
                print("Pessoa",pessoa+1,"deve fazer a tarefa",i+1)
                k=k+1
                alocado[i]=True
                poss[pessoa]=999999
                i=n

    #print(qntLinhas)
    print(C)
    print(zeros)
    print(m3)

def hvMax(C,n,lin,col):
    #returns maximum number of zeroes horizontal or vertical. 
    #(Positive number means vertical, negative number means horizontal)
    vertical=0
    horizontal=0
    for i in range(0,n):
        if(C[lin][i]==0):
            horizontal=horizontal+1
        if(C[i][col]==0):
            vertical=vertical+1
    
    if(vertical>horizontal):
        return vertical
    else:
        return horizontal*-1

def matrizLinhas(zeros,m3,lin,col,n):
    #void method, it will clear the horizontal neighbors if the value at row col 
    #indexes is negative, or clear vertical neighbors if positive. 
    # Moreover, it will set the line in the m3 array, by flipping the zero bit to 1.
    if(zeros[lin][col]>0):
        for i in range(0,n):
            if(zeros[i][col]>0):
                zeros[i][col]=0 #clear neighbour
            m3[i][col]=1 #draw line
    
    else:
        for i in range(0,n):
            if(zeros[lin][i]<0):
                zeros[lin][i]=0 #clear neighbour
            m3[lin][i]=1 #draw line
    
    zeros[lin][col]=0
    m3[lin][col]=1

def intersectingLines(m3,n,i,j):
    if(i>0):
        if(i<n-1):
            if(j>0):
                if(j<n-1):
                    if(m3[i-1][j]==1 and m3[i+1][j]==1 and m3[i][j+1]==1 and m3[i][j-1]==1):
                        return True
                else:#j=n-1
                    if(m3[i-1][j]==1 and m3[i+1][j]==1 and m3[i][j-1]==1):
                        return True
            else:#j=0
                if(m3[i-1][j]==1 and m3[i+1][j]==1 and m3[i][j+1]==1):
                        return True
        else:#i=n-1
            if(j>0):
                if(j<n-1):
                    if(m3[i-1][j]==1 and m3[i][j+1]==1 and m3[i][j-1]==1):
                        return True
                else:#j=n-1
                    if(m3[i-1][j]==1 and m3[i][j-1]==1):
                        return True
            else:#j=0
                if(m3[i-1][j]==1 and m3[i][j+1]==1):
                        return True
    else:#i=0
        if(j>0):
            if(j<n-1):
                if(m3[i+1][j]==1 and m3[i][j+1]==1 and m3[i][j-1]==1):
                    return True
            else:#j=n-1
                if(m3[i+1][j]==1 and m3[i][j-1]==1):
                    return True
        else:#j=0
            if(m3[i+1][j]==1 and m3[i][j+1]==1):
                return True
    
    return False


C = [[9,2,7,8],\
     [6,4,3,7],\
     [5,8,1,8],\
     [7,6,9,4]]

#C = [[2500,4000,3500],[4000,6000,3500],[2000,4000,2500]]

#C = [[1500,4000,4500],[2000,6000,3500],[2000,4000,2500]]

#C = [[0,1,0,1,1],[1,1,0,1,1],[1,0,0,0,1],[1,1,0,1,1],[1,0,0,1,0]]

alocar(C,len(C))