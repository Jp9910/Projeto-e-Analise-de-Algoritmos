class Ponto():
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y

class Reta():
    def __init__(self,a,b) -> None:
        self.ponto1 = a
        self.ponto2 = b

class Poligono():
    def __init__(self,v=None,a=None) -> None:
        self.vertices = v
        self.arestas = a

def produtoVetorialAPxBQ(a,p,b,q):
    return ((p.x-a.x) * (q.y-b.y)) - ((q.x-b.x)*(p.y-a.y))

def produtoVetorialComRetas(retaAP,retaBQ):
    return ((retaAP.ponto2.x - retaAP.ponto1.x) * (retaBQ.ponto2.y-retaBQ.ponto1.y)) \
            - ((retaBQ.ponto2.x-retaBQ.ponto1.x)*(retaAP.ponto2.y-retaAP.ponto1.y))

def segmentoPQehHorarioOuAntiEmRelacaoaPR(p,q,r):
    #entrada: pontos dos segmentos PQ e PR
    #saída: -1 se PQ for anti-horário em relação à PR, 0 se for colinear e 1 se for horário.
    #Complexidade: O(1)
    #-p.x e -p.y é para transladar as retas para a origem
    #produtoVetorial = ((q.x -p.x )*(r.y -p.y )) - ((r.x -p.x )*(q.y -p.y ))
    produtoVetorial = produtoVetorialAPxBQ(p,q,p,r)
    if(produtoVetorial > 0):
        return 1 #horário
    elif(produtoVetorial < 0):
        return -1 #anti-horário
    else:
        return 0 #colinear

def viraEsqOuDirPercorrendoPQeQR(p,q,r):
    #entrada: pontos dos segmentos PQ e QR
    #saída: -1 se vira a esquerda, 0 se não vira, ou 1 se vira a direita
    #Complexidade: O(1)
    #-p.x e -p.y é para transladar as retas para a origem
    
    #produtoVetorial = ((r.x -p.x )*(q.y -p.y )) - ((q.x -p.x )*(r.y -p.y ))
    produtoVetorial = produtoVetorialAPxBQ(p,r,p,q)
    #produtoVetorial = produtoVetorialComRetas(Reta(p,r),Reta(p,q))
    if(produtoVetorial > 0):
        return 1 #horário = vira direita
    elif(produtoVetorial < 0):
        return -1 #anti-horário = vira esquerda
    else:
        return 0 #colinear = não vira

def retasSeInterceptamOuNao(retaPQ,retaRS):
    #entrada: duas retas PQ e RS
    #saída: True se as retas se interceptam. False se não.
    #Complexidade: O(1)
    def direcao(p,AB):
        #entrada: ponto p e reta AB
        #saída: produto vetorial de (p-a) x (b-a)
        return ((p.x-AB.ponto1.x)*(AB.ponto2.y-AB.ponto1.y))\
                -((AB.ponto2.x-AB.ponto1.x)*(p.y-AB.ponto1.y))

    def noSegmento(p,AB):
        #verifica se um ponto p colinear a A e a B está ou não no segmento AB
        menorX = min(AB.ponto1.x,AB.ponto2.x)
        menorY = min(AB.ponto1.y,AB.ponto2.y)
        maiorX = max(AB.ponto1.x,AB.ponto2.x)
        maiorY = max(AB.ponto1.y,AB.ponto2.y)
        if(p.x >= menorX) and (p.x <= maiorX) and (p.y >= menorY) and (p.y <= maiorY):
            return True
        else:
            return False
    dp = direcao(retaPQ.ponto1,retaRS)
    dq = direcao(retaPQ.ponto2,retaRS)
    dr = direcao(retaRS.ponto1,retaPQ)
    ds = direcao(retaRS.ponto2,retaPQ)
    if((dp > 0 and dq <0) or (dp < 0 and dq >0)) and ((dr > 0 and ds < 0) or (dr < 0 and ds >0)):
        return True
    else: #checa se está no sucesso do Caso 2
        if (dp == 0 and noSegmento(retaPQ.ponto1,retaRS)):
            return True
        elif (dq == 0 and noSegmento(retaPQ.ponto2,retaRS)):
            return True
        elif (dr == 0 and noSegmento(retaRS.ponto1,retaPQ)):
            return True
        elif (ds == 0 and noSegmento(retaRS.ponto2,retaPQ)):
            return True
        else:
            return False #insucesso dos casos 1 e 2

