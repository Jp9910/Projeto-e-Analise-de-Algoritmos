#Lista semanal de PAA - Lista 7 Questão 2
#Aluno: João Paulo Feitosa Secundo

class Node():
    def __init__(self,freq,simb,left=None,right=None) -> None:
        self.freq = freq
        self.left = left
        self.right = right
        self.simb = simb
        self.huff = ''

def arvoreHuffman(T,n):
    frequencia = {}
    for i in range(0,n):
        frequencia[T[i]]=0 #construir dicionario de frequencia
    for i in range(0,n):
        frequencia[T[i]] += 1 #computar frequencia das letras
    simbolos = list(frequencia) #vetor com todos os simbolos
    m = len(frequencia)
    #print(simbolos)
    #print(frequencia)
    nodes = []
    for i in range(0,m):
        nodes.append(Node(frequencia[simbolos[i]] , simbolos[i]))
        #print(nodes[i].freq,nodes[i].simb)

    #print("------")
    montarHeapMinimo(nodes,m) #heap minimo baseado na frequencia
    #for i in range(0,m):
    #    print(nodes[i].freq,nodes[i].simb)
        
    while(len(nodes) > 1):
        el1 = popHeapMin(nodes,m)
        m-=1
        el2 = popHeapMin(nodes,m)
        m-=1
        el1.huff = 0
        el2.huff = 1
        noNavegacao = Node(el1.freq+el2.freq,el1.simb+el2.simb,el1,el2)
        inserirHeapMin(nodes,m,noNavegacao)
        m+=1
    raiz = noNavegacao
    return raiz

def printArvore(A,lado=-1):
    if(A is None):
        return
    if(lado==0): print("esq: ",end="")
    elif(lado==1): print("dir: ",end="")
    print(A.freq,A.simb)
    printArvore(A.left,0)
    printArvore(A.right,1)

def tabelaCodigo(A,codigos,codigo=''):
    #Recebe a raiz da árvore ruffman (A)
    if(A.left is None and A.right is None):
        codigo = codigo + str(A.huff)
        print(A.simb,":",codigo)
        codigos[A.simb] = codigo
    else:
        codigo = codigo + str(A.huff)
        tabelaCodigo(A.left,codigos,codigo)
        tabelaCodigo(A.right,codigos,codigo)

def codificar(msg,n,T):
    #Recebe a msg e a tabela de códigos
    msgCodificada = ""
    for i in range(n):
        msgCodificada += T[msg[i]]
    return msgCodificada

def decodificar(msg,n,node):
    #Recebe a msg e a raiz da arvore de ruffman
    novaMsg = ""
    raiz = node
    for i in range(n):
        if(msg[i]=="0"):
            node = node.left
        elif(msg[i]=="1"):
            node = node.right
        if(node.left is None and node.right is None):
            novaMsg += node.simb
            node = raiz
    return novaMsg

def montarHeapMinimo(A,tamVetor):
    metade = (tamVetor)//2
    for i in range(metade-1,-1,-1):
        heapifyMin(A,i,tamVetor)

def heapifyMin(A,i,tamVetor):
    esq = (2*i)+1
    dir = (2*i)+2
    if(esq < tamVetor and A[esq].freq < A[i].freq):
        maior = esq
    else:
        maior = i

    if(dir < tamVetor and A[dir].freq < A[maior].freq):
        maior = dir
    
    if(maior != i):
        A[i],A[maior] = A[maior],A[i]
        heapifyMin(A,maior,tamVetor)

def inserirHeapMin(A,n,el):
    n=n+1
    A.append(el)
    filho = n-1
    pai = (n-2)//2
    while(pai>=0):
        if(A[pai].freq>A[filho].freq):
            A[pai],A[filho] = A[filho], A[pai]
            filho = pai
            pai = (pai-1)//2
        else:
            pai=-1

def popHeapMin(A,n):
    if(n==0):
        print("Heap Vazio")
        return
    else:
        #print("Removendo a raiz", A[0].simb,A[0].freq)
        raiz = A[0]
        A[0],A[n-1]=A[n-1],A[0]
        A.pop(n-1)
        n=n-1
        rearranjarMinHeap(A,n)
        return raiz

def rearranjarMinHeap(A,n):
    pai = 0
    filho = 1
    while(filho<=n-1):
        if(filho!=n-1 and A[filho].freq>A[filho+1].freq):
            filho=filho+1
        if(A[filho].freq < A[pai].freq):
            A[pai],A[filho]=A[filho],A[pai]
            pai=filho
            filho=(2*filho)+1
        else:
            filho = n

msg = "TESTANDO A COMPRESSAO DE MENSAGENS ASDFQWERASDF"
msg = "ABRACADABRA"
#msg = "asdfzxcvqwertyuighjkbnmoplasdfghjklqwertyuiopzxcvbnm"
n = len(msg)
raiz = arvoreHuffman(msg,n)

print("----Arvore----")
printArvore(raiz)

print("----Codigos----")
codigos = {}
tabelaCodigo(raiz,codigos)
print(codigos)

print("----Msg Codificada----")
msgCodificada = codificar(msg,n,codigos)
print(msgCodificada)

print("----Nova msg recomposta----")
novaMsg = decodificar(msgCodificada,len(msgCodificada),raiz)
print(novaMsg)