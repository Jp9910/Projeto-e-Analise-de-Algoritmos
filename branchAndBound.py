class Tarefa():
    def __init__(self) -> None:
        self.alocada = False

class Pessoa():
    def __init__(self) -> None:
        self.alocada = False

class Assignment():
    def __init__(self,p,t,c) -> None:
        self.p = p
        self.t = t
        self.c = c

def branchAndBound(C,n,lb,R,p,P,T):
    bestLB = lb #18
    for p in range(0,n):
        lb = bestLB
        T[i].alocada = True
        for i in range(0,n):
            lb=lb-R[p].c+C[p][i]
            if(lb < bestLB and T[i].alocada==False):
                R[p]=Assignment(p,i,C[p][i])
                bestLB = lb
        
    printa(R)
    print(bestLB)
    #branchAndBound(C,n,lb,R,r+1)

def inicio(C,n,P,T):
    lowerboundInicial=0
    R = [0]*n
    for i in range(0,n):
        lowerboundInicial += C[i][i]
        R[i] = Assignment(i,i,C[i][i])
    print("R inicial:")
    printa(R)
    print("lb inicial:",lowerboundInicial)
    branchAndBound(C,n,lowerboundInicial,R,0,P,T)

def printa(R):
    for i in range(0,len(R)):
        print("Pessoa",R[i].p,"Tarefa",R[i].t,"Custo",R[i].c)

C = [[9,2,7,8],[6,4,3,7],[5,8,1,8],[7,6,9,4]]
T = [Tarefa(),Tarefa(),Tarefa(),Tarefa()]
P = [Pessoa(),Pessoa(),Pessoa(),Pessoa()]
#C[i][j] representa o custo da pessoa i fazer a tareja j
#pessoa = linha
#tarefa = coluna
inicio(C,len(C),P,T)