def pontoDentroOuForaDoPoligono(P,z):
    #entrada: Poligono P representado por seus vertices (um vetor de pontos). E um ponto z
    #saída: True caso z esteja dentro de P. False caso contrário
    #não lida com os casos especiais
    maiorx = P.vertices[0].x
    maiory = P.vertices[0].y
    
    #determinar maior coordenada x e y do poligono
    for i in range(1,len(P.vertices)):
        if(P.vertices[i].x > maiorx): maiorx = P.vertices[i].x
        if(P.vertices[i].y > maiory): maiory = P.vertices[i].y
    
    #definir um ponto fora do polígono
    s = Ponto(maiorx+2,maiory+2)

    #computar número de interseções
    cont=0
    for i in range(0,len(P.vertices)-1):
        if(retasSeInterceptamOuNao(Reta(s,z),Reta(P.vertices[i],P.vertices[i+1]))):
            cont=cont+1
    if(cont%2==0):
        return False #numero de intersessoes par = z está fora de P
    else: return True #numero de intersessoes impar = z está dentro de P

def trassarPoligonoSimples(pontos): #O(nlogn)
    #Entrada: n pontos p1, p2, ..., pn no plano, armazenados no vetor P. Cada elemento \
    #   de P possui três atributos: x, y e slope (inclinação)
    #Saída: Polígono P representado pela sequência dos pontos de entrada em uma dada \
    #   ordem tal que forme um polígono simples.
    #não lida com os casos especiais
    def pontoExtremo(pontos,n): #O(n)
        #Entrada: vetor pontos de n pontos
        #Saída: índice do ponto extremo (maior coordenada x, com menor y como desempate)
        extremo = 0
        for i in range(1,n):
            if(pontos[i].x > pontos[extremo].x) or ((pontos[i].x == pontos[extremo].x)and(pontos[i].y < pontos[extremo].y)):
                extremo = i
        return extremo
        
    def calcularSlope(slope,n): #O(n)
        #Entrada: vetor de 0s slope de tamanho n
        #Saída: inclinações entre (pontos[0] e pontos[i]) calculadas. Também \
        #   retorna a menor inclinação obtida.
        #Não considera casos de pontos com mesma coordenada x.
        slope[1] = (pontos[1].y - pontos[0].y)/(pontos[1].x-pontos[0].x)
        minSlope = slope[1]
        for i in range(2,n):
            slope[i] = (pontos[i].y - pontos[0].y)/(pontos[i].x - pontos[0].x)
            if(slope[i] < minSlope):
                minSlope = slope[i]
        return minSlope

    n = len(pontos)
    slope = [0]*n

    #determinar o ponto extremo mais à direita e coloca-lo na primeira posição
    extremo = pontoExtremo(pontos,n)
    pontos[extremo],pontos[0] = pontos[0],pontos[extremo]
    #calculo da inclinação entre o ponto extremo(pontos[0]) e todos os pontos
    #e devolve o mínimo entre eles
    minSlope = calcularSlope(slope,n)
    #ordenar os pontos de acordo com a inclinação.
    slope[0] = minSlope - 1
    #print(slope)
    #for i in range(0,n):
    #    print(pontos[i].x,pontos[i].y,end=' ')
    #    print(slope[i])
    heapSortSlope(slope,n,pontos) #O(nlogn)
    #for i in range(0,n):
    #    print(pontos[i].x,pontos[i].y,end=' ')
    #    print(slope[i])

def heapSortSlope(A,n,pontos): #O(n*lg(n))
    montarHeapMaximo(A,n,pontos)
    #print("heapSort heap montado: ",A)
    for i in range(n-1,0,-1):
        A[0],A[i]=A[i],A[0]
        pontos[0],pontos[i]=pontos[i],pontos[0]
        rearranjarMaxHeap(A,i,pontos)
        #print("heap rearranjado: ",A)

def montarHeapMaximo(A,tamVetor,pontos):
    metade = (tamVetor)//2
    for i in range(metade-1,-1,-1):
        heapifyMax(A,i,tamVetor,pontos)

def heapifyMax(A,i,tamVetor,pontos):
    esq = (2*i)+1
    dir = (2*i)+2
    if(esq < tamVetor and A[esq] > A[i]):
        maior = esq
    else:
        maior = i
    if(dir < tamVetor and A[dir] > A[maior]):
        maior = dir
    if(maior != i):
        A[i],A[maior] = A[maior],A[i]
        pontos[i],pontos[maior] = pontos[maior],pontos[i]
        heapifyMax(A,maior,tamVetor,pontos)

