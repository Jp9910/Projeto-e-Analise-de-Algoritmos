def posicaoValida(X,r,col) -> bool:
    #checa se a coluna col já foi utilizada por uma rainha de índice anterior a r
    #e também se a rainha k não ataca em diagonal a rainha r
    for k in range(1,r):
        if (X[k] == col) or (abs(X[k]-col) == abs(k-r)):
            return False
    return True

def NQ(i,n,X):
    #Entrada: rainha i, tamanho do tabuleiro n, solução X
    #Saída: X[0] indicando se tem solução (1) ou não (0). Caso sim, X[1..n] a armazena.
    for j in range(1,n+1):
        #verifica se pode alocar a rainha i na coluna j
        if(posicaoValida(X,i,j)):
            #colocar rainha i na coluna j
            X[i] = j
            #checar se já posicionou todas as rainhas ou se precisa continuar a busca
            if(i==n):
                X[0] = 1
                print(X)
                #para encontrar apenas a primeira solução, basta incluir
                #uma condiçao para parar (break no for) todas as recursoes caso X[0] == 1
            else:
                NQ(i+1,n,X) #prosseguir para alocar a proxima rainha

def nQueens(n):
    #Entrada: Tamanho do tabuleiro n
    #Saída: Solução armazenada em X[1..n] impressa, se existir alguma.
    #Posição 0 do vetor X indica se existe solução (1) ou não (0)
    X = [0]*(n+1)
    for i in range(0,n+1):
        X[i] = 0
    #NQ aplica backtracking para encontrar uma solução
    NQ(1,n,X)
    """
    if(X[0] == 1):
        print("Solução de ordem",n,":")
        for i in range(1,n+1):
            print(X[i],end='-')
    else:
        print("Não existe solução para um tabuleiro de ordem",n)
    """
    if(X[0]==0):
        print("Não existe solução para um tabuleiro de ordem",n)

nQueens(4)