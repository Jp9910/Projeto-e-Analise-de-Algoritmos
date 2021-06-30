
def rabinkarp(T,n,P,m):
    q = 3354393 #numero primo muito grande
    d = 32 #palavra do computador
    dM = 1
    for i in range(0,m-1):
        dM = (d*dM) % q #calcula a maior potência (d^m-1) que vai ser usada na
                        #remoçao do primeiro caractere da subcadeia do texto
    h1 = 0 #padrao
    h2 = 0 #texto
    for i in range(0,m):
        h1 = (h1*d+ord(P[i]))%q #hash do padrao só é calculado uma vez
        h2 = (h2*d+ord(T[i]))%q #calcula o hash do texto para os m primeiros caracteres

    i=0
    while(h1 != h2 and i < n-m):
        h2 = (h2 + d*q - ord(T[i])*dM )%q #remove o primeiro caractere da equação
        h2 = (h2*d + ord(T[i+m]))%q #e adiciona o proximo
        i=i+1 #avança o texto
    
    cont=0
    print(i,n-m)
    for j in range(i,i+m): #checagem para ver se não é falso positivo
        if(T[j] == P[j-i]):
            cont+=1
    if(cont==m):
        return i
    else: return -1

T = "3141592653589793"
P = "26"
n = len(T)
m = len(P)
resultado = rabinkarp(T,n,P,m)
print("indice da primeira letra:",resultado)