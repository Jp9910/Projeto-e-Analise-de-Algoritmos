#Lista semanal de PAA - Lista 13 Questão 2
#Aluno: João Paulo Feitosa Secundo

import random

### USANDO BERNOULLI TRIAL ###
#x = (0.6**9) + (0.4*(0.6**8)) + ((0.4**2)*(0.6**7)) + ((0.4**3)*(0.6**6)) + ((0.4**4)*(0.6**5)) + ((0.4**5)*(0.6**4)) + ((0.4**6)+(0.6**3)) + ((0.4**7)+(0.6**2)) + ((0.4**8)*(0.6**1)) + (0.4**9)
def escolhaJusta(): #51%=1 e 49%=0
    #b = [-1]*9
    cont=0
    for i in range(0,9):
        b = escolha() #60%=0 e 40%=1
        if(b==1):
            cont=cont+1
    #print(b)
    if(cont>=4):
        return 1
    else:
        return 0

### USANDO INVERSO DA FUNCAO ESCOLHA() ###
def escolhaJusta2(): #50%=1 e 50%=0
    a = escolha() # a --> 60%=0 ou 40%=1
    b = escolha() 
    if(b==1): b=0 # b --> 60%=1 ou 40%=0
    elif(b==0): b=1 # b --> 60%=1 ou 40%=0
    print('a:',a,'b:',b,'a+b:',a+b)
    if(a+b==1):
        return escolhaJusta2()
    return (a + b)/2

def escolha():
    a = random.randint(1,10)
    if(a>=7): #7,8,9,10
        return 1
    else: #1,2,3,4,5,6
        return 0

x = escolhaJusta2()
print(x)