def rearranjarMaxHeap(A,n,pontos):
    pai = 0
    filho = 1
    while(filho<=n-1):
        #print(A);print(A[pai],A[filho])
        if(filho!=n-1 and A[filho]<A[filho+1]):
            filho=filho+1
        if(A[filho] > A[pai]):
            A[pai],A[filho]=A[filho],A[pai]
            pontos[pai],pontos[filho]=pontos[filho],pontos[pai]
            pai=filho
            filho=(2*filho)+1
        else:
            filho = n

def graham(P):
    #Entrada: Conjunto de n pontos em P
    #Saída: envoltória convexa em H
    #Não trata os casos especiais (apenas pontos colineares ou apenas 1 ou 2 pontos)

    #construir o polígono simples
    trassarPoligonoSimples(P)
    n = len(P)

    #inicializar primeiros pontos de H
    H = [None]*n
    H[0] = P[0]; H[1] = P[1]; H[2] = P[2]; m = 2
    
    #construir o caminho
    for i in range(3,n):
        while(viraEsqOuDirPercorrendoPQeQR(H[m-1],H[m],P[i]) == 1):
            m=m-1 #vira a direita (maior que 180 graus). retroceder m
        m=m+1
        H[m] = P[i]
    
    return H,m

def jarvismarch(points):
    def _dist(p, q):
        dx, dy = q[0] - p[0], q[1] - p[1]
        return dx * dx + dy * dy

    def _next_hull_pt(points, p):
        q = p
        for r in points:
            t = viraEsqOuDirPercorrendoPQeQR(p, q, r)
            if t == 1 or t == 0 and _dist(p, r) > _dist(p, q):
                q = r
        return q

    hull = [min(points)]
    for p in hull:
        q = _next_hull_pt(points, p)
        if q != hull[0]:
            hull.append(q)
    return hull
    
def pontoExtremo(pontos,n): #O(n)
        #Entrada: vetor pontos de n pontos
        #Saída: índice do ponto extremo (maior coordenada x, com menor y como desempate)
        extremo = 0
        for i in range(1,n):
            if(pontos[i].x > pontos[extremo].x) or ((pontos[i].x == pontos[extremo].x)and(pontos[i].y < pontos[extremo].y)):
                extremo = i
        return extremo

p = Ponto(10,10)
q = Ponto(11,9)
r = Ponto(-1,3)
s = Ponto(3,3)
#desenhar um plano cartesiano para melhor visualização
problema1 = segmentoPQehHorarioOuAntiEmRelacaoaPR(p,q,r)
print("Segmento PQ é horário ou anti-horário em relação à PR?",problema1)

problema2 = viraEsqOuDirPercorrendoPQeQR(p,q,r)
print("De PQ à QR, em Q vira-se à esquerda ou direita?",problema2)

#p = Ponto(1,1);q=Ponto(2,2);r = Ponto(1,1);s=Ponto(3,3)
problema3 = retasSeInterceptamOuNao(Reta(p,q),Reta(r,s))
print("retas PQ e RS se interceptam?",problema3)

#definir o polígono com pontos na ordem anti-horária
poligono = Poligono([Ponto(-1,-1),Ponto(-4,-1),Ponto(-1,-4)])
z = Ponto(-2,-2)
problema4 = pontoDentroOuForaDoPoligono(poligono,z)
print("Ponto z está dentro do polígono?",problema4)

pontos = [Ponto(-1,2),Ponto(-1,-1),Ponto(1,0),Ponto(2,2),Ponto(2,-2),Ponto(3,3),Ponto(4,0),Ponto(3,-3)]
trassarPoligonoSimples(pontos)
print("\nPoligono simples:")
for i in range(0,len(pontos)):
        print(pontos[i].x,pontos[i].y,end=' --> ')

print("\n---------------------------------------------------------\n")
envoltoria,m = graham(pontos)
print("\nEnvoltória graham:")
for i in range(0,m+1):
    print(envoltoria[i].x,envoltoria[i].y,end=' --> ')

pontos = [Ponto(-1,2),Ponto(-1,-1),Ponto(1,0),Ponto(2,2),Ponto(2,-2),Ponto(3,3),Ponto(4,0),Ponto(3,-3)]
envoltoria = jarvismarch(pontos)
print("\n\nEnvoltória jarvisMarch:")
for i in range(0,len(envoltoria)):
    print(envoltoria[i].x,envoltoria[i].y,end=' --> ')
