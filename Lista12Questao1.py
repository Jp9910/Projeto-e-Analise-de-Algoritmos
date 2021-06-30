#Lista semanal de PAA - Lista 12 Questão 1
#Aluno: João Paulo Feitosa Secundo

def digitoValido(digito,n) -> bool:
    #checa se a soma dos dígitos das posições pares é igual
    # à soma dos dígitos das posições ímpares.
    if(digito[0]==0):
        return False
    somaImpares = 0;k=1
    somaPares = 0;m=0
    while(k < n):
        somaImpares = somaImpares + digito[k]
        k=k+2
    while(m < n):
        somaPares = somaPares + digito[m]
        m=m+2

    if(somaPares == somaImpares):
        return True
    else: return False

def nDigitos(num,digito,n,X):
    #Entrada: n-digito 'num', com forma vetorial 'digito'
    #Saída: lista X contendo todos os n-digitos tal que a soma dos dígitos das
    #       posições pares seja igual à soma dos dígitos das posições ímpares.

    while(len(digito)==n):
        if(digitoValido(digito,n)):
            X.append(num)
        num=num+1
        digito = [int(x) for x in str(num)]

    return X

def nDigitosRecursivo(num,digito,n,X):
    digito = [int(x) for x in str(num)]
    if(len(digito)!=n):
        return
    if(digitoValido(digito,n)):
        X.append(num)
    nDigitosRecursivo(num+1,digito,n,X)

def nDigitosBackTracking(digito,d,n,X):

    if(d==n):
        return
    for i in range(0,10):
        digito[d] = i
        if(d == n-1 and digitoValido(digito,n)):
            strings = [str(integer) for integer in digito] # converter de lista para int
            a_string = "".join(strings) # converter de lista para int
            an_integer = int(a_string) # converter de lista para int
            #if(an_integer in X):
            #    breakpointDebug=1
            X.append(an_integer)
        nDigitosBackTracking(digito,d+1,n,X)
    

def nd(n):
    #Entrada: Tamanho n dos digitos
    #Saída: Solução armazenada na lista X
    
    #Pré-processamento necessario apenas para a função iterativa ou recursiva.
    #num=1
    #digito = [1]
    #while(len(digito) < n):
    #    num=num*10
    #    digito = [int(x) for x in str(num)] #transformar o número em um vetor

    digito = [0]*n
    print("\nN-DIGITOS BACKTRACKING")
    X = []
    nDigitosBackTracking(digito,0,n,X)

    return X

X = nd(3)
print(X)